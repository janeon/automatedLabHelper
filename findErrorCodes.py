import sys

codes = list(open("errorCodes.txt","r"))
# create a dict of codes, where key = code, value = number of times this code is found
codeDict = {}
for code in codes:
    code = code.split(":")
    codeDict.update( {code[0] : 0} )

pylint2errors = list(open("Pylint2Errors.txt"))

for line in pylint2errors:
    line = line.split("):</th>")
    code = line[0].split("(")[1]
    codeDict[code] = line[1]
