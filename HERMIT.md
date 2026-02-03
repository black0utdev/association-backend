# Hermit Development Environment Setup

This project uses [Hermit](https://cashapp.github.io/hermit/) for reproducible development environments.

## 🎯 What is Hermit?

Hermit is a tool that manages your development tools in a reproducible way. It ensures everyone on the team uses the same versions of Python, Docker, Node, and other tools - all tracked in Git.

### Benefits

✅ **Reproducible** - Same tool versions across all machines  
✅ **Isolated** - No conflicts with system-installed tools  
✅ **Version-controlled** - Tool versions committed to Git  
✅ **Fast** - Pre-compiled binaries, no building required  
✅ **Cross-platform** - Works on macOS, Linux, and WSL  
✅ **Team-friendly** - Onboard new developers instantly

## 📦 What's Included

This project's Hermit environment includes:

- **Python 3.12** - Latest stable Python
- **pip** - Package installer
- **All project dependencies** - Installed via requirements.txt

Additional tools can be added as needed (Docker CLI, Node.js, kubectl, etc.)

## 🚀 Quick Start

### 1. Install Hermit (one-time)

```bash
# macOS / Linux
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash

# Verify installation
hermit version
```

### 2. Activate Project Environment

```bash
# Navigate to project
cd association-backend

# Activate environment (Hermit is already initialized)
source bin/activate-hermit

# Or use the shortcut
. bin/activate-hermit
```

### 3. Install Python Dependencies

```bash
# The Python environment is now active
python --version  # Should show Python 3.12.x

# Install project dependencies
pip install -r requirements.txt

# Verify installation
pytest --version
ruff --version
mypy --version
```

## 💡 Daily Usage

### Automatic Activation (Recommended)

Add to your shell profile for automatic activation when entering the project:

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

Now Hermit activates automatically when you `cd` into the project!

### Manual Activation

```bash
# Activate
source bin/activate-hermit

# Check active tools
hermit list

# Deactivate (when done)
deactivate-hermit
```

## 🔧 Managing Tools

### Install New Tools

```bash
# Search for available packages
hermit search python

# Install specific version
hermit install python@3.12.7

# Install latest version
hermit install python@3.12

# Install other tools
hermit install docker-cli
hermit install node@20
hermit install kubectl@1.29
```

### Update Tools

```bash
# Update to latest patch version
hermit upgrade python@3.12

# Update all tools
hermit upgrade

# Pin specific version
hermit install python@3.12.7
```

### List Installed Tools

```bash
# Show installed packages
hermit list

# Show available versions
hermit search python
```

## 📁 Project Structure

```
association-backend/
├── bin/
│   ├── hermit.hcl           # Hermit configuration
│   ├── activate-hermit      # Activation script
│   ├── python-3.12.hcl      # Python package manifest
│   └── README.md            # This file
├── .hermit.env              # Environment variables
├── .envrc                   # direnv integration (optional)
└── HERMIT.md                # This documentation
```

## 🔄 Integration with Existing Tools

### With direnv (Optional)

If you use [direnv](https://direnv.net/), the `.envrc` file automatically activates Hermit:

```bash
# Install direnv
brew install direnv  # macOS

# Configure your shell
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc  # or bash

# Allow direnv in this project
direnv allow
```

### With Docker

Hermit and Docker work together seamlessly:

```bash
# Hermit manages local tools (Python, linting)
source bin/activate-hermit
pytest
ruff check .

# Docker for services (PostgreSQL, Authelia, etc.)
docker-compose up -d
```

### With VS Code

Add to `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "terminal.integrated.env.osx": {
    "PATH": "${workspaceFolder}/bin:${env:PATH}"
  },
  "terminal.integrated.env.linux": {
    "PATH": "${workspaceFolder}/bin:${env:PATH}"
  }
}
```

## 🎓 Common Workflows

### Development

```bash
# Enter project
cd association-backend

# Hermit activates automatically (if hooks installed)
# Or activate manually: source bin/activate-hermit

# Install/update dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload

# Run tests
pytest

# Lint and format
ruff check .
ruff format .
mypy app/
```

### Adding Dependencies

```bash
# Add to requirements.txt
echo "httpx==0.26.0" >> requirements.txt

# Install
pip install -r requirements.txt

# Update Renovate will now track this dependency
```

### Team Onboarding

New team member setup:

```bash
# 1. Clone repo
git clone https://github.com/yourusername/association-backend.git
cd association-backend

# 2. Install Hermit
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash

# 3. Activate environment (Hermit installs everything automatically)
source bin/activate-hermit

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Done! Start developing
docker-compose up -d
pytest
```

## 🆚 Hermit vs Other Tools

| Feature                  | Hermit  | venv           | Docker  | asdf      |
| ------------------------ | ------- | -------------- | ------- | --------- |
| **Language-agnostic**    | ✅      | ❌ Python only | ✅      | ✅        |
| **No compilation**       | ✅ Fast | N/A            | ✅ Fast | ❌ Slow   |
| **Git-tracked versions** | ✅      | ❌             | ❌      | ❌        |
| **Cross-platform**       | ✅      | ✅             | ✅      | ✅        |
| **Isolated**             | ✅      | ✅             | ✅      | ⚠️ Global |
| **Team-friendly**        | ✅      | ⚠️             | ✅      | ⚠️        |

## 🐛 Troubleshooting

### Hermit not found

```bash
# Ensure Hermit is in PATH
export PATH="$HOME/bin:$PATH"

# Or reinstall
curl -fsSL https://github.com/cashapp/hermit/releases/latest/download/install.sh | bash
```

### Wrong Python version

```bash
# Check active Python
which python
python --version

# Reinstall Python in Hermit
hermit uninstall python
hermit install python@3.12
```

### Dependencies not installing

```bash
# Ensure Hermit environment is active
source bin/activate-hermit

# Upgrade pip
pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Environment not activating

```bash
# Check if hooks are installed
hermit version

# Reinstall hooks
eval "$(hermit hook zsh)"  # or bash

# Or activate manually
source bin/activate-hermit
```

## 📚 Resources

- **Hermit Docs**: https://cashapp.github.io/hermit/
- **Package Catalog**: https://github.com/cashapp/hermit-packages
- **GitHub Issues**: https://github.com/cashapp/hermit/issues
- **Slack Community**: https://hermit-community.slack.com/

## 🔐 Security

Hermit downloads pre-compiled binaries with verified checksums. All packages are:

✅ Checksummed for integrity  
✅ Downloaded from official sources  
✅ Isolated per-project  
✅ Version-locked in Git

## 🤝 Contributing

When adding new tools to the project:

1. Install via Hermit: `hermit install tool@version`
2. Test: `hermit list` and verify tool works
3. Commit changes: `git add bin/ && git commit -m "chore(hermit): add tool"`
4. Document in this file if needed

## ❓ FAQ

**Q: Do I need to install Python system-wide?**  
A: No! Hermit provides Python 3.12 automatically.

**Q: Can I use my existing venv?**  
A: Yes, but Hermit manages Python itself. You can still use venv for packages.

**Q: Does this work in CI?**  
A: Yes! See `.github/workflows/ci.yml` for Hermit CI usage.

**Q: What if I need a different Python version?**  
A: `hermit install python@3.11` (then update bin/hermit.hcl)

**Q: Can I use Hermit and Docker together?**  
A: Absolutely! Use Hermit for dev tools, Docker for services.

---

**Happy developing with Hermit! 🎉**
