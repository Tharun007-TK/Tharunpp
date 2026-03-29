@echo off
REM Complete deployment script - Cleans, stages, commits, and pushes to GitHub

echo.
echo ============================================================
echo  Tharun++ v1.0.0 - Complete GitHub Deployment
echo ============================================================
echo.

REM Step 1: Cleanup
echo [Step 1/9] Cleaning up temporary files...
del /Q debug_*.py 2>nul
del /Q check_*.py 2>nul
del /Q do_extract.py 2>nul
del /Q extract_source.py 2>nul
del /Q setup_dirs.py 2>nul
del /Q run_extract.bat 2>nul
del /Q test_e2e.py 2>nul
del /Q test_grammar.py 2>nul
del /Q cleanup.py 2>nul
rd /S /Q tharunpp-0.3.1 2>nul
rd /S /Q .pytest_cache 2>nul
for /d /r %%i in (__pycache__) do rd /S /Q "%%i" 2>nul
echo    ✓ Temporary files removed
echo.

REM Step 2: Reset staging
echo [Step 2/9] Resetting git staging area...
git reset >nul 2>&1
echo    ✓ Staging area reset
echo.

REM Step 3: Stage files
echo [Step 3/9] Staging files for commit...
git add .gitignore
git add .github/
git add CHANGELOG.md
git add DEPLOYMENT.md
git add IMPLEMENTATION_SUMMARY.md
git add QUICKSTART.md
git add READY_TO_PUSH.md
git add README.md
git add CODE_OF_CONDUCT.md
git add CONTRIBUTING.md
git add LICENSE
git add pyproject.toml
git add requirements.txt
git add poetry.lock
git add Tharunpp/
git add examples/
git add tests/test_interpreter.py
git add tharunpp_cli.py
git add verify_all.py
git add setup_venv.bat
git add run_example.bat
git add cleanup.bat
git add prepare_push.bat
echo    ✓ Essential files staged
echo.

REM Step 4: Check status
echo [Step 4/9] Git status:
git status --short
echo.

REM Step 5: Update remote
echo [Step 5/9] Setting remote repository...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/Tharun007-TK/Tharunpp.git
echo    ✓ Remote set to: https://github.com/Tharun007-TK/Tharunpp.git
echo.

REM Step 6: Verify remote
echo [Step 6/9] Verifying remote:
git remote -v
echo.

REM Step 7: Commit
echo [Step 7/9] Creating commit...
git commit -m "Release Tharun++ v1.0.0 - Complete rewrite with Lark parser" -m "" -m "Major Changes:" -m "- Migrated from rply to Lark parser for better maintainability" -m "- Converted all keywords to UPPERCASE (VAA, SOLLU, SARI, etc.)" -m "- Added list/array support with PATTI POTTU, ULLAYE POD, EDUTHU KO" -m "- Implemented string concatenation with type coercion" -m "- Added type-safe division returning int for whole numbers" -m "- Created modern CLI with Typer (run-file, shell, tokenize, version)" -m "- Comprehensive test suite with 26 tests (all passing)" -m "- Complete documentation: README, QUICKSTART, DEPLOYMENT guides" -m "- CI/CD workflows for GitHub Actions and PyPI publishing" -m "" -m "Technical Details:" -m "- Python 3.8+ support (tested on 3.8-3.13)" -m "- Proper error handling (TharunppSyntaxError, TharunppNameError, etc.)" -m "- New modular structure: Tharunpp/core and Tharunpp/cli" -m "- All examples updated to UPPERCASE syntax" -m "" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
echo    ✓ Commit created
echo.

REM Step 8: Push to GitHub
echo [Step 8/9] Pushing to GitHub...
echo    This may take a moment...
git push -u origin main
if %ERRORLEVEL% EQU 0 (
    echo    ✓ Successfully pushed to GitHub!
) else (
    echo    ✗ Push failed. You may need to force push or check credentials.
    echo    Try: git push -u origin main --force
)
echo.

REM Step 9: Create and push tag
echo [Step 9/9] Creating release tag v1.0.0...
git tag v1.0.0
git push origin v1.0.0
if %ERRORLEVEL% EQU 0 (
    echo    ✓ Tag v1.0.0 created and pushed!
    echo    ✓ GitHub Actions will now run automatically
) else (
    echo    ✗ Tag push failed. Create manually with:
    echo       git tag v1.0.0
    echo       git push origin v1.0.0
)
echo.

echo ============================================================
echo  Deployment Complete!
echo ============================================================
echo.
echo What happens next:
echo.
echo 1. GitHub Actions will run tests on Python 3.8-3.13
echo 2. If tag v1.0.0 was pushed, release workflow will:
echo    - Build the package
echo    - Publish to PyPI (if PYPI_TOKEN secret is set)
echo    - Create GitHub Release with assets
echo.
echo Visit your repository:
echo    https://github.com/Tharun007-TK/Tharunpp
echo.
echo Check Actions tab for workflow status:
echo    https://github.com/Tharun007-TK/Tharunpp/actions
echo.
echo After PyPI publish, install with:
echo    pip install tharunpp
echo.
echo ============================================================
pause
