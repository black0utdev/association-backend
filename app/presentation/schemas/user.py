"""Pydantic schemas for User API requests and responses."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.domain.entities.user import User


class UserBase(BaseModel):
	"""Base user schema with common fields."""

	name: str = Field(..., min_length=1, max_length=255, description="User's full name")
	email: EmailStr = Field(..., description="User's email address")


class UserCreate(UserBase):
	"""Schema for creating a new user."""


class UserUpdate(BaseModel):
	"""Schema for updating an existing user."""

	name: str | None = Field(None, min_length=1, max_length=255, description="User's full name")
	email: EmailStr | None = Field(None, description="User's email address")
	is_active: bool | None = Field(None, description="User's active status")


class UserResponse(UserBase):
	"""Schema for user response."""

	model_config = ConfigDict(from_attributes=True)

	id: int = Field(..., description="User's unique identifier")
	is_active: bool = Field(..., description="User's active status")
	created_at: datetime = Field(..., description="User creation timestamp")
	updated_at: datetime | None = Field(None, description="User last update timestamp")

	@classmethod
	def from_entity(cls, user: User) -> "UserResponse":
		"""Create UserResponse from domain entity.

		Args:
		        user: User domain entity

		Returns:
		        UserResponse instance
		"""
		return cls(
			id=user.id,  # type: ignore
			name=user.name,
			email=user.email.value,
			is_active=user.is_active,
			created_at=user.created_at,  # type: ignore
			updated_at=user.updated_at,
		)


class UserListResponse(BaseModel):
	"""Schema for paginated user list response."""

	users: list[UserResponse] = Field(..., description="List of users")
	total: int = Field(..., description="Total number of users")
	skip: int = Field(..., description="Number of skipped records")
	limit: int = Field(..., description="Maximum number of records returned")
