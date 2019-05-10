from subprocess import *
import os

def main():
    codes = list(open("errorCodes.txt","r"))
    # create a dict of codes, where key = code, value = number of times this code is found
    codeDict = {}
    for code in codes:
        code = code.split(":")
        codeDict.update( {code[0] : 0} )
    print(codeDict)

    matchFiles = os.listdir("testFiles/match")
    for file in matchFiles:
        fileName = "testFiles/match/"+file
        call = "python3 cleanOutput.py "+fileName+" CWERF"
        result = check_output(call.split(" ")).decode("utf-8")
        #print(result)


# what is the goal of this? to look through and see how many types of errors are found? Add them to some sort of dict?

# so:
# first create a dict contain all possible errors
# look through result for that error code
    # if it's present, add 1 to that entry in the dict.

if __name__ == "__main__":
    main()
