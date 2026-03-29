# Tharunpp

A programming language powered by Tamil cinema comedy dialogues.

## Badges

[![PyPI version](https://img.shields.io/pypi/v/tharunpp?style=flat-square)](https://pypi.org/project/tharunpp/)
[![Python versions](https://img.shields.io/pypi/pyversions/tharunpp?style=flat-square)](https://pypi.org/project/tharunpp/)
[![MIT License](https://img.shields.io/pypi/l/tharunpp?style=flat-square)](LICENSE)
[![CI Status](https://img.shields.io/github/actions/workflow/status/Tharun007-TK/Tharunpp/test.yml?branch=main&style=flat-square&label=tests)](https://github.com/Tharun007-TK/Tharunpp/actions/workflows/test.yml)

## Installation

```bash
pip install tharunpp
```

## Usage

```bash
# Run a Tharun++ program
tharunpp run-file program.tpp

# Start interactive shell
tharunpp shell

# Tokenize and show parse tree
tharunpp tokenize program.tpp

# Show version
tharunpp version
```

## Program Structure

Every Tharun++ program must begin with `VANAKKAM DA MAPLA` and end with `NANDRI VANNAKAM`.

**Hello World Example:**

```
VANAKKAM DA MAPLA

SOLLU "Hello, World!" ;

NANDRI VANNAKAM
```

## Full Keyword Reference

| Purpose | Keyword | Example |
|---------|---------|---------|
| **Program Structure** |
| Program start | `VANAKKAM DA MAPLA` | `VANAKKAM DA MAPLA` |
| Program end | `NANDRI VANNAKAM` | `NANDRI VANNAKAM` |
| **Variables** |
| Declare variable | `VAA` | `VAA x = 10 ;` |
| **Output** |
| Print output | `SOLLU` | `SOLLU "Hello" ;` |
| Debug output | `KALAAI` | `KALAAI x ;` |
| Warning output | `IRUNGH BHAII` | `IRUNGH BHAII "Warning" ;` |
| **Boolean Values** |
| True | `SARI` | `VAA flag = SARI ;` |
| False | `THAPPU` | `VAA flag = THAPPU ;` |
| Null | `ONNUMEY ILLA` | `VAA x = ONNUMEY ILLA ;` |
| **Logical Operators** |
| AND | `MATUM` | `ADHAVUDHU x > 5 MATUM y < 10:` |
| OR | `ILLA` | `ADHAVUDHU x == 0 ILLA y == 0:` |
| NOT | `VENDAM` | `ADHAVUDHU VENDAM flag:` |
| **Control Flow** |
| If condition | `ADHAVUDHU` | `ADHAVUDHU x > 5:` |
| Else if | `ILLA ADHAVUDHU` | `ILLA ADHAVUDHU x > 0:` |
| Else | `ILLAATI` | `ILLAATI:` |
| Block end | `DA` | `DA` |
| While loop | `TICKTOCK TICKTOCK` | `TICKTOCK TICKTOCK x < 10:` |
| For loop start | `FIRST_LA` | `FIRST_LA i IRUNDHU 1 VARAI 5:` |
| For range start | `IRUNDHU` | (see above) |
| For range end | `VARAI` | (see above) |
| Break | `EZHUNDHIRI` | `EZHUNDHIRI ;` |
| Continue | `ADUTHADUTHU` | `ADUTHADUTHU ;` |
| **Functions** |
| Declare function | `ENDRA SHANMUGHAM` | `ENDRA SHANMUGHAM greet:` |
| Call function | `VAA MA MINNAL` | `VAA MA MINNAL greet() ;` |
| Function end | `VELI JOWW` | `VELI JOWW` |
| Return | `INDHAA LEY PATHUKO` | `INDHAA LEY PATHUKO 42 ;` |
| Lambda | `VINVELI NAYAGAN` | (future feature) |
| **Error Handling** |
| Try block | `PAAKALAM` | `PAAKALAM:` |
| Catch block | `PUDRA IVANA` | `PUDRA IVANA err:` |
| Throw error | `AIYAYO` | `AIYAYO "Error!" ;` |
| Assert | `NIL GAVANI SEL` | `NIL GAVANI SEL x > 0 ;` |
| **Lists** |
| Create list | `PATTI POTTU` | `VAA nums = PATTI POTTU [1, 2, 3] ;` |
| Append to list | `ULLAYE POD` | `ULLAYE POD nums 4 ;` |
| Get from list | `EDUTHU KO` | `VAA x = EDUTHU KO nums [0] ;` |
| List length | `YEVLO IRUKU` | `SOLLU YEVLO IRUKU nums ;` |
| **Other** |
| Pass/No-op | `THALA_OK` | `THALA_OK ;` |
| Import | `MASS` | `MASS "module" ;` |
| Comment | `COMMENT PANDRAN` | `COMMENT PANDRAN This is a comment` |

## Code Examples

### 1. Hello World

```
VANAKKAM DA MAPLA

SOLLU "Vanakkam da! Welcome to Tharun++" ;

NANDRI VANNAKAM
```

### 2. Variables and Arithmetic

```
VANAKKAM DA MAPLA

VAA x = 10 ;
VAA y = 20 ;
VAA sum = x + y ;
VAA diff = y - x ;
VAA product = x * y ;
VAA quotient = y / x ;

SOLLU "Sum:", sum ;
SOLLU "Difference:", diff ;
SOLLU "Product:", product ;
SOLLU "Quotient:", quotient ;

NANDRI VANNAKAM
```

### 3. If / Else If / Else

```
VANAKKAM DA MAPLA

VAA score = 85 ;

ADHAVUDHU score >= 90:
    SOLLU "Grade: A" ;
ILLA ADHAVUDHU score >= 80:
    SOLLU "Grade: B" ;
ILLA ADHAVUDHU score >= 70:
    SOLLU "Grade: C" ;
ILLAATI:
    SOLLU "Grade: F" ;
DA

NANDRI VANNAKAM
```

### 4. Functions with Return

```
VANAKKAM DA MAPLA

ENDRA SHANMUGHAM calculate_area:
    VAA length = 10 ;
    VAA width = 5 ;
    VAA area = length * width ;
    INDHAA LEY PATHUKO area ;
VELI JOWW

VAA result = VAA MA MINNAL calculate_area() ;
SOLLU "Area is:", result ;

NANDRI VANNAKAM
```

### 5. Error Handling with Try/Catch

```
VANAKKAM DA MAPLA

PAAKALAM:
    SOLLU "Attempting division..." ;
    VAA x = 10 ;
    VAA y = 0 ;
    ADHAVUDHU y == 0:
        AIYAYO "Cannot divide by zero!" ;
    DA
    VAA result = x / y ;
PUDRA IVANA err:
    SOLLU "Caught error:", err ;
DA

SOLLU "Program continues..." ;

NANDRI VANNAKAM
```

## Error Messages

Tharun++ provides clear error messages for common issues:

### TharunppTypeError
```
Expected list, got int
```
Raised when a value of the wrong type is used (e.g., trying to append to a non-list).

### TharunppNameError
```
Variable 'x' is not defined
```
Raised when accessing a variable that hasn't been declared.

### TharunppZeroDivisionError
```
Cannot divide by zero
```
Raised when attempting division by zero.

### TharunppSyntaxError
```
Unexpected token at line 5
```
Raised when the code has invalid syntax.

## License

MIT License - see [LICENSE](LICENSE) file for details.

