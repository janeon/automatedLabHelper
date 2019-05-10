






def main():
    
    fileName = input("Please enter text file you want analysed: ")
    inputFile = open(fileName,"r")
    
    protein = inputFile.readline()
    leastErrors = len(protein) + 5
    position = 0
    
    
    for marker in inputFile:
        listErrors = []
        leastErrors = len(protein) + 5
        position = 0
        for i in range(len(protein)):
            errors = 0
            for j in range(len(marker)-1):
                if i+j < len(protein):
                    if protein[i+j] != marker[j]:
                        errors = errors + 1
            if i+j < len(protein):
                listErrors.append(errors)
        for x in range(len(listErrors)):
            if listErrors[x] < leastErrors:
                leastErrors = listErrors[x]
                position = x
        print("Sequence ", marker[:-1], " has ", leastErrors, " errors at position ", position, ".", sep='')

            
    
main()