"""Application configuration management."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	"""Application settings loaded from environment variables."""

	model_config = SettingsConfigDict(
		env_file=".env",
		env_file_encoding="utf-8",
		case_sensitive=False,
		extra="ignore",  # Ignore extra fields from .env
	)

	# Application
	app_name: str = "Association Backend"
	app_env: str = "development"
	environment: str = "development"  # Alias for app_env
	debug: bool = True
	app_port: int = 8000

	# Database
	database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/association"
	postgres_db: str = "association"
	postgres_user: str = "postgres"
	postgres_password: str = "postgres"
	postgres_port: int = 5432

	# Security
	secret_key: str = "your-secret-key-change-in-production"
	allowed_hosts: str = "*"

	# Authelia
	authelia_url: str = "http://authelia:9091"
	authelia_port: int = 9091
	authelia_jwt_secret: str = "change-this"
	authelia_session_secret: str = "change-this"
	authelia_storage_encryption_key: str = "change-this"
	authelia_db: str = "authelia"
	oauth2_client_id: str = "association-backend"
	oauth2_client_secret: str = "change-this"
	oauth2_redirect_uri: str = "http://localhost:8000/auth/callback"

	# CORS
	cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8000"]
	allowed_origins: str = "http://localhost:3000"

	# Logging
	log_level: str = "INFO"
	log_format: str = "json"

	# Security settings
	force_https: bool = False
	session_cookie_secure: bool = False
	session_cookie_httponly: bool = True
	session_cookie_samesite: str = "lax"


settings = Settings()
