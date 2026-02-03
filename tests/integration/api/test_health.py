"""Tests for health check endpoint."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check_returns_200(client: AsyncClient) -> None:
	"""Should return 200 OK with health status."""
	response = await client.get("/health")

	assert response.status_code == 200
	data = response.json()
	assert data["status"] == "healthy"
	assert "version" in data
	assert "environment" in data
