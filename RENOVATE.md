# Renovate Configuration Guide

This project uses [Renovate](https://docs.renovatebot.com/) for automated dependency management.

## 📋 Overview

Renovate automatically:

- ✅ Updates Python dependencies in `requirements.txt`
- ✅ Updates Docker images in `docker-compose.yml` and `Dockerfile`
- ✅ Updates GitHub Actions in `.github/workflows/`
- ✅ Creates pull requests with changelogs and release notes
- ✅ Groups related updates to reduce PR noise
- ✅ Checks for security vulnerabilities
- ✅ Follows semantic commit conventions

## 🚀 Setup Options

### Option 1: GitHub App (Recommended)

1. **Install Renovate GitHub App**
   - Visit: https://github.com/apps/renovate
   - Click "Install"
   - Select your repository
   - Renovate will automatically detect `renovate.json`

2. **Configure (Optional)**
   - Renovate will create an onboarding PR
   - Review and merge the PR
   - Customize `renovate.json` as needed

**Advantages:**

- ✅ Zero configuration required
- ✅ Automatic updates
- ✅ Free for public repositories
- ✅ No secrets management needed

### Option 2: Self-Hosted with GitHub Actions

1. **Create GitHub App** (for better rate limits)
   - Go to: https://github.com/settings/apps/new
   - Name: `Renovate Bot`
   - Webhook: Disable
   - Permissions:
     - Repository permissions:
       - Contents: Read & Write
       - Pull Requests: Read & Write
       - Issues: Read & Write
       - Metadata: Read-only
   - Generate private key and download

2. **Add GitHub Secrets**

   ```
   Settings → Secrets → Actions → New repository secret
   ```

   Add two secrets:
   - `RENOVATE_APP_ID`: Your GitHub App ID
   - `RENOVATE_APP_PRIVATE_KEY`: Contents of private key file

3. **Enable Workflow**
   - The workflow is already configured in `.github/workflows/renovate.yml`
   - It runs every Monday at 6am UTC
   - Can also be triggered manually

**Advantages:**

- ✅ Full control over schedule
- ✅ Can run on private repositories
- ✅ Custom configuration possible

### Option 3: Use GITHUB_TOKEN (Simpler, Limited)

If you don't set up the GitHub App secrets, Renovate will use `GITHUB_TOKEN`:

**Advantages:**

- ✅ No setup required
- ✅ Works out of the box

**Limitations:**

- ❌ Lower rate limits
- ❌ Can't trigger other workflows
- ❌ May have permission issues

## 📦 Update Groups

Renovate groups related dependencies to reduce PR noise:

| Group                   | Packages                           | Schedule   | Stability Days |
| ----------------------- | ---------------------------------- | ---------- | -------------- |
| **Python dependencies** | All pip packages (patch/minor)     | Monday 6am | 3 days         |
| **Major updates**       | Individual major versions          | Monday 6am | 7 days         |
| **FastAPI framework**   | fastapi, uvicorn                   | Monday 6am | 5 days         |
| **Database**            | sqlalchemy, asyncpg, alembic       | Monday 6am | 7 days         |
| **Security**            | python-jose, passlib, authlib      | Monday 6am | 7 days         |
| **Testing**             | pytest, pytest-asyncio, pytest-cov | Monday 6am | 3 days         |
| **Code quality**        | ruff, mypy                         | Monday 6am | 3 days         |
| **Python Docker**       | python:3.12-slim                   | Monday 6am | 7 days         |
| **PostgreSQL Docker**   | postgres:16-alpine                 | Monday 6am | 14 days        |
| **Authelia Docker**     | authelia/authelia:latest           | Monday 6am | 7 days         |
| **GitHub Actions**      | All actions                        | Monday 6am | 3 days         |

## 🎯 Update Strategy

### Patch & Minor Updates

- Grouped together (e.g., `1.2.3` → `1.2.4` and `1.2.0` → `1.3.0`)
- Wait 3 days for stability
- Auto-merge: **Disabled** (manual review required)

### Major Updates

- Separate PR for each package (e.g., `1.x` → `2.x`)
- Wait 7 days for stability
- Labeled as `major-update` for easy identification
- **Always requires manual review**

### Security Updates

- Highest priority
- Only 1 day stability wait
- Labeled as `security`

### Docker Updates

- Pin digests for reproducibility
- Separate PRs for base images
- PostgreSQL updates wait 14 days (critical service)

## 🔧 Customization

### Change Schedule

Edit `renovate.json`:

```json
{
  "schedule": ["before 6am on Monday"] // Change to your preference
}
```

Options:

- `"at any time"` - Immediate updates
- `"before 6am every weekday"` - Daily updates
- `"on the first day of the month"` - Monthly updates

### Enable Auto-merge (Not Recommended Initially)

After project matures and tests are comprehensive:

```json
{
  "packageRules": [
    {
      "matchUpdateTypes": ["patch"],
      "automerge": true,
      "automergeType": "pr"
    }
  ]
}
```

### Ignore Specific Dependencies

```json
{
  "ignoreDeps": ["package-name", "another-package"]
}
```

### Pin to Specific Version

```json
{
  "packageRules": [
    {
      "matchPackageNames": ["fastapi"],
      "allowedVersions": "<0.110.0"
    }
  ]
}
```

## 📊 Dependency Dashboard

Renovate creates a GitHub Issue called "Dependency Dashboard" that shows:

- ✅ Pending updates
- ⏸️ Rate-limited updates
- ❌ Failed updates
- 🕐 Scheduled updates

View it at: `Issues → Dependency Dashboard`

## 🔍 Reviewing Renovate PRs

When Renovate creates a PR:

### 1. Check the PR Description

- Review changelog and release notes
- Check for breaking changes
- Look at dependencies that changed

### 2. Verify CI Tests

```bash
# All tests should pass automatically
# Check GitHub Actions results
```

### 3. Test Locally (If Needed)

```bash
# Pull the PR branch
git fetch origin pull/<PR_NUMBER>/head:renovate-test
git checkout renovate-test

# Rebuild and test
docker-compose build
docker-compose up -d
docker-compose exec api pytest
```

### 4. Review Changes

```bash
# Check what changed in requirements.txt
git diff main -- requirements.txt

# Check Docker image updates
git diff main -- docker-compose.yml Dockerfile
```

### 5. Merge

- ✅ If tests pass and changes look good
- 🔴 If tests fail, investigate or close PR

## 🚨 Security Vulnerabilities

Renovate automatically detects security vulnerabilities:

1. **Alerts labeled with `security`**
2. **Higher priority in queue**
3. **Shorter stability period (1 day)**

Always prioritize security updates!

## 📝 Commit Messages

Renovate follows semantic commit conventions:

```
chore(deps): update fastapi to v0.109.0
chore(docker): update postgres Docker tag to v16.1
chore(ci): update actions/checkout action to v4
```

These trigger patch version bumps in semantic-release.

## 🛠️ Troubleshooting

### Renovate Not Creating PRs

1. **Check Dependency Dashboard Issue**
   - Look for rate limiting
   - Check for configuration errors

2. **Verify Configuration**

   ```bash
   # Validate locally
   npx renovate-config-validator
   ```

3. **Check Logs**
   - GitHub Actions → Renovate workflow → View logs

### PRs Failing CI

1. **Review test failures**
2. **Check if breaking changes in dependencies**
3. **Update code to handle new versions**

### Too Many PRs

Reduce frequency:

```json
{
  "prConcurrentLimit": 2,
  "prHourlyLimit": 1
}
```

## 📚 Resources

- **Renovate Docs**: https://docs.renovatebot.com/
- **Configuration Options**: https://docs.renovatebot.com/configuration-options/
- **Preset Configs**: https://docs.renovatebot.com/presets-config/
- **Self-Hosting**: https://docs.renovatebot.com/self-hosting/

## 🎯 Best Practices

1. ✅ **Start conservative** - Disable auto-merge initially
2. ✅ **Review dashboards weekly** - Check Dependency Dashboard
3. ✅ **Monitor failed updates** - Investigate and fix
4. ✅ **Update Renovate config** - As project matures
5. ✅ **Enable auto-merge** - After comprehensive test coverage
6. ✅ **Pin Docker digests** - For reproducibility
7. ✅ **Group related packages** - Reduce PR noise
8. ✅ **Prioritize security** - Merge security patches quickly

---

**Renovate keeps your dependencies fresh and secure! 🔄🔒**
