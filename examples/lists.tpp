VANAKKAM DA MAPLA

COMMENT PANDRAN List operations demonstration

COMMENT PANDRAN Create a list of 5 numbers
VAA numbers SOLLUNGA PATTI POTTU [10, 20, 30, 40, 50];
SOLLU "Initial list created with 5 numbers";

COMMENT PANDRAN Append two more numbers to the list
ULLAYE POD numbers 60;
ULLAYE POD numbers 70;
SOLLU "Added two more numbers to the list";

COMMENT PANDRAN Print the list length
VAA list_length SOLLUNGA YEVLO IRUKU numbers;
SOLLU "Total numbers in list: " + list_length;

COMMENT PANDRAN Get first and last elements
VAA first_element SOLLUNGA EDUTHU KO numbers [0];
SOLLU "First element: " + first_element;

VAA last_index SOLLUNGA list_length - 1;
VAA last_element SOLLUNGA EDUTHU KO numbers [last_index];
SOLLU "Last element: " + last_element;

COMMENT PANDRAN Get middle element
VAA middle_element SOLLUNGA EDUTHU KO numbers [3];
SOLLU "Element at index 3: " + middle_element;

COMMENT PANDRAN Print all elements using a for loop
SOLLU "";
SOLLU "All elements in the list:";
FIRST_LA i IRUNDHU 0 VARAI 6:
    VAA element SOLLUNGA EDUTHU KO numbers [i];
    SOLLU "Index " + i + ": " + element;
DA

COMMENT PANDRAN Create an empty list and add elements
VAA empty_list SOLLUNGA PATTI POTTU [];
SOLLU "";
SOLLU "Created empty list";
ULLAYE POD empty_list 100;
ULLAYE POD empty_list 200;
ULLAYE POD empty_list 300;

VAA new_length SOLLUNGA YEVLO IRUKU empty_list;
SOLLU "New list length: " + new_length;

SOLLU "";
SOLLU "List operations completed!";

NANDRI VANNAKAM
