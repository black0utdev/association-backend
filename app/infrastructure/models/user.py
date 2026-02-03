"""SQLAlchemy User model."""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.infrastructure.database import Base


class UserModel(Base):
	"""SQLAlchemy User model for database persistence."""

	__tablename__ = "users"

	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	name: Mapped[str] = mapped_column(String(255), nullable=False)
	email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
	is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True),
		server_default=func.now(),
		nullable=False,
	)
	updated_at: Mapped[Optional[datetime]] = mapped_column(
		DateTime(timezone=True),
		onupdate=func.now(),
		nullable=True,
	)

	def __repr__(self) -> str:
		"""String representation of UserModel."""
		return f"<UserModel(id={self.id}, name='{self.name}', email='{self.email}')>"
