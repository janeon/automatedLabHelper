# automatedLabHelper

List of some codes: http://pylint-messages.wikidot.com/all-codes (has been copied to allCodes.txt for cleaning)
List of all codes: https://docs.pylint.org/en/1.6.0/features.html
Code types:

"I": "info",
"C": "convention",
"R": "refactor",
"W": "warning",
"E": "error",
"F": "fatal"


POST PROCESSING:
run python3 cleanOutput.py [filename] [{i,c,r,w,e,f,I,C,R,W,E,F}^\*]

where 'c' for example lists line numbers where convention errors are found for each type of C error, and 'W' gives the full list of warnings in addition to the lists of line numbers by error type
