@echo off
echo Activating virtual environment and running hello.tpp...
call venv\Scripts\activate.bat
python -m Tharunpp.cli.main run-file examples\hello.tpp
pause
