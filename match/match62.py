







def match(p, m) :
    best, error, count = 0, len(m), 0
    
    
    
    for i in range(len(p) - len(m)) :
        test = p[i:len(m)+i-1]
        
        
        
        for j in range(len(test)) :
            if test[j] != m[j] :
                count = count+1
        if count < error :
            best = i
            error = count
        count = 0
    return best, error

def main() :
    goodInput = False
    while not goodInput :
        try :
            fileName = input("Please enter the file that is to be read: ")
            inputFile = open(fileName, "r")
            proteinSeq = inputFile.readline()
            markers = inputFile.readlines()
            
            
            for i in range(0, len(markers)) :
                best, error = match(proteinSeq, markers[i])
                print("Sequence ", i+1, " has ", error, " errors at position ", best, ".", sep='')
            goodInput = True
        
        except IOError:
            print("Sorry, that file isn't in this folder.")

main()



