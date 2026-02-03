"""Unit tests for User entity."""

import pytest
from datetime import datetime

from app.domain.entities.user import User
from app.domain.value_objects.email import Email


def test_create_user_with_valid_data() -> None:
	"""Should create user with valid data."""
	email = Email("john.doe@example.com")
	user = User(
		name="John Doe",
		email=email,
	)

	assert user.name == "John Doe"
	assert user.email.value == "john.doe@example.com"
	assert user.id is None
	assert user.created_at is None
	assert user.updated_at is None
	assert user.is_active is True


def test_create_user_with_all_fields() -> None:
	"""Should create user with all fields."""
	email = Email("jane.doe@example.com")
	created_at = datetime(2024, 1, 1, 12, 0, 0)
	updated_at = datetime(2024, 1, 2, 12, 0, 0)

	user = User(
		id=1,
		name="Jane Doe",
		email=email,
		is_active=False,
		created_at=created_at,
		updated_at=updated_at,
	)

	assert user.id == 1
	assert user.name == "Jane Doe"
	assert user.email.value == "jane.doe@example.com"
	assert user.is_active is False
	assert user.created_at == created_at
	assert user.updated_at == updated_at


def test_user_change_email() -> None:
	"""Should change user email."""
	email = Email("old@example.com")
	user = User(name="John Doe", email=email)

	new_email = Email("new@example.com")
	user.change_email(new_email)

	assert user.email.value == "new@example.com"


def test_user_deactivate() -> None:
	"""Should deactivate user."""
	email = Email("john@example.com")
	user = User(name="John Doe", email=email)

	assert user.is_active is True

	user.deactivate()

	assert user.is_active is False


def test_user_activate() -> None:
	"""Should activate user."""
	email = Email("john@example.com")
	user = User(name="John Doe", email=email, is_active=False)

	assert user.is_active is False

	user.activate()

	assert user.is_active is True


def test_user_update_name() -> None:
	"""Should update user name."""
	email = Email("john@example.com")
	user = User(name="John Doe", email=email)

	user.update_name("Jane Doe")

	assert user.name == "Jane Doe"


def test_user_update_name_with_empty_string_raises_error() -> None:
	"""Should raise ValueError when updating name with empty string."""
	email = Email("john@example.com")
	user = User(name="John Doe", email=email)

	with pytest.raises(ValueError, match="Name cannot be empty"):
		user.update_name("")


def test_user_update_name_with_whitespace_only_raises_error() -> None:
	"""Should raise ValueError when updating name with whitespace only."""
	email = Email("john@example.com")
	user = User(name="John Doe", email=email)

	with pytest.raises(ValueError, match="Name cannot be empty"):
		user.update_name("   ")


def test_create_user_with_empty_name_raises_error() -> None:
	"""Should raise ValueError when creating user with empty name."""
	email = Email("john@example.com")

	with pytest.raises(ValueError, match="Name cannot be empty"):
		User(name="", email=email)


def test_create_user_with_whitespace_name_raises_error() -> None:
	"""Should raise ValueError when creating user with whitespace name."""
	email = Email("john@example.com")

	with pytest.raises(ValueError, match="Name cannot be empty"):
		User(name="   ", email=email)


def test_user_str_representation() -> None:
	"""Should return string representation of user."""
	email = Email("john@example.com")
	user = User(id=1, name="John Doe", email=email)

	assert str(user) == "User(id=1, name='John Doe', email='john@example.com')"


def test_user_str_representation_without_id() -> None:
	"""Should return string representation of user without id."""
	email = Email("john@example.com")
	user = User(name="John Doe", email=email)

	assert str(user) == "User(id=None, name='John Doe', email='john@example.com')"
