@echo off
REM Cleanup script for Windows - removes debug and temporary files

echo Cleaning up debug files...

REM Remove debug scripts
del /Q debug_*.py 2>nul
del /Q check_*.py 2>nul
del /Q do_extract.py 2>nul
del /Q extract_source.py 2>nul
del /Q setup_dirs.py 2>nul
del /Q run_extract.bat 2>nul
del /Q test_e2e.py 2>nul
del /Q test_grammar.py 2>nul

REM Remove extracted directory
rd /S /Q tharunpp-0.3.1 2>nul

REM Remove pytest cache
rd /S /Q .pytest_cache 2>nul

REM Remove __pycache__ directories
for /d /r %%i in (__pycache__) do rd /S /Q "%%i" 2>nul

REM Remove .pyc files
for /r %%i in (*.pyc) do del /Q "%%i" 2>nul

echo.
echo Cleanup complete!
echo.
echo The following files/directories have been removed:
echo - debug_*.py (all debug scripts)
echo - check_*.py (all check scripts)
echo - do_extract.py, extract_source.py
echo - setup_dirs.py, run_extract.bat
echo - test_e2e.py, test_grammar.py
echo - tharunpp-0.3.1 directory
echo - .pytest_cache
echo - All __pycache__ directories
echo.
pause
