





def main():
    isValid = False
    while not isValid:
        try:
            filename = input("Please enter a txt file: ")
            inputFile = open(filename, "r")
            isValid = True
        except:
            print ("That is not a valid txt file. ")
    s = inputFile.readline()
    s = s[:-1]
    rest = inputFile.readlines()
    for i in range(len(rest)):
        if rest[i][-1]=="\n":
            rest[i] = rest[i][:-1]
            
    for i in range(len(rest)):
        leastMismatches = len(s) + 1
        if len(rest[i]) > len(s):
            print("Sequence", i + 1, "is too long.")
        elif len(rest[i]) == 0:
            print("Sequence", i + 1, "has no characters.")
        else:
            for j in range(len(s) - len(rest[i]) + 1):
                nrMismatches = 0
                for k in range(len(rest[i])):
                    if rest[i][k] != s[j+k]:
                        nrMismatches = nrMismatches+1
                if nrMismatches < leastMismatches:
                    leastMismatches = nrMismatches
                    bestPosition = j 
            print("Sequence ", i + 1, " has ", leastMismatches, " errors at position ", bestPosition, ".", sep = '')
               
main()