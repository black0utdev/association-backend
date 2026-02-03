"""User Data Transfer Objects for application layer."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CreateUserDTO:
	"""DTO for creating a new user."""

	name: str
	email: str


@dataclass
class UpdateUserDTO:
	"""DTO for updating an existing user."""

	name: Optional[str] = None
	email: Optional[str] = None
	is_active: Optional[bool] = None


@dataclass
class UserDTO:
	"""DTO for user data transfer."""

	id: int
	name: str
	email: str
	is_active: bool
	created_at: datetime
	updated_at: Optional[datetime] = None
