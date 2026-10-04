"""Current-session source authorization and mandatory PostgreSQL access audit."""

from datetime import UTC, datetime
from typing import Literal
from uuid import UUID, uuid4

from sqlalchemy import select, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode
from nextops.contracts.models import ActorContext, Role
from nextops.contracts.source_catalog import SourceCatalog
from nextops.contracts.sources import SourceReadBinding
from nextops.persistence.models import AuditEvent, Identity
from nextops.persistence.models import Session as SessionModel
from nextops.security.secrets import hash_opaque_token


class DurableSourceAccess:
    def __init__(self, factory: sessionmaker[Session]) -> None:
        self._factory = factory

    def record(
        self,
        token: str,
        correlation_id: UUID,
        outcome: Literal["catalog", "started", "completed", "failed"],
        binding: SourceReadBinding | None = None,
        digest: str | None = None,
    ) -> ActorContext:
        pending: ApplicationError | None = None
        try:
            with self._factory() as session, session.begin():
                session.execute(text("SET LOCAL lock_timeout = '1500ms'"))
                session.execute(text("SET LOCAL statement_timeout = '5s'"))
                now = datetime.now(UTC)
                identity = session.scalar(
                    select(Identity)
                    .join(SessionModel, SessionModel.identity_id == Identity.id)
                    .where(
                        SessionModel.token_sha256 == hash_opaque_token(token),
                        SessionModel.revoked_at.is_(None),
                        SessionModel.expires_at > now,
                        SessionModel.credential_version == Identity.credential_version,
                        Identity.is_active.is_(True),
                    )
                    .with_for_update(read=True, of=(Identity, SessionModel))
                )
                if identity is None:
                    raise ApplicationError(ErrorCode.UNAUTHENTICATED, "auth.session_invalid")
                if "zabbix.read" not in identity.scopes or (
                    binding is not None
                    and (
                        identity.organization_id != binding.organization_id
                        or identity.environment_id != binding.environment_id
                    )
                ):
                    pending = ApplicationError(
                        ErrorCode.POLICY_DENIED, "connector.source_scope_denied"
                    )
                actor = ActorContext(
                    subject_id=identity.id,
                    organization_id=identity.organization_id,
                    environment_id=identity.environment_id,
                    roles=frozenset(Role(r) for r in identity.roles),
                    scopes=frozenset(identity.scopes),
                )
                session.add(
                    AuditEvent(
                        id=uuid4(),
                        organization_id=identity.organization_id,
                        environment_id=identity.environment_id,
                        actor_id=identity.id,
                        correlation_id=correlation_id,
                        event_type=f"monitoring.source.{outcome}",
                        outcome="denied"
                        if pending
                        else "failed"
                        if outcome == "failed"
                        else "accepted",
                        details={
                            "source_id": binding.source_id if binding else None,
                            "target_id": binding.target_id if binding else None,
                            "evidence_sha256": digest,
                            "error_code": pending.code.value if pending else None,
                        },
                        occurred_at=now,
                    )
                )
                session.flush()
        except SQLAlchemyError:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "monitoring.audit_unavailable"
            ) from None
        if pending:
            raise pending
        return actor

    def catalog(self, token: str, correlation_id: UUID, catalog: SourceCatalog) -> SourceCatalog:
        actor = self.record(token, correlation_id, "catalog")
        return catalog.model_copy(
            update={
                "sources": tuple(
                    s
                    for s in catalog.sources
                    if s.organization_id == actor.organization_id
                    and s.environment_id == actor.environment_id
                )
            }
        )
