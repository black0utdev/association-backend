"""User repository interface."""

from abc import ABC, abstractmethod

from app.domain.entities.user import User


class UserRepository(ABC):
	"""User repository interface defining data access operations."""

	@abstractmethod
	async def get_by_id(self, user_id: int) -> User | None:
		"""Get user by ID.

		Args:
		        user_id: User identifier

		Returns:
		        User entity if found, None otherwise
		"""

	@abstractmethod
	async def get_by_email(self, email: str) -> User | None:
		"""Get user by email address.

		Args:
		        email: Email address

		Returns:
		        User entity if found, None otherwise
		"""

	@abstractmethod
	async def list_all(self, skip: int = 0, limit: int = 100) -> list[User]:
		"""List all users with pagination.

		Args:
		        skip: Number of records to skip
		        limit: Maximum number of records to return

		Returns:
		        List of user entities
		"""

	@abstractmethod
	async def save(self, user: User) -> User:
		"""Save user (create or update).

		Args:
		        user: User entity to save

		Returns:
		        Saved user entity with ID assigned
		"""

	@abstractmethod
	async def delete(self, user_id: int) -> bool:
		"""Delete user by ID.

		Args:
		        user_id: User identifier

		Returns:
		        True if user was deleted, False if not found
		"""

	@abstractmethod
	async def exists_by_email(self, email: str) -> bool:
		"""Check if user exists by email.

		Args:
		        email: Email address

		Returns:
		        True if user exists, False otherwise
		"""
