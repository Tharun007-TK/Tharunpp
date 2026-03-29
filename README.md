# Tharunpp 🎬

**A programming language powered by Tamil cinema comedy dialogues.**

[![PyPI version](https://img.shields.io/pypi/v/tharunpp?style=flat-square)](https://pypi.org/project/tharunpp/)
[![Python versions](https://img.shields.io/pypi/pyversions/tharunpp?style=flat-square)](https://pypi.org/project/tharunpp/)
[![MIT License](https://img.shields.io/pypi/l/tharunpp?style=flat-square)](LICENSE)
[![CI Status](https://img.shields.io/github/actions/workflow/status/Tharun007-TK/Tharunpp/test.yml?branch=main&style=flat-square&label=tests)](https://github.com/Tharun007-TK/Tharunpp/actions/workflows/test.yml)

---

## Installation

```bash
pip install tharunpp
```

Requires Python >= 3.8.1

---

## Usage

```bash
tharunpp run-file program.tpp    # run a program
tharunpp shell                   # interactive REPL
tharunpp tokenize program.tpp    # show tokens
tharunpp version                 # show version
```

---

## Program Structure

Every program must start with `VANAKKAM DA MAPLA` and end with `NANDRI VANNAKAM`.

```
VANAKKAM DA MAPLA

    SOLLU "Vanakkam da mapla!" ;

NANDRI VANNAKAM
```

---

## Keyword Reference

### Program

| Purpose       | Keyword             |
| ------------- | ------------------- |
| Program start | `VANAKKAM DA MAPLA` |
| Program end   | `NANDRI VANNAKAM`   |
| Comment       | `COMMENT PANDRAN`   |

### Variables & Values

| Purpose          | Keyword        | Example                  |
| ---------------- | -------------- | ------------------------ |
| Declare variable | `VAA`          | `VAA x = 10 ;`           |
| True             | `SARI`         | `VAA flag = SARI ;`      |
| False            | `THAPPU`       | `VAA flag = THAPPU ;`    |
| Null             | `ONNUMEY ILLA` | `VAA x = ONNUMEY ILLA ;` |

### Output & Input

| Purpose       | Keyword        | Example                        |
| ------------- | -------------- | ------------------------------ |
| Print         | `SOLLU`        | `SOLLU "dei!" ;`               |
| Debug print   | `KALAAI`       | `KALAAI x ;`                   |
| Warning print | `IRUNGH BHAII` | `IRUNGH BHAII "careful da!" ;` |

### Operators

| Purpose    | Symbol                      |
| ---------- | --------------------------- |
| Arithmetic | `+` `-` `*` `/` `%`         |
| Comparison | `==` `!=` `>` `<` `>=` `<=` |
| AND        | `MATUM`                     |
| OR         | `ILLA`                      |
| NOT        | `VENDAM`                    |

### Control Flow

| Purpose    | Keyword             | Example                          |
| ---------- | ------------------- | -------------------------------- |
| If         | `ADHAVUDHU`         | `ADHAVUDHU x > 5 :`              |
| Else if    | `ILLA ADHAVUDHU`    | `ILLA ADHAVUDHU x == 5 :`        |
| Else       | `ILLAATI`           | `ILLAATI :`                      |
| End block  | `DA`                | `DA`                             |
| While loop | `TICKTOCK TICKTOCK` | `TICKTOCK TICKTOCK x < 10 :`     |
| For loop   | `FIRST_LA`          | `FIRST_LA i IRUNDHU 0 VARAI 5 :` |
| Break      | `EZHUNDHIRI`        | `EZHUNDHIRI ;`                   |
| Continue   | `ADUTHADUTHU`       | `ADUTHADUTHU ;`                  |

### Functions

| Purpose         | Keyword              | Example                        |
| --------------- | -------------------- | ------------------------------ |
| Define function | `ENDRA SHANMUGHAM`   | `ENDRA SHANMUGHAM add(a, b) :` |
| End function    | `VELI JOWW`          | `VELI JOWW`                    |
| Call function   | `VAA MA MINNAL`      | `VAA MA MINNAL add(1, 2) ;`    |
| Return          | `INDHAA LEY PATHUKO` | `INDHAA LEY PATHUKO x + y ;`   |

### Error Handling

| Purpose | Keyword          | Example                       |
| ------- | ---------------- | ----------------------------- |
| Try     | `PAAKALAM`       | `PAAKALAM :`                  |
| Catch   | `PUDRA IVANA`    | `PUDRA IVANA err :`           |
| Throw   | `AIYAYO`         | `AIYAYO "something broke!" ;` |
| Assert  | `NIL GAVANI SEL` | `NIL GAVANI SEL x > 0 ;`      |

### Lists

| Purpose      | Keyword       | Example                              |
| ------------ | ------------- | ------------------------------------ |
| Create list  | `PATTI POTTU` | `VAA nums = PATTI POTTU [1, 2, 3] ;` |
| Append       | `ULLAYE POD`  | `ULLAYE POD nums 4 ;`                |
| Get by index | `EDUTHU KO`   | `VAA x = EDUTHU KO nums [0] ;`       |
| Length       | `YEVLO IRUKU` | `SOLLU YEVLO IRUKU nums ;`           |

### Other

| Purpose       | Keyword    | Example         |
| ------------- | ---------- | --------------- |
| Import module | `MASS`     | `MASS "math" ;` |
| Pass / no-op  | `THALA_OK` | `THALA_OK ;`    |

---

## Examples

### Hello World

```
VANAKKAM DA MAPLA

    SOLLU "Vanakkam da mapla!" ;

NANDRI VANNAKAM
```

### Variables and Arithmetic

```
VANAKKAM DA MAPLA

    VAA x = 10 ;
    VAA y = 3 ;
    SOLLU x + y ;
    SOLLU x * y ;
    SOLLU x - y ;

NANDRI VANNAKAM
```

### If / Else if / Else

```
VANAKKAM DA MAPLA

    VAA score = 85 ;

    ADHAVUDHU score >= 90 :
        SOLLU "Grade A da!" ;
    ILLA ADHAVUDHU score >= 80 :
        SOLLU "Grade B da!" ;
    ILLA ADHAVUDHU score >= 70 :
        SOLLU "Grade C da!" ;
    ILLAATI :
        SOLLU "Fail aagitanga da..." ;
    DA

NANDRI VANNAKAM
```

### While Loop

```
VANAKKAM DA MAPLA

    VAA i = 0 ;
    TICKTOCK TICKTOCK i < 5 :
        SOLLU i ;
        VAA i = i + 1 ;
    DA

NANDRI VANNAKAM
```

### For Loop

```
VANAKKAM DA MAPLA

    FIRST_LA i IRUNDHU 0 VARAI 5 :
        SOLLU i ;
    DA

NANDRI VANNAKAM
```

### Functions

```
VANAKKAM DA MAPLA

    ENDRA SHANMUGHAM add(a, b) :
        INDHAA LEY PATHUKO a + b ;
    VELI JOWW

    VAA result = VAA MA MINNAL add(10, 20) ;
    SOLLU result ;

NANDRI VANNAKAM
```

### Error Handling

```
VANAKKAM DA MAPLA

    PAAKALAM :
        AIYAYO "something went wrong da!" ;
    PUDRA IVANA err :
        SOLLU err ;
    DA

NANDRI VANNAKAM
```

### Lists

```
VANAKKAM DA MAPLA

    VAA nums = PATTI POTTU [1, 2, 3] ;
    ULLAYE POD nums 4 ;
    SOLLU YEVLO IRUKU nums ;
    VAA first = EDUTHU KO nums [0] ;
    SOLLU first ;

NANDRI VANNAKAM
```

---

## Error Messages

Tharunpp gives Tamil-flavoured error messages:

| Error              | Message                                          |
| ------------------ | ------------------------------------------------ |
| Type error         | `Aiyayo! list venum da, int koduthutta`          |
| Undefined variable | `Dei! 'x' yaaruda avan? Declare pannada`         |
| Division by zero   | `SUPERSTAR kooda zero-a divide panna maatan bro` |
| Syntax error       | `BHAI enna da idhu? Syntax puriyalai`            |

---

## License

MIT — see [LICENSE](LICENSE) for details.

Made with ❤️ in Tamil Nadu 🎬
