"""Closed admin input invariants independently of a running database."""

import pytest
from pydantic import ValidationError

from nextops.contracts.users import UserCreateRequest, UserPasswordRequest, UserStatusRequest


@pytest.mark.parametrize("role", ["admin", "root", "viewer,admin", "", 0, None])
def test_user_creation_cannot_select_administrator_or_arbitrary_role(role: object) -> None:
    with pytest.raises(ValidationError):
        UserCreateRequest.model_validate(
            {"username": "reader", "password": "local fixture password", "role": role}
        )


@pytest.mark.parametrize(
    "field", ["scopes", "organization_id", "environment_id", "is_active", "roles"]
)
def test_user_creation_rejects_authority_and_status_injection(field: str) -> None:
    with pytest.raises(ValidationError):
        UserCreateRequest.model_validate(
            {"username": "reader", "password": "local fixture password", field: []}
        )


@pytest.mark.parametrize("value", ["false", "true", 0, 1, None, [], {}])
def test_account_status_requires_actual_boolean(value: object) -> None:
    with pytest.raises(ValidationError):
        UserStatusRequest.model_validate({"is_active": value, "expected_version": 1})


@pytest.mark.parametrize("password", ["", "x" * 13, "x" * 257])
def test_both_password_routes_have_length_bounds(password: str) -> None:
    with pytest.raises(ValidationError):
        UserCreateRequest(username="reader", password=password)
    with pytest.raises(ValidationError):
        UserPasswordRequest(new_password=password, expected_version=1)


def test_secret_is_not_exposed_by_contract_representation() -> None:
    password = "local fixture password only"
    assert password not in repr(UserCreateRequest(username="reader", password=password))
    assert password not in repr(UserPasswordRequest(new_password=password, expected_version=1))
