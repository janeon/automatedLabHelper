





def main():
    
    lines = loadlist()
    for i in range(1, len(lines)):
        errors = []
        for n in range(0, len(lines[0])-len(lines[i])):
            errors.append(0)
            for t in range(0, len(lines[i])):
                if lines[i][t] != lines[0][n + t]:
                    errors[n] = errors[n] + 1
        minimum = errors[0]
        minindex = 0
        for x in range(1, len(errors)):
            if errors[x] < minimum:
                minimum = errors[x]
                minindex = x
        minimum = minimum - 1
        print("Sequence ",i, " has ", minimum, " errors at position ",minindex,".", sep='')

def loadlist():
    
    
    mylist  = []
    
    inputFile = open("test.txt","r")
    for line in inputFile:
        mylist.append(line)
    return mylist

main()
