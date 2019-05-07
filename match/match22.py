





def bestMatch(s1, s2) :
    bestMatch, leastErrors = 0, len(s2)
    
    for i in range(len(s1)-len(s2)) :
        errors = 0
        for j in range(len(s2)) :
            if s1[i+j] != s2[j] :
                errors = errors + 1
        if errors < leastErrors :
            bestMatch,leastErrors = i, errors
    return bestMatch, leastErrors
    
    

def main() :
    goodFile = False
    while goodFile == False :
        name = input("input the name of the file, or q to quit: ")
        if name == "q" :
            return
        try :
            t = open(name,"r")
            pattern = t.readline() 
            check = t.readlines() 
            goodFile = True
        except Exception as E :
            print("Error reading file.")
            print(E)
       
    
    try :
        for i in range(len(check)) :
            best, mis = bestMatch(pattern,check[i][:-1])
            print("Sequence ", i + 1, " has ", mis, " errors at position ", best, ".", sep='')
    except Exception as E:
        print("file seems to be in wrong format")
        print(E)

main()


