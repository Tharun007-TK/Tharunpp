VANAKKAM DA MAPLA

COMMENT PANDRAN Function examples demonstrating function definitions and calls

COMMENT PANDRAN Function 1: Add two numbers
ENDRA SHANMUGHAM add(a, b):
    VAA result SOLLUNGA a + b;
    INDHAA LEY PATHUKO result;
VELI JOWW

COMMENT PANDRAN Function 2: Check if number is even
ENDRA SHANMUGHAM is_even(n):
    VAA mod_result SOLLUNGA n % 2;
    ADHAVUDHU mod_result == 0:
        INDHAA LEY PATHUKO SARI;
    DA
    ILLAATI:
        INDHAA LEY PATHUKO THAPPU;
    DA
VELI JOWW

COMMENT PANDRAN Function 3: Calculate factorial using while loop
ENDRA SHANMUGHAM factorial(n):
    VAA result SOLLUNGA 1;
    VAA counter SOLLUNGA n;
    
    TICKTOCK TICKTOCK counter > 0:
        result SOLLUNGA result * counter;
        counter SOLLUNGA counter - 1;
    DA
    
    INDHAA LEY PATHUKO result;
VELI JOWW

COMMENT PANDRAN Main program - Call all functions and print results
SOLLU "Function Examples";
SOLLU "================";
SOLLU "";

COMMENT PANDRAN Test addition function
VAA sum SOLLUNGA VAA MA MINNAL add(10, 5);
SOLLU "add(10, 5) = " + sum;

COMMENT PANDRAN Test is_even function
VAA check1 SOLLUNGA VAA MA MINNAL is_even(4);
SOLLU "is_even(4) = " + check1;

VAA check2 SOLLUNGA VAA MA MINNAL is_even(7);
SOLLU "is_even(7) = " + check2;

COMMENT PANDRAN Test factorial function
VAA fact5 SOLLUNGA VAA MA MINNAL factorial(5);
SOLLU "factorial(5) = " + fact5;

VAA fact7 SOLLUNGA VAA MA MINNAL factorial(7);
SOLLU "factorial(7) = " + fact7;

SOLLU "";
SOLLU "All function tests completed!";

NANDRI VANNAKAM
