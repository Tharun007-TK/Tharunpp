"""Tests for Tharun++ Interpreter with UPPERCASE keywords"""

import pytest
from Tharunpp.core.interpreter import (
    Interpreter,
    TharunppError,
    TharunppSyntaxError,
    TharunppNameError,
    TharunppZeroDivisionError,
    TharunppTypeError
)


def WRAP(code):
    """Wrap code in program structure"""
    return f"VANAKKAM DA MAPLA\n{code}\nNANDRI VANNAKAM"


def run_capture(code, capsys):
    """Run code and capture output"""
    interpreter = Interpreter()
    interpreter.run(code)
    captured = capsys.readouterr()
    return captured.out.strip()


def test_hello_world(capsys):
    code = WRAP('SOLLU "Hello, World!" ;')
    out = run_capture(code, capsys)
    assert out == "Hello, World!"


def test_variable_declaration(capsys):
    code = WRAP('VAA x = 42 ;\nSOLLU x ;')
    out = run_capture(code, capsys)
    assert out == "42"


def test_arithmetic_operations(capsys):
    code = WRAP('VAA x = 10 + 5 ;\nSOLLU x ;')
    out = run_capture(code, capsys)
    assert out == "15"
    
    code = WRAP('VAA x = 20 - 8 ;\nSOLLU x ;')
    out = run_capture(code, capsys)
    assert out == "12"
    
    code = WRAP('VAA x = 6 * 7 ;\nSOLLU x ;')
    out = run_capture(code, capsys)
    assert out == "42"


def test_boolean_values(capsys):
    code = WRAP('VAA flag = SARI ;\nSOLLU flag ;')
    out = run_capture(code, capsys)
    assert out == "True"
    
    code = WRAP('VAA flag = THAPPU ;\nSOLLU flag ;')
    out = run_capture(code, capsys)
    assert out == "False"


def test_null_value(capsys):
    code = WRAP('VAA x = ONNUMEY ILLA ;\nSOLLU x ;')
    out = run_capture(code, capsys)
    assert out == "None"


def test_debug_output(capsys):
    code = WRAP('KALAAI "Debug message" ;')
    out = run_capture(code, capsys)
    assert "[KALAAI]" in out
    assert "Debug message" in out


def test_if_statement(capsys):
    code = WRAP('VAA x = 10 ;\nADHAVUDHU x > 5:\n    SOLLU "Greater" ;\nDA')
    out = run_capture(code, capsys)
    assert out == "Greater"


def test_if_else_statement(capsys):
    code = WRAP('VAA x = 3 ;\nADHAVUDHU x > 5:\n    SOLLU "Greater" ;\nILLAATI:\n    SOLLU "Less" ;\nDA')
    out = run_capture(code, capsys)
    assert out == "Less"


def test_while_loop(capsys):
    code = WRAP('VAA i = 0 ;\nTICKTOCK TICKTOCK i < 3:\n    SOLLU i ;\n    i = i + 1 ;\nDA')
    out = run_capture(code, capsys)
    assert "0" in out
    assert "1" in out
    assert "2" in out


def test_for_loop(capsys):
    code = WRAP('FIRST_LA i IRUNDHU 1 VARAI 3:\n    SOLLU i ;\nDA')
    out = run_capture(code, capsys)
    lines = out.split('\n')
    assert "1" in lines
    assert "2" in lines
    assert "3" in lines


def test_function_definition_and_call(capsys):
    code = WRAP('''
ENDRA SHANMUGHAM greet:
    SOLLU "Hello from function" ;
VELI JOWW

VAA MA MINNAL greet() ;
''')
    out = run_capture(code, capsys)
    assert "Hello from function" in out


def test_function_with_return(capsys):
    code = WRAP('''
ENDRA SHANMUGHAM get_value:
    INDHAA LEY PATHUKO 42 ;
VELI JOWW

VAA result = VAA MA MINNAL get_value() ;
SOLLU result ;
''')
    out = run_capture(code, capsys)
    assert "42" in out


def test_try_catch(capsys):
    code = WRAP('''
PAAKALAM:
    AIYAYO "Test error" ;
PUDRA IVANA err:
    SOLLU err ;
DA
''')
    out = run_capture(code, capsys)
    assert "Test error" in out


def test_assert_pass(capsys):
    code = WRAP('NIL GAVANI SEL SARI ;\nSOLLU "Assert passed" ;')
    out = run_capture(code, capsys)
    assert "Assert passed" in out


def test_assert_fail():
    code = WRAP('NIL GAVANI SEL THAPPU, "Should fail" ;')
    interpreter = Interpreter()
    with pytest.raises(TharunppError):
        interpreter.run(code)


def test_pass_statement(capsys):
    code = WRAP('THALA_OK ;\nSOLLU "After pass" ;')
    out = run_capture(code, capsys)
    assert "After pass" in out


def test_division_by_zero():
    code = WRAP('VAA x = 10 / 0 ;')
    interpreter = Interpreter()
    with pytest.raises(TharunppZeroDivisionError):
        interpreter.run(code)


def test_undefined_variable():
    code = WRAP('SOLLU undefined_var ;')
    interpreter = Interpreter()
    with pytest.raises(TharunppNameError):
        interpreter.run(code)


def test_logical_and(capsys):
    code = WRAP('VAA result = SARI MATUM SARI ;\nSOLLU result ;')
    out = run_capture(code, capsys)
    assert out == "True"
    
    code = WRAP('VAA result = SARI MATUM THAPPU ;\nSOLLU result ;')
    out = run_capture(code, capsys)
    assert out == "False"


def test_logical_or(capsys):
    code = WRAP('VAA result = SARI ILLA THAPPU ;\nSOLLU result ;')
    out = run_capture(code, capsys)
    assert out == "True"
    
    code = WRAP('VAA result = THAPPU ILLA THAPPU ;\nSOLLU result ;')
    out = run_capture(code, capsys)
    assert out == "False"


def test_logical_not(capsys):
    code = WRAP('VAA result = VENDAM THAPPU ;\nSOLLU result ;')
    out = run_capture(code, capsys)
    assert out == "True"


def test_string_concat(capsys):
    out = run_capture(WRAP('VAA s = "Vanakkam" + " da" ;\nSOLLU s ;'), capsys)
    assert out == "Vanakkam da"


def test_list_operations(capsys):
    code = WRAP(
        'VAA nums = PATTI POTTU [1, 2, 3] ;\n'
        'SOLLU YEVLO IRUKU nums ;'
    )
    out = run_capture(code, capsys)
    assert out == "3"


def test_int_division(capsys):
    out = run_capture(WRAP('SOLLU 10 / 2 ;'), capsys)
    assert out == "5"


def test_comparison_operators(capsys):
    code = WRAP('SOLLU 5 < 10 ;')
    out = run_capture(code, capsys)
    assert out == "True"
    
    code = WRAP('SOLLU 5 > 10 ;')
    out = run_capture(code, capsys)
    assert out == "False"
    
    code = WRAP('SOLLU 5 == 5 ;')
    out = run_capture(code, capsys)
    assert out == "True"


def test_multiple_print_args(capsys):
    code = WRAP('SOLLU "Hello", "World", 42 ;')
    out = run_capture(code, capsys)
    assert "Hello" in out
    assert "World" in out
    assert "42" in out
