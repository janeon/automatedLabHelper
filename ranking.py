from subprocess import *
import os

def main():
    codes = list(open("errorCodes.txt","r"))
    # create a dict of codes, where key = code, value = number of times this code is found
    codeDict = {}
    for code in codes:
        code = code.split(":")
        codeDict.update( {code[0] : 0} )
    # print(codeDict)

    pylint2file = open("Pylint2Errors.txt","r")
    # this file was a result of cleaning
    # http://pylint.pycqa.org/en/latest/technical_reference/features.html#metrics-checker-reports
    pylint2codes = list(pylint2file)
    pylint2file.close()
    for line in pylint2codes:
        line = line.split("):</th>")
        code = line[0].split("(")[1]
        codeMessage = line[1]
        codeDict[code] = codeMessage

    filesFolders = ["imageEdit", "match", "primes"]
    files = "imageEdit"
    matchFiles = os.listdir("testFiles/"+files)
    for file in matchFiles:
        if file.endswith('.py'):
            fileName = "testFiles/"+files+"/"+file
            call = "python3 cleanOutput.py "+fileName+" CWERF"
            result = check_output(call.split(" ")).decode("utf-8")
            # print(result)
            print("finished", fileName)

# what is the goal of this? to look through and see how many types of errors are found? Add them to some sort of dict?

# so:
# first create a dict contain all possible errors
# look through result for that error code
    # if it's present, add 1 to that entry in the dict.

if __name__ == "__main__":
    main()
