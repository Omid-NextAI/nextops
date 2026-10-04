"""Closed local account administration contracts; no caller-selected scopes."""

from typing import Literal
from uuid import UUID

from pydantic import AwareDatetime, Field, SecretStr, StrictBool

from nextops.contracts.durable import Username
from nextops.contracts.models import FrozenContract

ManagedRole = Literal["viewer", "operator", "engineer"]


class UserCreateRequest(FrozenContract):
    username: Username
    password: SecretStr = Field(min_length=14, max_length=256, repr=False)
    role: ManagedRole = "viewer"


class UserStatusRequest(FrozenContract):
    is_active: StrictBool
    expected_version: int = Field(strict=True, ge=1)


class UserPasswordRequest(FrozenContract):
    new_password: SecretStr = Field(min_length=14, max_length=256, repr=False)
    expected_version: int = Field(strict=True, ge=1)


class UserRecord(FrozenContract):
    identity_id: UUID
    username: Username
    roles: tuple[str, ...] = Field(min_length=1, max_length=4)
    is_active: bool
    credential_version: int = Field(ge=1)
    created_at: AwareDatetime
    manageable: bool


class UserPage(FrozenContract):
    users: tuple[UserRecord, ...] = Field(max_length=50)
    next_offset: int | None = Field(default=None, ge=0)
