# Association Backend

> **A modern, production-ready FastAPI backend for registered association management tools.**

[![CI](https://github.com/yourusername/association-backend/workflows/CI/badge.svg)](https://github.com/yourusername/association-backend/actions)
[![codecov](https://codecov.io/gh/yourusername/association-backend/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/association-backend)
[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

## 📚 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Setup (5 Minutes)](#quick-setup-5-minutes)
  - [Detailed Setup](#detailed-setup)
- [Verifying Your Setup](#-verifying-your-setup)
- [Development Workflow](#-development-workflow)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Code Quality](#-code-quality)
- [Docker Commands](#-docker-commands)
- [Troubleshooting](#-troubleshooting)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Features

- ⚡ **FastAPI** - Modern, fast async Python framework
- 🐘 **PostgreSQL 16** - Robust relational database with async support
- 🔐 **OAuth2 Authentication** - Secure authentication via Authelia
- 🏗️ **Domain-Driven Design** - Clean architecture with clear layer separation
- 🧪 **Test-Driven Development** - Comprehensive test suite with >80% coverage
- 🐳 **Docker-First** - Production-ready containerized deployment
- 🔄 **Auto-Versioning** - Semantic releases with automated changelogs
- 🤖 **Dependency Management** - Automated updates via Renovate
- 📖 **OpenAPI Documentation** - Auto-generated interactive API docs
- 🐚 **Hermit Environment** - Reproducible development setup

---

## 🛠️ Technology Stack

| Component          | Technology       | Version      |
| ------------------ | ---------------- | ------------ |
| **Framework**      | FastAPI          | Latest       |
| **Language**       | Python           | 3.12+        |
| **Database**       | PostgreSQL       | 16 Alpine    |
| **ORM**            | SQLAlchemy       | 2.0+ (async) |
| **Authentication** | Authelia         | Latest       |
| **Testing**        | pytest           | Latest       |
| **Code Quality**   | Ruff + mypy      | Latest       |
| **Containers**     | Docker + Compose | Latest       |
| **CI/CD**          | GitHub Actions   | -            |
| **Environment**    | Hermit           | Latest       |

---

## 🎯 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Git** (for cloning the repository)
- **Docker & Docker Compose** (for running services)
- **Python 3.12+** (optional if using Hermit)

**That's it!** Hermit will handle the rest.

### Quick Setup (5 Minutes)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/association-backend.git
cd association-backend

# 2️⃣ Install Hermit (one-time, for reproducible environment)
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash

# 3️⃣ Activate Hermit environment (already initialized)
source bin/activate-hermit

# 4️⃣ Set up environment variables
cp .env.example .env

# Generate secure secrets
openssl rand -hex 32  # Copy this for SECRET_KEY
openssl rand -hex 32  # Copy this for AUTHELIA_JWT_SECRET
openssl rand -hex 32  # Copy this for AUTHELIA_SESSION_SECRET
openssl rand -hex 32  # Copy this for OAUTH2_CLIENT_SECRET

# Edit .env with your favorite editor
nano .env  # or vim, code, etc.

# 5️⃣ Install Python dependencies
pip install -r requirements.txt

# 6️⃣ Start all services (PostgreSQL, Authelia, FastAPI)
docker-compose up -d

# 7️⃣ Verify everything is running
curl http://localhost:8000/health

# 🎉 You're ready to develop!
```

### Detailed Setup

#### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/association-backend.git
cd association-backend
```

#### Step 2: Choose Your Environment Setup

You have **two options** for setting up your development environment:

##### Option A: Hermit (Recommended - Reproducible)

Hermit ensures everyone has the same Python version and tools.

```bash
# Install Hermit (one-time)
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash

# Activate the environment (Hermit is already initialized in this project)
source bin/activate-hermit

# Verify Python and pip are available
python --version  # Should show Python 3.12.3
pip --version     # Should show pip 24.0

# (Optional) Enable automatic activation
echo 'eval "$(hermit hook zsh)"' >> ~/.zshrc
source ~/.zshrc
```

**Benefits:**

- ✅ Python 3.12 + pip automatically available
- ✅ Same versions for entire team
- ✅ No conflicts with system Python
- ✅ Version-controlled tool versions
- ✅ No need to run `hermit init` - already configured!

##### Option B: Traditional venv (Alternative)

If you prefer traditional Python virtual environments:

```bash
# Create virtual environment
python3.12 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

#### Step 3: Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Generate secure secrets
echo "SECRET_KEY=$(openssl rand -hex 32)"
echo "AUTHELIA_JWT_SECRET=$(openssl rand -hex 32)"
echo "AUTHELIA_SESSION_SECRET=$(openssl rand -hex 32)"
echo "OAUTH2_CLIENT_SECRET=$(openssl rand -hex 32)"
echo "POSTGRES_PASSWORD=$(openssl rand -hex 16)"
```

**Edit `.env` and replace the placeholder values:**

```bash
# Open with your favorite editor
nano .env      # or vim, code, etc.
```

**Required changes:**

- `SECRET_KEY` - Use generated value
- `AUTHELIA_JWT_SECRET` - Use generated value
- `AUTHELIA_SESSION_SECRET` - Use generated value
- `OAUTH2_CLIENT_SECRET` - Use generated value
- `POSTGRES_PASSWORD` - Use generated value

#### Step 4: Install Dependencies

```bash
# Ensure you're in the activated environment (Hermit or venv)
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python --version    # Should show Python 3.12.x
pytest --version    # Should show pytest
ruff --version      # Should show ruff
```

#### Step 5: Start Services with Docker

```bash
# Start all services (PostgreSQL, Authelia, FastAPI)
docker-compose up -d

# View logs (optional)
docker-compose logs -f api

# Check service status
docker-compose ps
```

**Services started:**

- 🐘 PostgreSQL 16 - Database (port 5432)
- 🔐 Authelia - OAuth2 authentication (port 9091)
- ⚡ FastAPI - API server (port 8000)

#### Step 6: Initialize Database (First Time Only)

```bash
# Run database migrations
docker-compose exec api alembic upgrade head
```

---

## ✅ Verifying Your Setup

Run these commands to ensure everything is working correctly:

### 1. Check Services Are Running

```bash
# All services should show "Up" status
docker-compose ps
```

**Expected output:**

```
NAME                    STATUS      PORTS
association-app         Up          0.0.0.0:8000->8000/tcp
association-postgres    Up          0.0.0.0:5432->5432/tcp
association-authelia    Up          0.0.0.0:9091->9091/tcp
```

### 2. Test Health Endpoint

```bash
# Should return: {"status":"healthy","version":"0.1.0","environment":"development"}
curl http://localhost:8000/health
```

### 3. Open API Documentation

```bash
# macOS
open http://localhost:8000/docs

# Linux
xdg-open http://localhost:8000/docs

# Windows
start http://localhost:8000/docs
```

**You should see:**

- Swagger UI with interactive API documentation
- Health check endpoint listed
- OpenAPI schema available

### 4. Run Tests

```bash
# Run all tests
docker-compose exec api pytest

# Run with verbose output
docker-compose exec api pytest -v

# Run with coverage report
docker-compose exec api pytest --cov=app --cov-report=term
```

**Expected output:**

```
========================= test session starts =========================
collected 3 items

tests/integration/api/test_health.py .                          [ 33%]
tests/unit/domain/test_email_value_object.py ......             [100%]

========================= 3 passed in 0.45s ==========================
```

### 5. Test Code Quality Tools

```bash
# Lint check (should pass with no errors)
docker-compose exec api ruff check .

# Format check
docker-compose exec api ruff format --check .

# Type check
docker-compose exec api mypy app/
```

### 6. Test Database Connection

```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U association_user -d association_db

# Inside psql, run:
\dt  # List tables
\q   # Quit
```

### 7. Full Integration Test

```bash
# Run this comprehensive test script
cat << 'EOF' > test_setup.sh
#!/bin/bash
echo "🧪 Running setup verification tests..."
echo ""

# Test 1: Health endpoint
echo "1️⃣ Testing health endpoint..."
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "✅ Health endpoint working"
else
    echo "❌ Health endpoint failed"
    exit 1
fi

# Test 2: Run pytest
echo "2️⃣ Running tests..."
if docker-compose exec -T api pytest -q; then
    echo "✅ All tests passed"
else
    echo "❌ Tests failed"
    exit 1
fi

# Test 3: Lint check
echo "3️⃣ Checking code quality..."
if docker-compose exec -T api ruff check . > /dev/null 2>&1; then
    echo "✅ Code quality checks passed"
else
    echo "❌ Code quality checks failed"
    exit 1
fi

# Test 4: Database connection
echo "4️⃣ Testing database connection..."
if docker-compose exec -T postgres pg_isready -U association_user > /dev/null 2>&1; then
    echo "✅ Database connection working"
else
    echo "❌ Database connection failed"
    exit 1
fi

echo ""
echo "🎉 All verification tests passed! Your setup is ready."
EOF

chmod +x test_setup.sh
./test_setup.sh
```

**Expected final output:**

```
🎉 All verification tests passed! Your setup is ready.
```

---

## 💻 Development Workflow

### Daily Workflow

```bash
# 1. Navigate to project
cd association-backend

# 2. Activate Hermit (if not auto-activated)
source bin/activate-hermit

# 3. Start services (if not running)
docker-compose up -d

# 4. Watch logs (optional)
docker-compose logs -f api

# 5. Run development server with hot reload
uvicorn app.main:app --reload
# Or use Docker: docker-compose up

# 6. Make your changes...

# 7. Run tests frequently (TDD!)
pytest

# 8. Check code quality before committing
ruff check .
ruff format .
mypy app/
pytest --cov=app
```

### Making Changes

1. **Write tests first** (TDD approach):

   ```bash
   # Create a test file
   touch tests/unit/domain/test_my_feature.py

   # Write failing test
   pytest tests/unit/domain/test_my_feature.py  # Should fail
   ```

2. **Implement the feature**:

   ```python
   # Write code in app/
   ```

3. **Run tests until they pass**:

   ```bash
   pytest tests/unit/domain/test_my_feature.py  # Should pass
   ```

4. **Check code quality**:

   ```bash
   ruff check .
   ruff format .
   mypy app/
   ```

5. **Commit with conventional format**:
   ```bash
   git add .
   git commit -m "feat(domain): add my amazing feature"
   ```

### Adding Dependencies

```bash
# 1. Add to requirements.txt
echo "httpx==0.26.0" >> requirements.txt

# 2. Install
pip install -r requirements.txt

# 3. Rebuild Docker image
docker-compose build api
docker-compose up -d
```

---

## 📁 Project Structure

```
association-backend/
├── 📋 Documentation
│   ├── README.md              ← You are here!
│   ├── AGENTS.md              → AI coding guidelines
│   ├── QUICKSTART.md          → 5-minute quick start
│   ├── HERMIT.md              → Hermit environment guide
│   ├── RENOVATE.md            → Dependency management
│   └── DOCKER_SETUP.md        → Docker operations guide
│
├── 🐍 Application Code
│   └── app/
│       ├── main.py            → FastAPI entry point
│       ├── config.py          → Configuration management
│       ├── dependencies.py    → Dependency injection
│       │
│       ├── domain/            → Business logic (entities, value objects)
│       ├── application/       → Use cases and DTOs
│       ├── infrastructure/    → Database and external services
│       └── presentation/      → API routes and schemas
│
├── 🧪 Tests
│   └── tests/
│       ├── unit/              → Fast, isolated tests
│       ├── integration/       → API and database tests
│       └── conftest.py        → Pytest fixtures
│
├── 🐳 Docker
│   ├── Dockerfile             → Multi-stage production image
│   ├── docker-compose.yml     → Service orchestration
│   ├── .dockerignore          → Build optimization
│   └── .env.example           → Environment template
│
├── 🗄️ Database
│   └── migrations/
│       ├── env.py             → Alembic configuration
│       └── versions/          → Migration files
│
├── 🔧 Configuration
│   ├── pyproject.toml         → Python project config
│   ├── requirements.txt       → Dependencies
│   ├── renovate.json          → Dependency automation
│   └── .releaserc.json        → Semantic release config
│
├── 🐚 Hermit
│   ├── bin/                   → Hermit environment
│   ├── .hermit.env            → Environment variables
│   └── .envrc                 → direnv integration
│
└── 🚀 CI/CD
    └── .github/workflows/
        ├── ci.yml             → Continuous integration
        ├── release.yml        → Automated releases
        ├── renovate.yml       → Dependency updates
        └── dependency-review.yml → Security review
```

---

## 🧪 Testing

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/unit/domain/test_email_value_object.py

# Specific test function
pytest tests/unit/domain/test_email_value_object.py::test_create_email_with_valid_format

# With verbose output
pytest -v

# With output from print statements
pytest -s

# Unit tests only
pytest tests/unit

# Integration tests only
pytest tests/integration

# With coverage report
pytest --cov=app --cov-report=html
open htmlcov/index.html  # View coverage report
```

### Test Coverage

```bash
# Run tests with coverage
pytest --cov=app --cov-report=term --cov-report=html

# View coverage report
open htmlcov/index.html

# Coverage must be >80% (enforced by CI)
pytest --cov=app --cov-fail-under=80
```

### Writing Tests

Tests follow the **AAA pattern** (Arrange, Act, Assert):

```python
# tests/unit/domain/test_email_value_object.py
import pytest
from app.domain.value_objects.email import Email

def test_create_email_with_valid_format() -> None:
    """Should create Email with valid format."""
    # Arrange
    email_string = "user@example.com"

    # Act
    email = Email(email_string)

    # Assert
    assert email.value == email_string
```

---

## 🎨 Code Quality

### Linting and Formatting

```bash
# Check for linting issues
ruff check .

# Auto-fix linting issues
ruff check --fix .

# Format code
ruff format .

# Check formatting (without changing files)
ruff format --check .
```

### Type Checking

```bash
# Run mypy type checker
mypy app/

# Strict mode (recommended)
mypy --strict app/
```

### Run All Quality Checks

```bash
# One command to rule them all
ruff check . && ruff format . && mypy app/ && pytest --cov=app --cov-fail-under=80

# Or create an alias in your shell
alias qa='ruff check . && ruff format . && mypy app/ && pytest --cov=app --cov-fail-under=80'
qa  # Run all checks
```

---

## 🐳 Docker Commands

### Starting and Stopping

```bash
# Start all services
docker-compose up -d

# Start specific service
docker-compose up -d postgres

# Stop all services
docker-compose down

# Stop and remove volumes (fresh start)
docker-compose down -v

# Restart a service
docker-compose restart api
```

### Viewing Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f api
docker-compose logs -f postgres
docker-compose logs -f authelia

# Last 100 lines
docker-compose logs --tail=100 api
```

### Accessing Containers

```bash
# Open shell in API container
docker-compose exec api /bin/bash

# Run Python commands
docker-compose exec api python

# Access PostgreSQL
docker-compose exec postgres psql -U association_user -d association_db

# Run tests in container
docker-compose exec api pytest
```

### Rebuilding

```bash
# Rebuild images
docker-compose build

# Rebuild specific service
docker-compose build api

# Rebuild without cache
docker-compose build --no-cache

# Rebuild and restart
docker-compose up -d --build
```

---

## 🐛 Troubleshooting

### Services Won't Start

**Problem:** Docker containers fail to start

```bash
# Check service status
docker-compose ps

# View logs for errors
docker-compose logs

# Common fix: Remove volumes and restart
docker-compose down -v
docker-compose up -d
```

### Port Already in Use

**Problem:** `Error: port is already allocated`

```bash
# Check what's using the port
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process or change port in docker-compose.yml
```

### Database Connection Errors

**Problem:** `could not connect to server`

```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Check PostgreSQL logs
docker-compose logs postgres

# Restart PostgreSQL
docker-compose restart postgres

# Wait for it to be healthy
docker-compose ps  # Wait for "healthy" status
```

### Import Errors in Tests

**Problem:** `ModuleNotFoundError: No module named 'app'`

```bash
# Ensure you're in project root
pwd  # Should show .../association-backend

# Install dependencies
pip install -r requirements.txt

# Set PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Hermit Not Working

**Problem:** `hermit: command not found`

```bash
# Ensure Hermit is installed
hermit version

# If not installed
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash

# Ensure it's in PATH
export PATH="$HOME/bin:$PATH"

# Activate environment
source bin/activate-hermit
```

### Tests Failing

**Problem:** Tests fail unexpectedly

```bash
# Clear pytest cache
rm -rf .pytest_cache

# Recreate database
docker-compose down -v
docker-compose up -d
docker-compose exec api alembic upgrade head

# Run tests with verbose output
pytest -v -s
```

### Docker Build Fails

**Problem:** `ERROR: failed to solve`

```bash
# Clean Docker cache
docker system prune -a --volumes

# Rebuild from scratch
docker-compose build --no-cache
docker-compose up -d
```

---

## 📖 Documentation

### Project Documentation

| File                | Description                               |
| ------------------- | ----------------------------------------- |
| **README.md**       | This file - Getting started guide         |
| **AGENTS.md**       | AI coding guidelines (TDD, DDD, commands) |
| **QUICKSTART.md**   | 5-minute quick start guide                |
| **HERMIT.md**       | Hermit environment management guide       |
| **RENOVATE.md**     | Dependency management with Renovate       |
| **DOCKER_SETUP.md** | Docker operations and troubleshooting     |

### API Documentation

Once services are running:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### External Resources

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org/
- **Hermit Docs**: https://cashapp.github.io/hermit/
- **Renovate Docs**: https://docs.renovatebot.com/
- **Authelia Docs**: https://www.authelia.com/

---

## 🤝 Contributing

We follow **Test-Driven Development (TDD)** and **Conventional Commits**.

### Development Process

1. **Create a feature branch**

   ```bash
   git checkout -b feat/my-amazing-feature
   ```

2. **Write tests first (TDD)**

   ```bash
   # Create test file
   touch tests/unit/domain/test_my_feature.py

   # Write failing test
   pytest tests/unit/domain/test_my_feature.py  # Should fail
   ```

3. **Implement the feature**

   ```python
   # Write code to make test pass
   ```

4. **Ensure all checks pass**

   ```bash
   ruff check . && ruff format . && mypy app/ && pytest --cov=app --cov-fail-under=80
   ```

5. **Commit with conventional format**

   ```bash
   git commit -m "feat(domain): add amazing feature"
   ```

6. **Push and create PR**
   ```bash
   git push origin feat/my-amazing-feature
   ```

### Commit Message Format

```
type(scope): description

feat(users): add user registration endpoint
fix(auth): resolve token validation issue
docs(readme): update installation instructions
refactor(db): optimize query performance
test(api): add integration tests
chore(deps): update FastAPI to v0.110.0
```

### Versioning

This project uses **Semantic Versioning** with automated releases:

- **feat:** → Minor version (0.1.0 → 0.2.0)
- **fix/refactor:** → Patch version (0.1.0 → 0.1.1)
- **BREAKING CHANGE:** → Major version (0.1.0 → 1.0.0)

---

## 📝 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

---

## 🎉 You're Ready to Develop!

Your development environment is now set up. Here's a quick recap:

```bash
# Daily workflow
cd association-backend
source bin/activate-hermit        # Activate Hermit
docker-compose up -d              # Start services
pytest                            # Run tests
uvicorn app.main:app --reload    # Start dev server
```

**Happy coding! 🚀**

For questions or issues, please open a GitHub issue or refer to the documentation files listed above.

---

**Made with ❤️ using FastAPI, PostgreSQL, and Domain-Driven Design**
