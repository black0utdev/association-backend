"""User API endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/users", summary="List all users")
async def list_users() -> dict[str, str]:
	"""List all users - placeholder endpoint."""
	return {"message": "User list endpoint - to be implemented"}


@router.get("/users/{user_id}", summary="Get user by ID")
async def get_user(user_id: int) -> dict[str, int]:
	"""Get user by ID - placeholder endpoint."""
	return {"message": "Get user endpoint - to be implemented", "user_id": user_id}
