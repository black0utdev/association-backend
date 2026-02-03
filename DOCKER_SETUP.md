# Docker Setup Guide

This guide explains how to use the Docker infrastructure for the FastAPI + PostgreSQL + Authelia application.

## Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- 4GB RAM minimum
- 10GB disk space

## Quick Start

### 1. Environment Setup

```bash
# Copy environment template
cp .env.example .env

# Generate secure secrets
openssl rand -hex 32  # Use for SECRET_KEY
openssl rand -hex 32  # Use for POSTGRES_PASSWORD
openssl rand -hex 32  # Use for AUTHELIA_JWT_SECRET
openssl rand -hex 32  # Use for AUTHELIA_SESSION_SECRET
openssl rand -hex 32  # Use for AUTHELIA_STORAGE_ENCRYPTION_KEY
openssl rand -hex 32  # Use for OAUTH2_CLIENT_SECRET

# Edit .env with your generated secrets
nano .env
```

### 2. Create Authelia Configuration

```bash
# Create Authelia config directory
mkdir -p config/authelia

# Create basic configuration (adjust as needed)
cat > config/authelia/configuration.yml <<EOF
---
theme: light
jwt_secret: YOUR_JWT_SECRET_HERE
default_redirection_url: http://localhost:8000

server:
  host: 0.0.0.0
  port: 9091

log:
  level: info

authentication_backend:
  file:
    path: /config/users_database.yml

access_control:
  default_policy: deny
  rules:
    - domain: localhost
      policy: one_factor

session:
  name: authelia_session
  secret: YOUR_SESSION_SECRET_HERE
  expiration: 3600
  inactivity: 300
  domain: localhost

storage:
  postgres:
    host: postgres
    port: 5432
    database: authelia
    username: postgres
    password: YOUR_POSTGRES_PASSWORD_HERE

notifier:
  filesystem:
    filename: /config/notification.txt
EOF
```

### 3. Build and Start Services

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Check service health
docker-compose ps
```

### 4. Verify Setup

```bash
# Check FastAPI health endpoint
curl http://localhost:8000/health

# Check Authelia health
curl http://localhost:9091/api/health

# Check PostgreSQL
docker-compose exec postgres psql -U postgres -d association -c "SELECT version();"
```

## Development Workflow

### Hot Reload

The application automatically reloads when code changes are detected:

```bash
# Start in development mode (default)
docker-compose up

# Edit files in ./app directory
# Changes are reflected immediately
```

### Database Migrations

```bash
# Create a new migration
docker-compose exec app alembic revision --autogenerate -m "description"

# Apply migrations
docker-compose exec app alembic upgrade head

# Rollback migration
docker-compose exec app alembic downgrade -1
```

### Access Database

```bash
# PostgreSQL CLI
docker-compose exec postgres psql -U postgres -d association

# Using external tool (DBeaver, pgAdmin)
# Host: localhost
# Port: 5432
# Database: association
# User: postgres
# Password: (from .env)
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f app
docker-compose logs -f postgres
docker-compose logs -f authelia

# Last 100 lines
docker-compose logs --tail=100 app
```

## Production Deployment

### 1. Update Environment

```bash
# Set production environment
APP_ENV=production
DEBUG=false
FORCE_HTTPS=true
SESSION_COOKIE_SECURE=true
```

### 2. Remove Development Ports

Edit `docker-compose.yml` and remove port mappings for PostgreSQL:

```yaml
# Comment out or remove
# ports:
#   - "${POSTGRES_PORT:-5432}:5432"
```

### 3. Use Production Command

The app automatically uses multiple workers in production mode:

```bash
# Production mode uses 4 workers
docker-compose up -d
```

### 4. Add Reverse Proxy

Use Nginx or Traefik as reverse proxy:

```yaml
# Example Traefik labels
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.app.rule=Host(`yourdomain.com`)"
  - "traefik.http.routers.app.entrypoints=websecure"
  - "traefik.http.routers.app.tls.certresolver=letsencrypt"
```

### 5. Backup Strategy

```bash
# Backup PostgreSQL
docker-compose exec postgres pg_dump -U postgres association > backup.sql

# Restore PostgreSQL
docker-compose exec -T postgres psql -U postgres association < backup.sql

# Backup volumes
docker run --rm -v association-postgres-data:/data -v $(pwd):/backup \
  alpine tar czf /backup/postgres-backup.tar.gz /data
```

## Troubleshooting

### Service Won't Start

```bash
# Check logs
docker-compose logs app

# Rebuild image
docker-compose build --no-cache app
docker-compose up -d
```

### Database Connection Issues

```bash
# Check PostgreSQL is healthy
docker-compose ps postgres

# Test connection
docker-compose exec app python -c "from sqlalchemy import create_engine; \
  engine = create_engine('postgresql://postgres:password@postgres:5432/association'); \
  print(engine.connect())"
```

### Permission Issues

```bash
# Fix volume permissions
docker-compose exec app chown -R appuser:appuser /app/logs

# Recreate volumes
docker-compose down -v
docker-compose up -d
```

### Reset Everything

```bash
# Stop and remove all containers, networks, volumes
docker-compose down -v

# Remove images
docker-compose down --rmi all

# Start fresh
docker-compose up -d
```

## Useful Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose stop

# Restart service
docker-compose restart app

# Rebuild service
docker-compose build app

# Execute command in container
docker-compose exec app python manage.py

# Shell access
docker-compose exec app bash

# Remove everything
docker-compose down -v --rmi all

# View resource usage
docker stats
```

## Security Checklist

- [ ] All secrets in `.env` are randomly generated
- [ ] `.env` file has restricted permissions (`chmod 600 .env`)
- [ ] `.env` is in `.gitignore`
- [ ] `DEBUG=false` in production
- [ ] PostgreSQL port not exposed in production
- [ ] HTTPS enabled via reverse proxy
- [ ] Secure cookies enabled (`SESSION_COOKIE_SECURE=true`)
- [ ] CORS origins restricted to your domain
- [ ] Regular security updates (`docker-compose pull`)
- [ ] Database backups automated
- [ ] Container logs monitored

## Architecture

```
┌─────────────────┐
│   Reverse Proxy │ (Nginx/Traefik)
│   (Port 80/443) │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼──────┐
│  App  │ │ Authelia│
│ :8000 │ │  :9091  │
└───┬───┘ └────┬────┘
    │          │
    └────┬─────┘
         │
    ┌────▼────────┐
    │  PostgreSQL │
    │    :5432    │
    └─────────────┘
```

## Next Steps

1. Create FastAPI application structure (`app/main.py`)
2. Set up database models and migrations
3. Configure Authelia users and access control
4. Implement OAuth2 authentication flow
5. Add API endpoints
6. Write tests
7. Set up CI/CD pipeline

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Authelia Documentation](https://www.authelia.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
