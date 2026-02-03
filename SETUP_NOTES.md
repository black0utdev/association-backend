# Setup Notes

## ✅ Hermit Environment Fixed

The Hermit environment has been properly configured with the following packages:

- **Python 3.12.3** - Installed from Hermit's official package repository
- **pip 24.0** - Included with Python package
- **uv (latest)** - Modern Python package manager (optional, faster alternative to pip)

## 🚀 Quick Start

```bash
# 1. Activate Hermit environment
source bin/activate-hermit

# 2. Verify Python and pip are available
python --version  # Python 3.12.3
pip --version     # pip 24.0

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Start Docker services
docker-compose up -d

# 5. Verify setup
curl http://localhost:8000/health
```

## 📦 Installed Hermit Packages

```bash
# List all installed packages
hermit list
```

**Current packages:**

- `python3@3.12` - Python interpreter with pip included
- `uv@latest` - Fast Python package manager (optional)

## 🔧 What Changed

### Before (Broken)

- Had a custom `bin/python-3.12.hcl` manifest trying to build Python from source
- Multiple syntax errors in the manifest
- pip was not available

### After (Fixed)

- Removed custom manifest
- Installed Python from Hermit's official package repository
- pip is now included automatically
- Added `uv` as a modern alternative to pip

## 💡 Using uv (Optional)

`uv` is an extremely fast Python package manager written in Rust. You can use it as a drop-in replacement for pip:

```bash
# Install dependencies with uv (much faster)
uv pip install -r requirements.txt

# Install a single package
uv pip install fastapi

# Sync dependencies (like pip install -r requirements.txt but faster)
uv pip sync requirements.txt
```

## 🐚 Shell Integration (Recommended)

Enable automatic Hermit activation when entering the project directory:

**For Zsh:**

```bash
echo 'eval "$(hermit hook zsh)"' >> ~/.zshrc
source ~/.zshrc
```

**For Bash:**

```bash
echo 'eval "$(hermit hook bash)"' >> ~/.bashrc
source ~/.bashrc
```

Now Hermit will activate automatically when you `cd` into the project!

## 📝 Adding More Tools

You can easily add more development tools:

```bash
# Search for available packages
hermit search docker
hermit search node
hermit search kubectl

# Install tools
hermit install docker-cli@latest
hermit install node@20
hermit install kubectl@1.29

# Update tools
hermit upgrade
```

## 🔍 Troubleshooting

### "pip: command not found"

Make sure you've activated the Hermit environment:

```bash
source bin/activate-hermit
```

### "Python version mismatch"

Deactivate any existing virtual environments first:

```bash
deactivate  # If using venv
source bin/activate-hermit
```

### "Hermit not found"

Install Hermit first:

```bash
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash
```

## 📚 More Information

- [Hermit Documentation](https://cashapp.github.io/hermit/)
- [Full Setup Guide](./HERMIT.md)
- [Project README](./README.md)
