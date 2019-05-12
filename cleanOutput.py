""" cleanOutput.py
    post-processes pylint self.warnings and self.errors into more readable, less redundant/terrifying messages
"""
from pylint import epylint
import sys
import regexChecks
ticks = 45

class cleanOutput:
    def __init__(self, fname, report, originalCode, options):
        self.conventions = {}
        self.warnings = {}
        self.errors = {}
        self.refactors = {}
        self.fatals = {}
        self.conventionByTypes = {} # {code : [line numbers]} where code is of type C
        self.warningByTypes = {} # {code : [line numbers]} where code is of type W
        self.errorByTypes = {}
        self.refactorByTypes = {}
        self.fatalByTypes = {}
        self.fname = fname
        self.report = report
        self.originalCode = originalCode
        self.options = options

    def printconventions(self, codeToNames, codeMessagesDict):
        print()
        print((' '*ticks)+"CONVENTION CHECKS"+(' '*ticks))
        for code in self.conventionByTypes:
            lines = self.conventionByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" convention reminders \n\t located on line(s) ", end="")
                for line in lines:
                    print(line, end=", ")
                print("\n")
                if 'C' in self.report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

    def printwarnings(self, codeToNames, codeMessagesDict):
        print()
        print((' '*ticks)+"WARNING  CHECKS"+(' '*ticks))
        for code in self.warningByTypes:
            lines = self.warningByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" self.warnings \n\t located on line(s) ", end="")
                for line in lines:
                    print(line, end=", ")
                print("\n")
                if 'W' in self.report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

    def printerrors(self, codeToNames, codeMessagesDict):
        print()
        print((' '*ticks)+"ERROR  CHECKS"+(' '*ticks))
        if self.errorByTypes["E0001"] != []:
            print("Found 1", "\""+codeToNames["E0001"]+ "\" self.errors \n\t located on line ", end="")
            l = self.errorByTypes["E0001"]
            print(l[0])
            print('\t',"Note: While you have a syntax error, output from other code checks won't show up.\n")

            match = regexChecks.check(self.originalCode[int(l[0])-1])
            print('\t',codeMessagesDict["E0001"][0],'\t',match)
        else:
            for code in self.errorByTypes:
                lines = self.errorByTypes[code]
                if lines:
                    print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" self.errors \n\t located on line(s) ", end="")
                    match = ""
                    for line in lines:
                        ### save in case
                        #if code == "E0001":
                            #match = regexChecks.check(originalCode[int(line)-1])
                        print(line, end=", ")
                    print("\n")
                    if 'E' in self.report:
                        msgs = codeMessagesDict[code]
                        for msg in msgs:
                            ### save in case
                            #print('\t',msg,'\t',match)
                            print('\t',msg)

    def printrefactors(self, codeToNames, codeMessagesDict):
        print()
        print((' '*ticks)+"REFACTOR CHECKS"+(' '*ticks))
        for code in self.refactorByTypes:
            lines = self.refactorByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" self.refactors \n\t located on line(s) ", end="")
                for line in lines:
                    print(line, end=", ")
                print("\n")
                if 'R' in self.report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

    def printfatals(self, codeToNames, codeMessagesDict):
        print()
        print((' '*ticks)+"FATAL CHECKS"+(' '*ticks))
        for code in self.fatalByTypes:
            lines = self.fatalByTypes[code]
            if lines:
                print("Found", str(len(lines)), "\""+codeToNames[code]+ "\" fatal checks \n\t located on line(s) ", end="")
                for line in lines:
                    print(line, end=", ")
                print("\n")
                if 'F' in self.report:
                    msgs = codeMessagesDict[code]
                    for msg in msgs:
                        print('\t',msg)

    def buildCode_MessagePairs(self, codes):
        for i in range (0,25):
            codeMessage = codes[i].split(": ")
            self.conventions[codeMessage[0]] = codeMessage[1]
        # print(self.conventions)
        for i in range (25,84):
            codeMessage = codes[i].split(": ")
            self.errors[codeMessage[0]] = codeMessage[1]
        # print(self.errors)

        for i in range (84,92):
            codeMessage = codes[i].split(": ")
            self.fatals[codeMessage[0]] = codeMessage[1]

        for i in range (102,117):
            codeMessage = codes[i].split(": ")
            self.refactors[codeMessage[0]] = codeMessage[1]
        # print(self.refactors)

        for i in range (117,186):
            codeMessage = codes[i].split(": ")
            self.warnings[codeMessage[0]] = codeMessage[1]


    def buildCode_LineListPairs(self):
        for code in self.conventions:
            self.conventionByTypes[code] = []
        for code in self.warnings:
            self.warningByTypes[code] = []
        for code in self.errors:
            self.errorByTypes[code] = []
        for code in self.refactors:
            self.refactorByTypes[code] = []
        for code in self.fatals:
            self.fatalByTypes[code] = []
        # print(conventionByTypes)
        ### end of processing convention messages
        # Test prints self.conventions dictionary
        # for convention in self.conventions:
        #     print(convention, self.conventions[convention])
    def clean(self):
        # ICRWEF
        pylint_stdout, pylint_stderr = epylint.py_run(self.fname + ' ' + self.options, return_std=True)
        # TODO: Not sure what the following line does yet, need to test out on more example files
        # print(pylint_stderr.getvalue())
        output = pylint_stdout.getvalue()
        output = output.split(self.fname)
        messages = {} # {line : message}
        for line in range (1,len(output)):
            warning = output[line].split(": ")
            lineNum = warning[0]
            messages[lineNum[1:]] = warning[1]
        codes = list(open("errorCodes.txt","r"))

        self.buildCode_MessagePairs(codes) # {code:message}
        self.buildCode_LineListPairs()

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
                self.conventionByTypes[code].append(line)
            elif type == "warning":
                self.warningByTypes[code].append(line)
            elif type == "error":
                self.errorByTypes[code].append(line)
            elif type == "refactor":
                self.refactorByTypes[code].append(line)
            elif type == "fatal":
                self.fatalByTypes[code].append(line)
            if code in codeMessagesDict:
                codeMessagesDict[code].append("L" + line + ": " + warningMessage)
            else:
                codeMessagesDict[code] = ["L" + line + ": "+ warningMessage]

        # handling input from report:
        if ('c' in self.report) or ('C' in self.report):
            self.printconventions(codeToNames, codeMessagesDict)
        if ('r' in self.report) or ('R' in self.report):
            self.printrefactors(codeToNames, codeMessagesDict)
        if ('w' in self.report) or ('W' in self.report):
            self.printwarnings(codeToNames, codeMessagesDict)
        if ('e' in self.report) or ('E' in self.report) or (self.errorByTypes["E0001"] != []):
            self.printerrors(codeToNames, codeMessagesDict)
        if ('f' in self.report) or ('F' in self.report):
            self.printfatals(codeToNames, codeMessagesDict)

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
    out = cleanOutput(fname, report, originalCode, options)
    out.clean()

if __name__ == "__main__":
    main()
