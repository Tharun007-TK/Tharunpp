# Quick Start Guide for Tharun++

## Option 1: Automated Setup (Recommended)

Simply run the setup script:
```bash
setup_venv.bat
```

This will:
1. Create a virtual environment in the `venv` folder
2. Activate it
3. Install all required dependencies

## Option 2: Manual Setup

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
```bash
# On Windows
venv\Scripts\activate

# You should see (venv) in your terminal prompt
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Running Tharun++ Programs

Once your virtual environment is activated:

### Run an example file:
```bash
python -m Tharunpp.cli.main run-file examples\hello.tpp
```

### Or use the shortcut:
```bash
run_example.bat
```

### Interactive shell:
```bash
python -m Tharunpp.cli.main shell
```

### Show parse tree:
```bash
python -m Tharunpp.cli.main tokenize examples\hello.tpp
```

### Check version:
```bash
python -m Tharunpp.cli.main version
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/test_interpreter.py -v

# Run specific test
python -m pytest tests/test_interpreter.py::test_hello_world -v

# Run with coverage
python -m pytest tests/test_interpreter.py --cov=Tharunpp
```

## Quick Verification

```bash
# Test grammar
python test_grammar.py

# Test end-to-end
python test_e2e.py

# Run all verifications
python verify_all.py
```

## Deactivating Virtual Environment

When you're done:
```bash
deactivate
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'lark'"
**Solution:** Make sure you activated the virtual environment first:
```bash
venv\Scripts\activate
```

### Issue: "python is not recognized"
**Solution:** Make sure Python is installed and added to your PATH.

### Issue: Virtual environment not activating
**Solution:** Try running PowerShell as administrator or use Command Prompt instead.

## What's Installed

- **lark** (>=1.1.9) - Parser generator for the Tharun++ grammar
- **typer** (>=0.4.1) - CLI framework
- **loguru** (>=0.6.0) - Logging library
- **pytest** (>=7.1.2) - Testing framework
- **pytest-cov** (>=3.0.0) - Code coverage for tests

## Creating Your First Program

Create a new file `my_program.tpp`:

```
VANAKKAM DA MAPLA

VAA name = "World" ;
SOLLU "Hello,", name, "!" ;

VAA x = 10 ;
VAA y = 20 ;
SOLLU "Sum:", x + y ;

NANDRI VANNAKAM
```

Run it:
```bash
python -m Tharunpp.cli.main run-file my_program.tpp
```

## Next Steps

1. Check out the examples in the `examples/` folder
2. Read the full language reference in `README.md`
3. Run the test suite to see more usage examples
4. Start writing your own Tharun++ programs!

Enjoy coding in Tharun++! 🎉
