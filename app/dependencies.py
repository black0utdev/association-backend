"""Dependency injection for FastAPI."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
	"""Dependency for database session."""
	async with AsyncSessionLocal() as session:
		try:
			yield session
		finally:
			await session.close()
