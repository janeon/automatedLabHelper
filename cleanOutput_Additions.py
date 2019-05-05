# post-processes syntactical errors into more readable, less redundant / terrifying messages

from pylint import epylint
import sys
import regexChecks

def printConventions(conventionByTypes, report, codeToNames, codeMessagesDict):
    print(('-'*50)+"CONVENTION CHECKS"+('-'*50))
    for code in conventionByTypes:
        lines = conventionByTypes[code]
        if lines:
            print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" convention reminders \n\t located on line(s) ", end="")
            for line in lines:
                print(line, end=", ")
            print("\n")
            if 'C' in report:
                msgs = codeMessagesDict[code]
                for msg in msgs:
                    print('\t',msg)
                    # print(warning)

def printwarnings(warningByTypes, report, codeToNames, codeMessagesDict):
    print(('-'*51)+"WARNING  CHECKS"+('-'*51))
    for code in warningByTypes:
        lines = warningByTypes[code]
        if lines:
            print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" warnings \n\t located on line(s) ", end="")
            for line in lines:
                print(line, end=", ")
            print("\n")
            if 'W' in report:
                msgs = codeMessagesDict[code]
                for msg in msgs:
                    print('\t',msg)

def printerrors(errorByTypes, report, codeToNames, codeMessagesDict, originalCode):
        print(('-'*52)+"ERROR  CHECKS"+('-'*52))
        for code in errorByTypes:
            lines = errorByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" erors \n\t located on line(s) ", end="")
                for line in lines:
                    match = regexChecks.check(line)
                    if (match == ""):
                        print(line, end=", ")
                    else:
                        print(line, match,",")

                print("\n")
                if 'W' in report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

def printrefactors(refactorByTypes, report, codeToNames, codeMessagesDict):
        print(('-'*52)+"REFACTOR CHECKS"+('-'*52))
        for code in refactorByTypes:
            lines = refactorByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" refactors \n\t located on line(s) ", end="")
                for line in lines:
                    print(line, end=", ")
                print("\n")
                if 'W' in report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

def printfatals(fatalByTypes, report, codeToNames, codeMessagesDict):
        print(('-'*53)+"FATAL CHECKS"+('-'*53))
        for code in fatalByTypes:
            lines = fatalByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" fatal checks \n\t located on line(s) ", end="")
                for line in lines:
                    print(line, end=", ")
                print("\n")
                if 'W' in report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

def buildCode_MessagePairs(codes):
    conventions = {}
    warnings = {}
    errors = {}
    refactors = {}
    fatals = {}
    for i in range (0,25):
        codeMessage = codes[i].split(": ")
        conventions[codeMessage[0]] = codeMessage[1]
    # print(conventions)
    for i in range (25,84):
        codeMessage = codes[i].split(": ")
        errors[codeMessage[0]] = codeMessage[1]
    # print(errors)

    for i in range (84,92):
        codeMessage = codes[i].split(": ")
        fatals[codeMessage[0]] = codeMessage[1]

    for i in range (102,117):
        codeMessage = codes[i].split(": ")
        refactors[codeMessage[0]] = codeMessage[1]
    # print(refactors)

    for i in range (117,186):
        codeMessage = codes[i].split(": ")
        warnings[codeMessage[0]] = codeMessage[1]


    return (conventions, warnings, errors, refactors, fatals)

def buildCode_LineListPairs(conventions, warnings, errors, refactors, fatals):
    conventionByTypes = {} # {code : [line numbers]} where code is of type C
    warningByTypes = {} # {code : [line numbers]} where code is of type W
    errorByTypes = {}
    refactorByTypes = {}
    fatalByTypes = {}
    for code in conventions:
        conventionByTypes[code] = []
    for code in warnings:
        warningByTypes[code] = []
    for code in errors:
        errorByTypes[code] = []
    for code in refactors:
        refactorByTypes[code] = []
    for code in fatals:
        fatalByTypes[code] = []
    # print(conventionByTypes)
    ### end of processing convention messages
    # Test prints conventions dictionary
    # for convention in conventions:
    #     print(convention, conventions[convention])
    return (conventionByTypes, warningByTypes, errorByTypes, refactorByTypes, fatalByTypes)

def main():
    options = '--enable=all '  # all messages will be shown
    options += '--reports=y'  # also print the reports (ascii tables at the end)
    fname = sys.argv[1]
    report = list(sys.argv[2])

    ##### read in fname, save in originalCode to call later. for use with regexChecks.
    codeFile = open(fname,"r")
    originalCode = list(codeFile)
    codeFile.close()

    # ICRWEF
    pylint_stdout, pylint_stderr = epylint.py_run(fname + ' ' + options, return_std=True)
    # TODO: Not sure what this does yet, need to test out on more example files
    # print(pylint_stderr.getvalue())
    output = pylint_stdout.getvalue()
    output = output.split(fname)
    messages = {} # {line : message}
    for line in range (1,len(output)-1):
        warning = output[line].split(": ")
        lineNum = warning[0]
        messages[lineNum[1:]] = warning[1]
    codes = list(open("errorCodes.txt","r"))

    (conventions, warnings, errors, refactors, fatals) = buildCode_MessagePairs(codes) # {code:message}
    (conventionByTypes, warningByTypes, errorByTypes, refactorByTypes, fatalByTypes) = buildCode_LineListPairs(conventions, warnings,errors, refactors, fatals)

    codeToNames = {} # {code : name}
    codeMessagesDict = {} # {code : message}
    for line in messages:
        warning = messages[line]
        words = warning.split(" ")
        type = words[0]
        code = words[1][1:-1]
        name = words[2][:-1]
        codeToNames[code] = name
        warningMessage = " ".join(words[4:])
        if type == "convention":
            conventionByTypes[code].append(line)
        elif type == "warning":
            warningByTypes[code].append(line)
        elif type == "error":
            errorByTypes[code].append(line)
        elif type == "refactor":
            refactorByTypes[code].append(line)
        elif type == "fatal":
            fatalByTypes[code].append(line)
        if code in codeMessagesDict:
            codeMessagesDict[code].append("L" + line + ": " + warningMessage)
        else:
            codeMessagesDict[code] = ["L" + line + ": "+ warningMessage]
        # print(type,code,name)
        # print(warningMessage)
    # print(codeMessagesDict)

    for cmd in report:
        if cmd in ['c', 'C']:
            printConventions(conventionByTypes, report, codeToNames, codeMessagesDict)
        elif cmd in ['w','W']:
            printwarnings(warningByTypes, report, codeToNames, codeMessagesDict)
        elif cmd in ['e','E']:
            printerrors(errorByTypes, report, codeToNames, codeMessagesDict, originalCode)
        elif cmd in ['r','R']:
            printrefactors(refactorByTypes, report, codeToNames, codeMessagesDict)
        elif cmd in ['f','F']:
            printfatals(fatalByTypes, report, codeToNames, codeMessagesDict)
if __name__ == "__main__":
    main()
