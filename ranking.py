""" ranking.py
    takes in a list of folders and reads each python file in each of the folders.
    It then outputs a list of pylint errors and the number of times each error was
    found throughout all the files.
"""
from subprocess import *
import os
import cleanOutput
import argparse

def getKey(item):
    return item[1]

def main():
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='print all errors (including those with value 0)', action="store_true")
    parser.add_argument ('-p', '--progress', help='print the name of each file as it is processed', action="store_true")
    parser.add_argument ('-o', '--outfile', help='print the name of each file as it is processed')
    parser.add_argument('folders', help='list the paths to folders you want to read from (including / after folder name)', nargs='+')
    args = parser.parse_args()

    # creating a list of error codes
    codes = list(open("errorCodes.txt","r"))
    # create a dict of codes, where key = code, value = number of times this code is found
    codeDict = {}
    for code in codes:
        code = code.split(":")
        codeDict.update( {code[0] : 0} )

    pylint2file = open("Pylint2Errors.txt","r")
    # this file was a result of cleaning
    # http://pylint.pycqa.org/en/latest/technical_reference/features.html#metrics-checker-reports
    pylint2codes = list(pylint2file)
    pylint2file.close()
    for line in pylint2codes:
        line = line.split("):</th>")
        code = line[0].split("(")[1]
        codeDict.update( {code : 0 } )

    # processing files in folders
    for folder in args.folders:
        matchFiles = os.listdir(folder)
        for file in matchFiles:
            if file.endswith('.py'):
                fileName = folder+file
                output = cleanOutput.cleanOutput(fileName, "CWERF", "--enable=all --reports=y")
                output.clean()
                for error in output.codesFound:
                    codeDict[error] += output.codesFound[error]
                if args.progress:
                    print("finished "+fileName)

    # producing output
    if args.outfile:
        open(args.outfile, "w+").close()
        f = open(args.outfile, "a")
    codeList = []
    for entry in codeDict:
        codeList.append((entry, codeDict[entry]))
    codeList = sorted(codeList, key=getKey, reverse=True)
    print("Error prevalences: ")
    if args.all:
        for entry in codeList:
            if args.outfile:
                f.write(entry[0]+": "+str(entry[1]))
            else:
                print(entry[0]+": "+str(entry[1]))
    else:
        for entry in codeList:
            if entry[1] != 0:
                if args.outfile:
                    f.write(entry[0]+": "+str(entry[1]))
                else:
                    print(entry[0]+": "+str(entry[1]))

if __name__ == "__main__":
    main()
