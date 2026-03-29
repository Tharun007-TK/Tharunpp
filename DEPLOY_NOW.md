# 🚀 Quick Deployment Instructions

## Option 1: Automated (EASIEST) ⭐

Just run this single command:

```bash
deploy.bat
```

This will:
1. ✅ Clean up all temporary files
2. ✅ Reset git and stage only essential files  
3. ✅ Set remote to https://github.com/Tharun007-TK/Tharunpp.git
4. ✅ Commit all changes
5. ✅ Push to GitHub
6. ✅ Create and push v1.0.0 tag

**That's it!** Everything is automated.

---

## Option 2: Manual (Step by Step)

If you prefer to do it step-by-step:

### 1. Clean up
```bash
cleanup.bat
```

### 2. Prepare and stage
```bash
prepare_push.bat
```

### 3. Push to GitHub
```bash
git push -u origin main
```

### 4. Create release tag
```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## What to Expect

### After Pushing:

1. **GitHub Actions will run** (check Actions tab)
   - Test workflow runs immediately
   - Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

2. **After pushing tag v1.0.0:**
   - Release workflow triggers
   - Package builds automatically
   - Publishes to PyPI (if PYPI_TOKEN secret is configured)
   - Creates GitHub Release

### Setting Up PyPI (One-time):

If you want automatic PyPI publishing:

1. Go to https://pypi.org/manage/account/token/
2. Create API token
3. Copy token (starts with `pypi-...`)
4. Go to GitHub repo → Settings → Secrets and variables → Actions
5. Create new secret:
   - Name: `PYPI_TOKEN`
   - Value: paste your token

### Manual PyPI Publishing:

If you prefer to publish manually:

```bash
poetry config pypi-token.pypi your-token-here
poetry build
poetry publish
```

---

## Verification Checklist

Before deploying, ensure:

- [ ] All tests pass: `python -m pytest tests/test_interpreter.py -v`
- [ ] Examples work: `python tharunpp_cli.py run-file examples/hello.tpp`
- [ ] Package builds: `poetry build`
- [ ] Version is 1.0.0 in `pyproject.toml`

---

## Quick Commands Reference

```bash
# Run automated deployment
deploy.bat

# Run tests
python -m pytest tests/test_interpreter.py -v

# Test an example
python tharunpp_cli.py run-file examples/hello.tpp

# Build package
poetry build

# Check git status
git status

# View remote
git remote -v
```

---

## Support

- **Repository**: https://github.com/Tharun007-TK/Tharunpp
- **PyPI**: https://pypi.org/project/tharunpp/ (after publishing)
- **Issues**: https://github.com/Tharun007-TK/Tharunpp/issues

---

## 🎉 That's All!

Just run **`deploy.bat`** and you're done! 
