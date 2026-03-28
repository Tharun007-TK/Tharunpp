"""Verification script for Tharun++"""

print("=" * 60)
print("STEP 1: Grammar Validation")
print("=" * 60)
try:
    from lark import Lark
    from pathlib import Path
    grammar = Path('Tharunpp/core/tharunpp.lark').read_text()
    Lark(grammar, parser='earley', ambiguity='resolve')
    print('✓ Grammar: OK')
except Exception as e:
    print(f'✗ Grammar validation failed: {e}')

print("\n" + "=" * 60)
print("STEP 2: Running Test Suite")
print("=" * 60)
import subprocess
result = subprocess.run(['python', '-m', 'pytest', 'tests/', '-v'], 
                       capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
print(f"Exit code: {result.returncode}")

print("\n" + "=" * 60)
print("STEP 3: End-to-End Test")
print("=" * 60)
try:
    from Tharunpp.core.interpreter import Interpreter
    code = open('examples/hello.tpp').read()
    print("Running examples/hello.tpp:")
    print("-" * 40)
    Interpreter().run(code)
    print("-" * 40)
    print("✓ End-to-end test: OK")
except Exception as e:
    print(f"✗ End-to-end test failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("STEP 4: Package Build")
print("=" * 60)
result = subprocess.run(['poetry', 'build'], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
print(f"Exit code: {result.returncode}")
if result.returncode == 0:
    print("✓ Package build: OK")
else:
    print("✗ Package build failed")

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE")
print("=" * 60)
