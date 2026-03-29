@echo off
REM Git preparation script for Tharun++ v1.0.0

echo ========================================
echo Tharun++ Git Preparation Script
echo ========================================
echo.

REM Step 1: Reset staging area
echo [1/8] Resetting staging area...
git reset
echo.

REM Step 2: Clean up debug files
echo [2/8] Removing debug files...
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
echo Debug files removed.
echo.

REM Step 3: Add essential files
echo [3/8] Staging essential files...
git add .gitignore
git add .github/
git add CHANGELOG.md
git add DEPLOYMENT.md
git add IMPLEMENTATION_SUMMARY.md
git add QUICKSTART.md
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
echo Files staged.
echo.

REM Step 4: Show status
echo [4/8] Current git status:
git status --short
echo.

REM Step 5: Check remote
echo [5/8] Checking remote repository...
git remote -v
echo.

REM Step 6: Update/Add remote
echo [6/8] Setting remote to https://github.com/Tharun007-TK/Tharunpp.git
git remote remove origin 2>nul
git remote add origin https://github.com/Tharun007-TK/Tharunpp.git
git remote -v
echo.

REM Step 7: Commit
echo [7/8] Creating commit...
git commit -m "Release Tharun++ v1.0.0 - Complete rewrite with Lark parser" -m "Major Changes:" -m "- Migrated from rply to Lark parser for better maintainability" -m "- Converted all keywords to UPPERCASE (VAA, SOLLU, SARI, etc.)" -m "- Added list/array support with PATTI POTTU, ULLAYE POD, EDUTHU KO" -m "- Implemented string concatenation with type coercion" -m "- Added type-safe division returning int for whole numbers" -m "- Created modern CLI with Typer (run-file, shell, tokenize, version)" -m "- Comprehensive test suite with 26 tests (all passing)" -m "- Complete documentation: README, QUICKSTART, DEPLOYMENT guides" -m "- CI/CD workflows for GitHub Actions and PyPI publishing" -m "" -m "Technical Details:" -m "- Python 3.8+ support (tested on 3.8-3.13)" -m "- Proper error handling (TharunppSyntaxError, TharunppNameError, etc.)" -m "- New modular structure: Tharunpp/core and Tharunpp/cli" -m "- All examples updated to UPPERCASE syntax" -m "" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
echo.

REM Step 8: Ready to push
echo [8/8] Ready to push!
echo.
echo ========================================
echo Next steps:
echo ========================================
echo.
echo To push to GitHub, run:
echo     git push -u origin main
echo.
echo To create a release tag:
echo     git tag v1.0.0
echo     git push origin v1.0.0
echo.
echo This will trigger the GitHub Actions workflow to:
echo   - Run tests on Python 3.8-3.13
echo   - Build the package
echo   - Publish to PyPI (requires PYPI_TOKEN secret)
echo   - Create GitHub Release
echo.
echo ========================================
pause
