"""Unit tests for CreateUser use case."""

from unittest.mock import AsyncMock

import pytest

from app.application.dtos.user_dto import CreateUserDTO
from app.application.use_cases.create_user import CreateUserUseCase
from app.domain.entities.user import User
from app.domain.value_objects.email import Email


@pytest.mark.asyncio()
async def test_create_user_success() -> None:
	"""Should create user successfully."""
	# Arrange
	mock_repository = AsyncMock()
	mock_repository.exists_by_email.return_value = False

	created_user = User(
		id=1,
		name="John Doe",
		email=Email("john@example.com"),
	)
	mock_repository.save.return_value = created_user

	use_case = CreateUserUseCase(mock_repository)
	dto = CreateUserDTO(name="John Doe", email="john@example.com")

	# Act
	result = await use_case.execute(dto)

	# Assert
	assert result.id == 1
	assert result.name == "John Doe"
	assert result.email == "john@example.com"
	mock_repository.exists_by_email.assert_called_once_with("john@example.com")
	mock_repository.save.assert_called_once()


@pytest.mark.asyncio()
async def test_create_user_with_existing_email_raises_error() -> None:
	"""Should raise error when email already exists."""
	# Arrange
	mock_repository = AsyncMock()
	mock_repository.exists_by_email.return_value = True

	use_case = CreateUserUseCase(mock_repository)
	dto = CreateUserDTO(name="John Doe", email="john@example.com")

	# Act & Assert
	with pytest.raises(ValueError, match="User with email john@example.com already exists"):
		await use_case.execute(dto)

	mock_repository.exists_by_email.assert_called_once_with("john@example.com")
	mock_repository.save.assert_not_called()


@pytest.mark.asyncio()
async def test_create_user_with_invalid_email_raises_error() -> None:
	"""Should raise error when email is invalid."""
	# Arrange
	mock_repository = AsyncMock()
	mock_repository.exists_by_email.return_value = False
	use_case = CreateUserUseCase(mock_repository)
	dto = CreateUserDTO(name="John Doe", email="invalid-email")

	# Act & Assert
	with pytest.raises(ValueError, match="Invalid email format"):
		await use_case.execute(dto)

	mock_repository.exists_by_email.assert_not_called()
	mock_repository.save.assert_not_called()


@pytest.mark.asyncio()
async def test_create_user_with_empty_name_raises_error() -> None:
	"""Should raise error when name is empty."""
	# Arrange
	mock_repository = AsyncMock()
	mock_repository.exists_by_email.return_value = False
	use_case = CreateUserUseCase(mock_repository)
	dto = CreateUserDTO(name="", email="john@example.com")

	# Act & Assert
	with pytest.raises(ValueError, match="Name cannot be empty"):
		await use_case.execute(dto)

	mock_repository.exists_by_email.assert_not_called()
	mock_repository.save.assert_not_called()
