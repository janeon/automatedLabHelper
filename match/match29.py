





def main() :
    
    filename = input("Please enter the filename followed by \".txt\":")
    try:
        
        inputFile = open(filename,"r")
        s = inputFile.readline()
        s = s[0:len(s)-1]
        sequenceCounter = 0
        
        for line in inputFile:
            
            p = line[0:len(line)-1]
            sequenceCounter = sequenceCounter+1 
            
            errors = compare(s,p, sequenceCounter)
    except FileNotFoundError:
        print("Could not find given file.  Please enter a filename within the directory that ends in \".txt\"")
    except:
        print("Unknown error, please try again.")

def compare(s,p,sequenceCounter) :
    
    
    dif = len(s) - len(p)
    errors = []
    counter = 0
    
    
    if s != "" and p != "":
        
        for i in range(0,dif+1) :
            
            
            temp = s[i:i+len(p)]
            
            for j in range (0,len(p)) :
                
                if p[j] != temp[j] :
                    counter = counter + 1
            
            errors.append(counter)
            counter = 0
        
        
        for i in range (0,len(errors)-1) :
            if errors[i] == min(errors):
                print("Sequence ", sequenceCounter, " has ", min(errors), " errors at position ", i, ".", sep='')
                break
    else:
        print("Error: Empty protein sequence.")

main()