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


#### POST PROCESSING
run python3 cleanOutput.py [filename] [{i,c,r,w,e,f,I,C,R,W,E,F}<sup>\*</sup>]

#Lowercase := shortened lists
Where ''c','w' lists line numbers where convention/warning messages are found for each type of message (organized by error code) 

#Uppercase := full lists
Capitalized counterparts give the full list of messages outputted from pylint in addition to the lists of line numbers by error type 

These lists are organized and ordered by the input CLI parameter: cW gives all shortened convention messages followed by a full list of warnings

I think you should use an
`<addr>` element here instead.
