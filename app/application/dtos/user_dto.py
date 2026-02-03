"""User Data Transfer Objects for application layer."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateUserDTO:
	"""DTO for creating a new user."""

	name: str
	email: str


@dataclass
class UpdateUserDTO:
	"""DTO for updating an existing user."""

	name: str | None = None
	email: str | None = None
	is_active: bool | None = None


@dataclass
class UserDTO:
	"""DTO for user data transfer."""

	id: int
	name: str
	email: str
	is_active: bool
	created_at: datetime
	updated_at: datetime | None = None
