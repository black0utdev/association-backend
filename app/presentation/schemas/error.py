"""Error response schemas."""

from typing import Any

from pydantic import BaseModel


class ErrorResponse(BaseModel):
	"""Standard error response format."""

	error: str
	message: str
	details: dict[str, Any] | None = None

	class Config:
		"""Pydantic config."""

		json_schema_extra = {
			"example": {
				"error": "not_found",
				"message": "Resource not found",
				"details": {"resource_id": 123},
			}
		}
