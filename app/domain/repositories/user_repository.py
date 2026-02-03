"""User repository interface."""

from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import User


class UserRepository(ABC):
	"""User repository interface defining data access operations."""

	@abstractmethod
	async def get_by_id(self, user_id: int) -> Optional[User]:
		"""Get user by ID.

		Args:
			user_id: User identifier

		Returns:
			User entity if found, None otherwise
		"""
		pass

	@abstractmethod
	async def get_by_email(self, email: str) -> Optional[User]:
		"""Get user by email address.

		Args:
			email: Email address

		Returns:
			User entity if found, None otherwise
		"""
		pass

	@abstractmethod
	async def list_all(self, skip: int = 0, limit: int = 100) -> List[User]:
		"""List all users with pagination.

		Args:
			skip: Number of records to skip
			limit: Maximum number of records to return

		Returns:
			List of user entities
		"""
		pass

	@abstractmethod
	async def save(self, user: User) -> User:
		"""Save user (create or update).

		Args:
			user: User entity to save

		Returns:
			Saved user entity with ID assigned
		"""
		pass

	@abstractmethod
	async def delete(self, user_id: int) -> bool:
		"""Delete user by ID.

		Args:
			user_id: User identifier

		Returns:
			True if user was deleted, False if not found
		"""
		pass

	@abstractmethod
	async def exists_by_email(self, email: str) -> bool:
		"""Check if user exists by email.

		Args:
			email: Email address

		Returns:
			True if user exists, False otherwise
		"""
		pass
