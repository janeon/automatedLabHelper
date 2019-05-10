






def main():
    
    try:
        userFile = eval(input("\n Please enter the file you would like to read, surrounded by quotation marks, in a <file>.txt format: "))
        inputFile = open(userFile, "r")
        s = inputFile.readlines()
        protein = s[0]
        print(protein)
        for i in range(1, len(s)):
            marker = s[i]
            bestStart = 0
            minErrors = len(marker)
            for j in range(len(protein)-len(marker)):
                errors = 0
                for k in range(len(marker)-1):
                    if protein[j+k] != marker[k]:
                        errors = errors + 1
                    if errors < minErrors:
                        minErrors = errors
                        bestStart = j
            print("Sequence", " ", i, " ", "has", " ", errors, " ", "errors at position", " ", bestStart, ".", sep='')
    except NameError:
        print("\n Are you sure you entered the file name correctly? Remember quotes around <yourfile>.txt ! \n")

main()