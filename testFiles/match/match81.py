






def compareSequence(sequence1, sequence2) :
    minErr = len(sequence1)
    minIndex = 0
    for i in range(0, len(sequence1)-len(sequence2)):
        count = 0
        for j in range(0, len(sequence2)):
            if sequence1[i+j]!=sequence2[j]:
                count = count + 1
        count = count - 1
        if (count < minErr):
            minErr = count
            minIndex = i
    print(minErr, "errors at position", minIndex)


    
        
            
                
                    
    
            
        
def main() :
    n = input(" which file would you like to load Mr. George Washington: ")
    inputFile = open(n,"r")
    g = inputFile.readline()
    i = 1
    for line in inputFile:
        print("Sequence",i,"has ",end="")
        compareSequence(g, line)
        i = i + 1

 
main()
        
        