# post-processes syntactical errors into more readable, less redundant / terrifying messages

from pylint import epylint
import sys
import regexChecks
ticks = 45
def printConventions(conventionByTypes, report, codeToNames, codeMessagesDict):
    print()
    print((' '*ticks)+"CONVENTION CHECKS"+(' '*ticks))
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
    print()
    print((' '*ticks)+"WARNING  CHECKS"+(' '*ticks))
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
    print()
    print((' '*ticks)+"ERROR  CHECKS"+(' '*ticks))
    if errorByTypes["E0001"] != []:
        print("Found 1", "\""+codeToNames["E0001"]+ "\" errors \n\t located on line ", end="")
        l = errorByTypes["E0001"]
        print(l[0])
        print('\t',"Note: While you have a syntax error, output from other code checks won't show up.\n")

        match = regexChecks.check(originalCode[int(l[0])-1])
        print('\t',codeMessagesDict["E0001"][0],'\t',match)
    else:
        for code in errorByTypes:
            lines = errorByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" errors \n\t located on line(s) ", end="")
                match = ""
                for line in lines:
                    ### save in case
                    #if code == "E0001":
                        #match = regexChecks.check(originalCode[int(line)-1])
                    print(line, end=", ")
                print("\n")
                if 'E' in report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        ### save in case
                        #print('\t',msg,'\t',match)
                        print('\t',msg)

def printrefactors(refactorByTypes, report, codeToNames, codeMessagesDict):
    print()
    print((' '*ticks)+"REFACTOR CHECKS"+(' '*ticks))
    for code in refactorByTypes:
        lines = refactorByTypes[code]
        if lines:
            print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" refactors \n\t located on line(s) ", end="")
            for line in lines:
                print(line, end=", ")
            print("\n")
            if 'R' in report:
                msgs = codeMessagesDict[code]
                for msg in msgs:
                    print('\t',msg)

def printfatals(fatalByTypes, report, codeToNames, codeMessagesDict):
    print()
    print((' '*ticks)+"FATAL CHECKS"+(' '*ticks))
    for code in fatalByTypes:
        lines = fatalByTypes[code]
        if lines:
            print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" fatal checks \n\t located on line(s) ", end="")
            for line in lines:
                print(line, end=", ")
            print("\n")
            if 'F' in report:
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
    #### read in fname, save in originalCode to use later
    codeFile = open(fname,"r")
    originalCode = list(codeFile)
    #print(originalCode)
    codeFile.close()

    # ICRWEF
    pylint_stdout, pylint_stderr = epylint.py_run(fname + ' ' + options, return_std=True)
    # TODO: Not sure what this does yet, need to test out on more example files
    # print(pylint_stderr.getvalue())
    output = pylint_stdout.getvalue()
    output = output.split(fname)
    messages = {} # {line : message}
    for line in range (1,len(output)):
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

    #for cmd in report:
    ########## (i changed this b/c if you did "WCRRRRRRR" it would print R like 7 times. also I wanted
    ##########  to modify it to print syntax errors even if 'E' wasn't selected in report.)
        # if cmd in ['c', 'C']:
        #     printConventions(conventionByTypes, report, codeToNames, codeMessagesDict)
        # elif cmd in ['w','W']:
        #     printwarnings(warningByTypes, report, codeToNames, codeMessagesDict)
        # elif cmd in ['e','E']:
        #     printerrors(errorByTypes, report, codeToNames, codeMessagesDict, originalCode)
        # elif cmd in ['r','R']:
        #     printrefactors(refactorByTypes, report, codeToNames, codeMessagesDict)
        # elif cmd in ['f','F']:
        #     printfatals(fatalByTypes, report, codeToNames, codeMessagesDict)

    # handling input from report:
    if ('c' in report) or ('C' in report):
        printConventions(conventionByTypes, report, codeToNames, codeMessagesDict)
    if ('w' in report) or ('W' in report):
        printwarnings(warningByTypes, report, codeToNames, codeMessagesDict)
    if ('e' in report) or ('E' in report) or (errorByTypes["E0001"] != []):
        printerrors(errorByTypes, report, codeToNames, codeMessagesDict, originalCode)
    if ('r' in report) or ('R' in report):
        printrefactors(refactorByTypes, report, codeToNames, codeMessagesDict)
    if ('f' in report) or ('F' in report):
        printfatals(fatalByTypes, report, codeToNames, codeMessagesDict)

if __name__ == "__main__":
    main()
