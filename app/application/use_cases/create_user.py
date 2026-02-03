"""Create user use case."""

from app.application.dtos.user_dto import CreateUserDTO, UserDTO
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.domain.value_objects.email import Email


class CreateUserUseCase:
	"""Use case for creating a new user."""

	def __init__(self, user_repository: UserRepository) -> None:
		"""Initialize use case with repository.

		Args:
		        user_repository: User repository instance
		"""
		self.user_repository = user_repository

	async def execute(self, data: CreateUserDTO) -> UserDTO:
		"""Execute the create user use case.

		Args:
		        data: User creation data

		Returns:
		        Created user DTO

		Raises:
		        ValueError: If email already exists or validation fails
		"""
		# Create email value object (validates format first)  # noqa: ERA001
		email = Email(data.email)

		# Create user entity (validates name)  # noqa: ERA001
		user = User(name=data.name, email=email)

		# Check if user with email already exists
		if await self.user_repository.exists_by_email(data.email):
			raise ValueError(f"User with email {data.email} already exists")

		# Save user
		saved_user = await self.user_repository.save(user)

		# Convert to DTO
		return UserDTO(
			id=saved_user.id,  # type: ignore
			name=saved_user.name,
			email=saved_user.email.value,
			is_active=saved_user.is_active,
			created_at=saved_user.created_at,  # type: ignore
			updated_at=saved_user.updated_at,
		)
