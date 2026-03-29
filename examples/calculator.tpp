VANAKKAM DA MAPLA

COMMENT PANDRAN Calculator program demonstrating arithmetic operations

COMMENT PANDRAN Declare two numbers
VAA num1 SOLLUNGA 20;
VAA num2 SOLLUNGA 5;

SOLLU "Calculator - Arithmetic Operations";
SOLLU "================================";
SOLLU "Number 1: " + num1;
SOLLU "Number 2: " + num2;
SOLLU "";

COMMENT PANDRAN Perform all 5 arithmetic operations
VAA sum SOLLUNGA num1 + num2;
SOLLU "Addition: " + num1 + " + " + num2 + " = " + sum;

VAA diff SOLLUNGA num1 - num2;
SOLLU "Subtraction: " + num1 + " - " + num2 + " = " + diff;

VAA product SOLLUNGA num1 * num2;
SOLLU "Multiplication: " + num1 + " * " + num2 + " = " + product;

VAA quotient SOLLUNGA num1 / num2;
SOLLU "Division: " + num1 + " / " + num2 + " = " + quotient;

VAA remainder SOLLUNGA num1 % num2;
SOLLU "Modulus: " + num1 + " % " + num2 + " = " + remainder;

COMMENT PANDRAN Check if first number is positive, negative, or zero
SOLLU "";
SOLLU "Number Analysis:";

ADHAVUDHU num1 > 0:
    SOLLU num1 + " is positive";
DA
ILLA ADHAVUDHU num1 < 0:
    SOLLU num1 + " is negative";
DA
ILLAATI:
    SOLLU num1 + " is zero";
DA

NANDRI VANNAKAM
