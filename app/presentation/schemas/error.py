"""Error response schemas."""

from typing import Any

from pydantic import BaseModel, ConfigDict


class ErrorResponse(BaseModel):
	"""Standard error response format."""

	model_config = ConfigDict(
		json_schema_extra={
			"example": {
				"error": "not_found",
				"message": "Resource not found",
				"details": {"resource_id": 123},
			}
		}
	)

	error: str
	message: str
	details: dict[str, Any] | None = None
