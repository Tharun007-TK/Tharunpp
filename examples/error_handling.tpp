COMMENT PANDRAN Tharun++ Error Handling Example

VANAKKAM DA MAPLA

COMMENT PANDRAN Try-catch example
PAAKALAM:
    SOLLU "Attempting risky operation..." ;
    VAA x = 10 ;
    VAA y = 0 ;
    ADHAVUDHU y == 0:
        AIYAYO "Cannot divide by zero!" ;
    DA
    VAA result = x / y ;
    SOLLU "Result:", result ;
PUDRA IVANA err:
    SOLLU "Caught error:", err ;
DA

COMMENT PANDRAN Assert example
VAA age = 25 ;
NIL GAVANI SEL age > 18, "Age must be greater than 18" ;
SOLLU "Age is valid:", age ;

COMMENT PANDRAN Boolean logic
VAA is_valid = SARI ;
VAA is_active = THAPPU ;

ADHAVUDHU is_valid MATUM is_active:
    SOLLU "Both conditions are true" ;
ILLA ADHAVUDHU is_valid ILLA is_active:
    SOLLU "At least one condition is true" ;
ILLAATI:
    SOLLU "Neither condition is true" ;
DA

COMMENT PANDRAN Using VENDAM (NOT)
VAA flag = THAPPU ;
ADHAVUDHU VENDAM flag:
    SOLLU "Flag is false" ;
DA

NANDRI VANNAKAM
