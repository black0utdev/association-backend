"""User repository implementation using SQLAlchemy."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.domain.value_objects.email import Email
from app.infrastructure.models.user import UserModel


class UserRepositoryImpl(UserRepository):
	"""SQLAlchemy implementation of UserRepository."""

	def __init__(self, db: AsyncSession) -> None:
		"""Initialize repository with database session.

		Args:
		        db: Async database session
		"""
		self.db = db

	async def get_by_id(self, user_id: int) -> User | None:
		"""Get user by ID."""
		result = await self.db.execute(select(UserModel).where(UserModel.id == user_id))
		model = result.scalar_one_or_none()
		return self._to_entity(model) if model else None

	async def get_by_email(self, email: str) -> User | None:
		"""Get user by email address."""
		result = await self.db.execute(select(UserModel).where(UserModel.email == email))
		model = result.scalar_one_or_none()
		return self._to_entity(model) if model else None

	async def list_all(self, skip: int = 0, limit: int = 100) -> list[User]:
		"""List all users with pagination."""
		result = await self.db.execute(select(UserModel).offset(skip).limit(limit))
		models = result.scalars().all()
		return [self._to_entity(model) for model in models]

	async def save(self, user: User) -> User:
		"""Save user (create or update)."""
		if user.id is None:
			# Create new user
			model = self._to_model(user)
			self.db.add(model)
		else:
			# Update existing user
			result = await self.db.execute(select(UserModel).where(UserModel.id == user.id))
			model = result.scalar_one_or_none()
			if model is None:
				raise ValueError(f"User with id {user.id} not found")
			self._update_model(model, user)

		await self.db.commit()
		await self.db.refresh(model)
		return self._to_entity(model)

	async def delete(self, user_id: int) -> bool:
		"""Delete user by ID."""
		result = await self.db.execute(select(UserModel).where(UserModel.id == user_id))
		model = result.scalar_one_or_none()
		if model is None:
			return False

		await self.db.delete(model)
		await self.db.commit()
		return True

	async def exists_by_email(self, email: str) -> bool:
		"""Check if user exists by email."""
		result = await self.db.execute(select(UserModel.id).where(UserModel.email == email))
		return result.scalar_one_or_none() is not None

	def _to_entity(self, model: UserModel) -> User:
		"""Convert SQLAlchemy model to domain entity.

		Args:
		        model: SQLAlchemy UserModel

		Returns:
		        User domain entity
		"""
		return User(
			id=model.id,
			name=model.name,
			email=Email(model.email),
			is_active=model.is_active,
			created_at=model.created_at,
			updated_at=model.updated_at,
		)

	def _to_model(self, entity: User) -> UserModel:
		"""Convert domain entity to SQLAlchemy model.

		Args:
		        entity: User domain entity

		Returns:
		        SQLAlchemy UserModel
		"""
		return UserModel(
			id=entity.id,
			name=entity.name,
			email=entity.email.value,
			is_active=entity.is_active,
			created_at=entity.created_at,
			updated_at=entity.updated_at,
		)

	def _update_model(self, model: UserModel, entity: User) -> None:
		"""Update SQLAlchemy model from domain entity.

		Args:
		        model: SQLAlchemy UserModel to update
		        entity: User domain entity with new data
		"""
		model.name = entity.name
		model.email = entity.email.value
		model.is_active = entity.is_active
