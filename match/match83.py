






fileName=input("What file would you like me to look at? ")
inputFile=open(fileName,"r")
    
    

def main():
    
    protein=inputFile.readline() 
    print("We will be matching marker sequences with the protein sequence", protein)
    sequence = 0
    for line in inputFile:
        sequence = sequence + 1
        marker=len(line)-1
        
        lineTests=len(protein)-marker - 1 
                                         
        print ("Sequence", sequence, end='')
        errors = len(line) 
        minIndex = 0 
        for i in range(lineTests): 
            lineMatch=0
            for j in range (marker):
                proteinPos=i+j
                if line[j]==protein[proteinPos]:
                    lineMatch=lineMatch+1
            if marker - lineMatch < errors:
                
                
                errors=marker-lineMatch
                minIndex=i
                
        print(" has", errors, "errors at position", minIndex)
    
main()


