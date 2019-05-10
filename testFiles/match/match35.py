




def main():
    fileName = input("Please enter the file name of sequences:")
    openFile = open(fileName, "r")
    protein = openFile.readline()
    protein = [protein]
    
    openFile.seek(0)
    openFile.readline()
    sequences = openFile.readlines()
    
    for c in range(0, len(sequences)):
        errorlist = []
        position = []
        for pos in range(0,(len(protein[0])-len(sequences[c]))+1):
            error = 0
            for i in range(0,len(sequences[c])):
                if not sequences[c][i]==protein[0][i+pos]:
                   error = error+1
                errors = 0
                errors = error-1
            print()
            position.append(pos)
            errorlist.append(errors)
        errorlist, position = zip(*sorted(zip(errorlist, position)))
        print("Sequence", c+1, "has", errorlist[0], "errors at position", position[0], end="")


    
main()