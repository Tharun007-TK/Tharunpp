@echo off
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ============================================
echo Virtual environment setup complete!
echo ============================================
echo.
echo To activate the environment in the future, run:
echo   venv\Scripts\activate
echo.
echo To deactivate, run:
echo   deactivate
echo.
echo To test Tharun++, run:
echo   python -m Tharunpp.cli.main run-file examples\hello.tpp
echo.
pause
