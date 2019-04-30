# automatedLabHelper

To run the right version of pylint, call the script using the following command:

`source shelltest.sh `

This will not only run pylint, it will also install the latest versions of pip, pylint, and virtualenv (in case your environment doesn't have them already) inside the virtual environment called virtual (super original I know).

### TODO:
- Write gitignore for virtual environment
- Debug in return not caught
- Possible database setup if going down the route of a more interactive website https://firebase.google.com/docs/web/setup

### DONE:
- Written a custom checker
- Figure out how to package pylint in environments



Code types:

"I": "info",
"C": "convention",
"R": "refactor",
"W": "warning",
"E": "error",
"F": "fatal"

List of some codes: http://pylint-messages.wikidot.com/all-codes (has been copied to allCodes.txt for cleaning)

List of all codes: https://docs.pylint.org/en/1.6.0/features.html


#### POST PROCESSING
run `python3 cleanOutput.py [filename] [{c,r,w,e,f,C,R,W,E,F}`<sup>\*</sup>`]`

#Lowercase := shortened lists

Where ''c','r', 'w','e','f' lists line numbers where convention/warning messages are found for each type of message (organized by error code)

#Uppercase := full lists

Capitalized counterparts give the full list of messages outputted from pylint in addition to the lists of line numbers by error type

These lists are organized and ordered by the input CLI parameter: cW gives all shortened convention messages followed by a full list of warnings

Note: To make post-processing work with our checker(s) I had to add the files to the path `miniconda3/pkgs/pylint-2.3.1-py37_0/lib/python3.7/site-packages/pylint/checkers`
