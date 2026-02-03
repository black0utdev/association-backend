"""Tests for Email value object."""

import pytest

from app.domain.value_objects.email import Email


def test_create_email_with_valid_format() -> None:
	"""Should create Email with valid format."""
	email = Email("user@example.com")

	assert email.value == "user@example.com"
	assert str(email) == "user@example.com"


def test_create_email_with_invalid_format_raises_error() -> None:
	"""Should raise ValueError for invalid email format."""
	with pytest.raises(ValueError, match="Invalid email format"):
		Email("invalid-email")


def test_create_email_without_domain_raises_error() -> None:
	"""Should raise ValueError for email without domain."""
	with pytest.raises(ValueError, match="Invalid email format"):
		Email("user@")


def test_create_email_without_at_symbol_raises_error() -> None:
	"""Should raise ValueError for email without @ symbol."""
	with pytest.raises(ValueError, match="Invalid email format"):
		Email("userexample.com")


def test_email_is_immutable() -> None:
	"""Should be immutable (frozen dataclass)."""
	email = Email("user@example.com")

	with pytest.raises(AttributeError, match="can't set attribute|has no setter"):
		email.value = "changed@example.com"  # type: ignore


def test_emails_with_same_value_are_equal() -> None:
	"""Should be equal if values are the same."""
	email1 = Email("user@example.com")
	email2 = Email("user@example.com")

	assert email1 == email2
