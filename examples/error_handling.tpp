VANAKKAM DA MAPLA

COMMENT PANDRAN Error handling demonstration with try/catch, assert, and debug

SOLLU "Error Handling Examples";
SOLLU "======================";
SOLLU "";

COMMENT PANDRAN Example 1: Try/Catch with error throwing
SOLLU "Example 1: Try/Catch";
PAAKALAM:
    SOLLU "Attempting risky operation...";
    VAA divisor SOLLUNGA 0;
    ADHAVUDHU divisor == 0:
        AIYAYO "Cannot divide by zero!";
    DA
    SOLLU "This line will not execute";
DA
PUDRA IVANA err:
    SOLLU "Error caught: " + err;
    SOLLU "Handled gracefully!";
DA

COMMENT PANDRAN Example 2: Using assert to validate conditions
SOLLU "";
SOLLU "Example 2: Assert";
VAA age SOLLUNGA 25;
NIL GAVANI SEL age > 0;
SOLLU "Age validation passed: " + age;

VAA score SOLLUNGA 85;
NIL GAVANI SEL score >= 0 MATUM score <= 100;
SOLLU "Score validation passed: " + score;

COMMENT PANDRAN Example 3: Debug printing
SOLLU "";
SOLLU "Example 3: Debug Output";
VAA debug_var SOLLUNGA "Debugging value";
KALAAI debug_var;
KALAAI "Debug: Processing data...";

VAA counter SOLLUNGA 42;
KALAAI "Counter value: " + counter;

COMMENT PANDRAN Example 4: Warning messages
SOLLU "";
SOLLU "Example 4: Warnings";
IRUNGH BHAII "This is a warning message!";
IRUNGH BHAII "Low memory warning - consider optimization";

VAA threshold SOLLUNGA 90;
ADHAVUDHU threshold > 80:
    IRUNGH BHAII "Threshold exceeded: " + threshold;
DA

COMMENT PANDRAN Example 5: Nested try/catch
SOLLU "";
SOLLU "Example 5: Nested Error Handling";
PAAKALAM:
    SOLLU "Outer try block";
    PAAKALAM:
        SOLLU "Inner try block";
        VAA test_val SOLLUNGA 10;
        ADHAVUDHU test_val < 20:
            SOLLU "Test passed in inner block";
        DA
    DA
    PUDRA IVANA inner_err:
        SOLLU "Inner error: " + inner_err;
    DA
    SOLLU "Outer try completed successfully";
DA
PUDRA IVANA outer_err:
    SOLLU "Outer error: " + outer_err;
DA

COMMENT PANDRAN Example 6: Assert with boolean values
SOLLU "";
SOLLU "Example 6: Boolean Assertions";
VAA is_valid SOLLUNGA SARI;
NIL GAVANI SEL is_valid;
SOLLU "Boolean assertion passed";

VAA condition SOLLUNGA 5 > 3;
NIL GAVANI SEL condition;
SOLLU "Condition assertion passed";

SOLLU "";
SOLLU "All error handling examples completed successfully!";

NANDRI VANNAKAM
