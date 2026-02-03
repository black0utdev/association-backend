# 🚀 Quick Start Guide

Get your Association Backend up and running in 5 minutes!

## Prerequisites Check

```bash
# Verify you have the required tools
python3 --version  # Should be 3.12+
docker --version   # Should be 20.10+
docker-compose --version  # Should be 2.0+
```

## Step 1: Clone & Configure (2 minutes)

```bash
# If not already in the repo
cd association-backend

# Create environment file
cp .env.example .env

# Generate secure secrets and update .env
echo "SECRET_KEY=$(openssl rand -hex 32)"
echo "AUTHELIA_JWT_SECRET=$(openssl rand -hex 32)"
echo "AUTHELIA_SESSION_SECRET=$(openssl rand -hex 32)"
echo "OAUTH2_CLIENT_SECRET=$(openssl rand -hex 32)"

# Edit .env with a text editor and paste the generated secrets
# On macOS: open -e .env
# On Linux: nano .env
```

## Step 2: Start Services (1 minute)

```bash
# Start all services (PostgreSQL, Authelia, FastAPI)
docker-compose up -d

# Watch the logs (optional)
docker-compose logs -f api
```

## Step 3: Verify Installation (30 seconds)

```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected output:
# {"status":"healthy","version":"0.1.0","environment":"development"}

# Open API documentation in browser
# macOS: open http://localhost:8000/docs
# Linux: xdg-open http://localhost:8000/docs
# Windows: start http://localhost:8000/docs
```

## Step 4: Run Tests (30 seconds)

```bash
# Run the test suite
docker-compose exec api pytest

# Run with coverage
docker-compose exec api pytest --cov=app --cov-report=term
```

## Step 5: Start Developing! (1 minute)

```bash
# Option A: Develop inside Docker (recommended)
docker-compose exec api /bin/bash
# Now you're inside the container, can run pytest, uvicorn, etc.

# Option B: Develop locally with hot reload
python3.12 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📍 Important URLs

| Service          | URL                                | Description                   |
| ---------------- | ---------------------------------- | ----------------------------- |
| **API**          | http://localhost:8000              | Main API endpoint             |
| **Health Check** | http://localhost:8000/health       | Service health status         |
| **Swagger Docs** | http://localhost:8000/docs         | Interactive API documentation |
| **ReDoc**        | http://localhost:8000/redoc        | Alternative API documentation |
| **OpenAPI JSON** | http://localhost:8000/openapi.json | OpenAPI specification         |
| **Authelia**     | http://localhost:9091              | OAuth2 authentication service |

## 🧪 Common Commands

```bash
# Stop services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v

# Restart a single service
docker-compose restart api

# View logs for specific service
docker-compose logs -f postgres
docker-compose logs -f authelia
docker-compose logs -f api

# Run tests
docker-compose exec api pytest

# Run single test file
docker-compose exec api pytest tests/unit/domain/test_email_value_object.py

# Format code
docker-compose exec api ruff format .

# Lint code
docker-compose exec api ruff check .

# Type check
docker-compose exec api mypy app/

# Database migration
docker-compose exec api alembic upgrade head
```

## 🔍 Troubleshooting

### Port Already in Use

```bash
# Check what's using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process or change port in docker-compose.yml
# Change APP_PORT=8001 in .env
```

### Database Connection Error

```bash
# Check if PostgreSQL is running
docker-compose ps postgres

# Check PostgreSQL logs
docker-compose logs postgres

# Restart PostgreSQL
docker-compose restart postgres
```

### Dependencies Import Errors

```bash
# Rebuild the Docker image
docker-compose build --no-cache api

# Or install dependencies locally
pip install -r requirements.txt
```

### Tests Failing

```bash
# Check test database is running
docker-compose ps postgres

# Run tests with verbose output
docker-compose exec api pytest -v -s

# Run single failing test
docker-compose exec api pytest tests/path/to/test_file.py::test_function_name -v
```

## 📚 Next Steps

1. **Read the Documentation**
   - [AGENTS.md](AGENTS.md) - AI coding agent guidelines
   - [README.md](README.md) - Full project documentation
   - [DOCKER_SETUP.md](DOCKER_SETUP.md) - Docker operations guide

2. **Explore the Code**
   - Check out `app/main.py` - FastAPI entry point
   - Review `app/domain/` - Domain-driven design structure
   - Look at `tests/` - Test examples

3. **Make Your First Feature**
   - Write a test in `tests/unit/`
   - Implement the feature following TDD
   - Run `pytest` to verify
   - Commit with conventional format: `feat(scope): description`

4. **Configure GitHub Secrets** (for CI/CD)
   - Go to GitHub repository settings
   - Add secrets for deployment:
     - `DEPLOY_HOST`
     - `DEPLOY_USER`
     - `DEPLOY_SSH_KEY`

## 🆘 Getting Help

- **Issue?** Check [DOCKER_SETUP.md](DOCKER_SETUP.md) troubleshooting section
- **Question?** Read [README.md](README.md) or [AGENTS.md](AGENTS.md)
- **Bug?** Open an issue on GitHub with the bug report template
- **Feature idea?** Open an issue with the feature request template

---

**Happy coding! 🎉**
