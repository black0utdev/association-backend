"""User domain entity."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.domain.value_objects.email import Email


@dataclass
class User:
	"""User domain entity representing a registered association member."""

	name: str
	email: Email
	id: Optional[int] = None
	is_active: bool = True
	created_at: Optional[datetime] = None
	updated_at: Optional[datetime] = None

	def __post_init__(self) -> None:
		"""Validate user data after initialization."""
		if not self.name or not self.name.strip():
			raise ValueError("Name cannot be empty")

	def change_email(self, new_email: Email) -> None:
		"""Change user email address.

		Args:
			new_email: New email address

		Raises:
			ValueError: If email is invalid (handled by Email value object)
		"""
		self.email = new_email

	def activate(self) -> None:
		"""Activate user account."""
		self.is_active = True

	def deactivate(self) -> None:
		"""Deactivate user account."""
		self.is_active = False

	def update_name(self, new_name: str) -> None:
		"""Update user name.

		Args:
			new_name: New name for the user

		Raises:
			ValueError: If name is empty or whitespace only
		"""
		if not new_name or not new_name.strip():
			raise ValueError("Name cannot be empty")
		self.name = new_name

	def __str__(self) -> str:
		"""String representation of user."""
		return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
