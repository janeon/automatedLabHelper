# automatedLabHelper

The lab helper now has an interface!
run with `python3 interface.py`

This will not only run pylint, it will also install the latest versions of pip, pylint, and virtualenv (in case your environment doesn't have them already) inside the virtual environment called virtual (super original I know).

### TODO:
- Make it possible to run cleanoutput on interface
- Find sites that targets/is often visited or popular among beginning Python coders and scrape from each for example code or demos / articles / documentation.

### DONE:
- Basic interface for making installing and file browsing easier 
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

These lists are organized and ordered by the second CLI argument:

'cW' gives all shortened convention messages followed by a full list of warnings
