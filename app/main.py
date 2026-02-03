"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.presentation.api.v1 import users

app = FastAPI(
	title=settings.app_name,
	description="Backend API for registered association management",
	version="0.1.0",
	docs_url="/docs",
	redoc_url="/redoc",
	openapi_url="/openapi.json",
)

# CORS middleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=settings.cors_origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
	"""Health check endpoint for container orchestration."""
	return {
		"status": "healthy",
		"version": "0.1.0",
		"environment": settings.environment,
	}


# Include routers
app.include_router(users.router, prefix="/api/v1", tags=["users"])
