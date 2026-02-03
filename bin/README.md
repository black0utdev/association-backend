# Hermit Environment

This directory contains the Hermit environment configuration for the Association Backend project.

## What is Hermit?

[Hermit](https://cashapp.github.io/hermit/) is a tool for managing development environments in a reproducible, version-controlled way. It ensures everyone on the team has the same tool versions.

## Installation

### First-time setup

1. **Install Hermit** (if not already installed):

   ```bash
   curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | /bin/bash
   ```

2. **Initialize Hermit in this project** (only needed once):

   ```bash
   hermit init .
   ```

3. **Activate the environment**:

   ```bash
   source bin/activate-hermit
   ```

   Or add to your shell profile for automatic activation:

   ```bash
   # For bash
   echo 'source ~/path/to/association-backend/bin/activate-hermit' >> ~/.bashrc

   # For zsh
   echo 'source ~/path/to/association-backend/bin/activate-hermit' >> ~/.zshrc
   ```

## Adding Tools

Install packages with:

```bash
# Python
hermit install python@3.12

# Docker CLI (if needed locally)
hermit install docker-cli

# Other tools
hermit install node@20
hermit install kubectl
```

Installed packages are automatically tracked in `bin/` directory.

## Usage

Once Hermit is activated, all tools are available:

```bash
# Check Python version
python --version

# Install project dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload

# Run tests
pytest

# Use any installed tool
ruff check .
mypy app/
```

## Deactivation

To deactivate the Hermit environment:

```bash
deactivate-hermit
```

## Files

- `hermit.hcl` - Hermit configuration
- `activate-hermit` - Shell activation script
- Package manifests - `.pkg` files for each installed tool

## Benefits

✅ **Reproducible** - Same tool versions for everyone
✅ **Isolated** - No conflicts with system tools
✅ **Version-controlled** - Tool versions tracked in Git
✅ **Fast** - Binary packages, no compilation needed
✅ **Cross-platform** - Works on macOS, Linux, WSL

## Documentation

- [Hermit Docs](https://cashapp.github.io/hermit/)
- [Package Catalog](https://github.com/cashapp/hermit-packages)
