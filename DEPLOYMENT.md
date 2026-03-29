# Deployment Guide for Tharun++

## Prerequisites

1. **GitHub Repository Setup**
   - Repository should be pushed to GitHub (e.g., `https://github.com/Tharun007-TK/Tharunpp`)
   - You need admin access to the repository

2. **PyPI Account**
   - Create account at https://pypi.org/
   - Verify your email
   - Generate API token at https://pypi.org/manage/account/token/

3. **GitHub Secrets Configuration**
   Go to repository Settings → Secrets and variables → Actions → New repository secret

   Add this secret:
   - Name: `PYPI_TOKEN`
   - Value: Your PyPI API token (starts with `pypi-...`)

## Pre-Deployment Checklist

### 1. Clean Up Temporary Files

```bash
python cleanup.py
```

This removes all debug files and temporary directories.

### 2. Run Full Test Suite

```bash
# Install dependencies if not already installed
poetry install

# Run tests
poetry run pytest tests/test_interpreter.py -v

# All 26 tests should pass
```

### 3. Verify Package Builds

```bash
poetry build
```

Should create files in `dist/`:
- `tharunpp-1.0.0.tar.gz`
- `tharunpp-1.0.0-py3-none-any.whl`

### 4. Test Package Locally

```bash
# Install the built package
pip install dist/tharunpp-1.0.0-py3-none-any.whl

# Test the CLI
tharunpp version
tharunpp run-file examples/hello.tpp
```

## Deployment Methods

### Method 1: Manual PyPI Release (Recommended for First Release)

```bash
# Build the package
poetry build

# Publish to PyPI (will prompt for credentials)
poetry publish

# Or publish with token
poetry config pypi-token.pypi your-token-here
poetry publish
```

### Method 2: GitHub Tag Release (Automated via CI/CD)

1. **Update version in pyproject.toml** (if needed)
   ```toml
   version = "1.0.0"
   ```

2. **Commit and push all changes**
   ```bash
   git add .
   git commit -m "Release v1.0.0"
   git push origin main
   ```

3. **Create and push a version tag**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

4. **GitHub Actions will automatically:**
   - Run tests
   - Build the package
   - Publish to PyPI (if PYPI_TOKEN is configured)
   - Create a GitHub Release with assets

### Method 3: Manual GitHub Release Workflow

1. Go to repository → Actions
2. Select "Release to PyPI" workflow
3. Click "Run workflow"
4. Select branch (usually `main`)
5. Click "Run workflow" button

## Post-Deployment Verification

### 1. Check PyPI

Visit https://pypi.org/project/tharunpp/ to verify:
- Package is listed
- Version number is correct
- README displays properly
- All metadata is correct

### 2. Test Installation from PyPI

```bash
# Create a clean virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from PyPI
pip install tharunpp

# Test it works
tharunpp version
tharunpp run-file examples/hello.tpp
```

### 3. Check GitHub Release

Go to https://github.com/Tharun007-TK/Tharunpp/releases
- Verify release is created
- Check release notes
- Verify dist files are attached

## Continuous Integration

The repository includes two GitHub Actions workflows:

### 1. `test.yml` - Runs on every push/PR
- Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12
- Runs linting checks
- Generates code coverage
- Builds the package

### 2. `release.yml` - Runs on version tags
- Runs tests
- Builds package
- Publishes to PyPI (on tags starting with `v`)
- Creates GitHub Release

## Versioning

Follow Semantic Versioning (semver.org):
- **MAJOR** version (1.x.x) - Incompatible API changes
- **MINOR** version (x.1.x) - New features, backwards compatible
- **PATCH** version (x.x.1) - Bug fixes

## Troubleshooting

### Build Fails
```bash
# Clear poetry cache
poetry cache clear pypi --all

# Reinstall dependencies
rm poetry.lock
poetry install
```

### Tests Fail
```bash
# Check which test is failing
poetry run pytest tests/test_interpreter.py -v -x

# Run specific test
poetry run pytest tests/test_interpreter.py::test_hello_world -v
```

### PyPI Upload Fails
```bash
# Check token is valid
poetry config pypi-token.pypi your-token-here

# Try publishing with verbose output
poetry publish -v
```

### GitHub Actions Fails
- Check Actions tab for error logs
- Verify PYPI_TOKEN secret is set correctly
- Ensure Python 3.8+ is compatible with code

## Release Checklist

- [ ] All tests pass locally
- [ ] Version bumped in `pyproject.toml`
- [ ] `CHANGELOG.md` updated with changes
- [ ] README.md is up to date
- [ ] Examples work correctly
- [ ] Package builds successfully
- [ ] Git tag created
- [ ] PyPI upload successful
- [ ] GitHub release created
- [ ] Verified installation from PyPI

## Support

For issues:
- GitHub Issues: https://github.com/Tharun007-TK/Tharunpp/issues
- Email: tharunkumarvmt@gmail.com
