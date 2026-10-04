"""Local admin controls: authoritative sessions, bounded scope, atomic audit/revocation."""

from collections.abc import Callable
from datetime import UTC, datetime
from typing import Literal, TypeVar
from uuid import UUID, uuid4

from sqlalchemy import func, select, text, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode
from nextops.contracts.users import (
    UserCreateRequest,
    UserPage,
    UserPasswordRequest,
    UserRecord,
    UserStatusRequest,
)
from nextops.persistence.models import AuditEvent, Identity
from nextops.persistence.models import Session as SessionModel
from nextops.security.secrets import PasswordService, hash_opaque_token

T = TypeVar("T")
UserOperation = Literal["list", "create", "status", "password_reset"]
MAX_USERS = 500
ROLE_SCOPES = {
    "viewer": ["runs.read", "zabbix.read"],
    "operator": ["linux.read", "runs.read", "zabbix.read"],
    "engineer": ["linux.read", "runs.read", "zabbix.read"],
}


class DurableUserService:
    """Does not hold connector credentials or grant administrator/infrastructure mutations."""

    def __init__(
        self,
        factory: sessionmaker[Session],
        *,
        clock: Callable[[], datetime] | None = None,
        passwords: PasswordService | None = None,
    ) -> None:
        self._factory = factory
        self._clock = clock or (lambda: datetime.now(UTC))
        self._passwords = passwords or PasswordService()

    def _run(
        self,
        token: str,
        correlation_id: UUID,
        operation: str,
        target_id: UUID | None,
        execute: Callable[[Session, Identity, datetime], T],
    ) -> T:
        pending: ApplicationError | None = None
        result: T
        try:
            with self._factory() as session, session.begin():
                session.execute(text("SET LOCAL lock_timeout = '1500ms'"))
                session.execute(text("SET LOCAL statement_timeout = '5s'"))
                predicate = (
                    SessionModel.token_sha256 == hash_opaque_token(token),
                    SessionModel.revoked_at.is_(None),
                    SessionModel.expires_at > self._clock(),
                    SessionModel.credential_version == Identity.credential_version,
                    Identity.is_active.is_(True),
                )
                binding = session.scalar(
                    select(Identity.environment_id)
                    .join(SessionModel, SessionModel.identity_id == Identity.id)
                    .where(*predicate)
                )
                if binding is None:
                    raise ApplicationError(ErrorCode.UNAUTHENTICATED, "auth.session_required")
                # Trusted environment-derived advisory key, not user input. Serializes quota
                # and updates without granting UPDATE on environments or authorization columns.
                session.execute(select(func.pg_advisory_xact_lock(binding.int % (2**63 - 1))))
                now = self._clock()
                actor = session.scalar(
                    select(Identity)
                    .join(SessionModel, SessionModel.identity_id == Identity.id)
                    .where(
                        SessionModel.token_sha256 == hash_opaque_token(token),
                        SessionModel.revoked_at.is_(None),
                        SessionModel.expires_at > now,
                        SessionModel.credential_version == Identity.credential_version,
                        Identity.is_active.is_(True),
                        Identity.environment_id == binding,
                    )
                    .with_for_update(of=(Identity, SessionModel))
                )
                if actor is None:
                    raise ApplicationError(ErrorCode.UNAUTHENTICATED, "auth.session_required")
                if "admin" not in actor.roles:
                    pending = ApplicationError(ErrorCode.POLICY_DENIED, "users.admin_required")
                else:
                    try:
                        with session.begin_nested():
                            result = execute(session, actor, now)
                            session.flush()
                    except IntegrityError:
                        pending = ApplicationError(ErrorCode.CONFLICT, "users.username_conflict")
                    except ApplicationError as error:
                        pending = error
                audited_target = target_id
                if pending is None and isinstance(result, UserRecord):
                    audited_target = result.identity_id
                # No password, username, token, scopes or response payload in security audit.
                session.add(
                    AuditEvent(
                        id=uuid4(),
                        organization_id=actor.organization_id,
                        environment_id=actor.environment_id,
                        actor_id=actor.id,
                        correlation_id=correlation_id,
                        event_type=f"identity.users.{operation}",
                        outcome="denied" if pending else "accepted",
                        details={
                            "target_identity_id": str(audited_target) if audited_target else None,
                            "error_code": pending.code.value if pending else None,
                        },
                        occurred_at=now,
                    )
                )
                session.flush()
        except SQLAlchemyError:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "users.transaction_failed", retryable=True
            ) from None
        if pending:
            raise pending
        return result

    @staticmethod
    def _record(identity: Identity) -> UserRecord:
        return UserRecord(
            identity_id=identity.id,
            username=identity.username,
            roles=tuple(identity.roles),
            is_active=identity.is_active,
            credential_version=identity.credential_version,
            created_at=identity.created_at,
            manageable="admin" not in identity.roles,
        )

    def reject_invalid_request(
        self,
        token: str,
        correlation_id: UUID,
        operation: UserOperation,
        target_id: UUID | None,
    ) -> None:
        """Audit a schema rejection through the same fresh session/role transaction."""

        def execute(session: Session, actor: Identity, now: datetime) -> None:
            raise ApplicationError(ErrorCode.INVALID_REQUEST, "request.validation_failed")

        self._run(token, correlation_id, operation, target_id, execute)

    def list(self, token: str, correlation_id: UUID, offset: int = 0) -> UserPage:
        if not 0 <= offset <= MAX_USERS:
            raise ApplicationError(ErrorCode.INVALID_REQUEST, "users.invalid_page")

        def execute(session: Session, actor: Identity, now: datetime) -> UserPage:
            rows = list(
                session.scalars(
                    select(Identity)
                    .where(
                        Identity.organization_id == actor.organization_id,
                        Identity.environment_id == actor.environment_id,
                    )
                    .order_by(Identity.username, Identity.id)
                    .offset(offset)
                    .limit(51)
                )
            )
            return UserPage(
                users=tuple(self._record(row) for row in rows[:50]),
                next_offset=offset + 50 if len(rows) > 50 else None,
            )

        return self._run(token, correlation_id, "list", None, execute)

    def create(self, token: str, correlation_id: UUID, request: UserCreateRequest) -> UserRecord:
        def execute(session: Session, actor: Identity, now: datetime) -> UserRecord:
            count = session.scalar(
                select(func.count())
                .select_from(Identity)
                .where(
                    Identity.organization_id == actor.organization_id,
                    Identity.environment_id == actor.environment_id,
                )
            )
            if count is None or count >= MAX_USERS:
                raise ApplicationError(ErrorCode.OVERLOADED, "users.limit_reached")
            identity = Identity(
                id=uuid4(),
                organization_id=actor.organization_id,
                environment_id=actor.environment_id,
                username=request.username,
                password_hash=self._passwords.hash(request.password.get_secret_value()),
                roles=[request.role],
                scopes=ROLE_SCOPES[request.role].copy(),
                is_active=True,
                credential_version=1,
                created_at=now,
                updated_at=now,
            )
            session.add(identity)
            session.flush()
            return self._record(identity)

        return self._run(token, correlation_id, "create", None, execute)

    def change_status(
        self, token: str, correlation_id: UUID, target_id: UUID, request: UserStatusRequest
    ) -> UserRecord:
        return self._change(token, correlation_id, target_id, request)

    def reset_password(
        self, token: str, correlation_id: UUID, target_id: UUID, request: UserPasswordRequest
    ) -> UserRecord:
        return self._change(token, correlation_id, target_id, request)

    def _change(
        self,
        token: str,
        correlation_id: UUID,
        target_id: UUID,
        request: UserStatusRequest | UserPasswordRequest,
    ) -> UserRecord:
        def execute(session: Session, actor: Identity, now: datetime) -> UserRecord:
            identity = session.scalar(
                select(Identity)
                .where(
                    Identity.id == target_id,
                    Identity.organization_id == actor.organization_id,
                    Identity.environment_id == actor.environment_id,
                )
                .with_for_update()
            )
            if identity is None:
                raise ApplicationError(ErrorCode.NOT_FOUND, "users.not_found")
            if "admin" in identity.roles or identity.id == actor.id:
                raise ApplicationError(ErrorCode.POLICY_DENIED, "users.admin_protected")
            if identity.credential_version != request.expected_version:
                raise ApplicationError(ErrorCode.CONFLICT, "users.version_conflict")
            if isinstance(request, UserStatusRequest):
                identity.is_active = request.is_active
            else:
                identity.password_hash = self._passwords.hash(
                    request.new_password.get_secret_value()
                )
            identity.credential_version += 1
            identity.updated_at = now
            session.execute(
                update(SessionModel)
                .where(
                    SessionModel.identity_id == identity.id,
                    SessionModel.revoked_at.is_(None),
                )
                .values(revoked_at=now)
            )
            return self._record(identity)

        operation = "status" if isinstance(request, UserStatusRequest) else "password_reset"
        return self._run(token, correlation_id, operation, target_id, execute)
