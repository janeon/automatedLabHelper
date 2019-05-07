







def main():
    
    
    file = open(input("Type a file name to evaluate: "), "r")
    
    protein = file.readline()
    markers = file.readlines()
    protein = protein[:-1]
    numMarkers = len(markers)
    
    bestMatch(protein, markers, numMarkers)
    
def bestMatch(protein, markers, numMarkers) :
    
    for i in range(numMarkers):  
        
        marker = markers[i]
        marker = marker[:-1]
        
        errorList = []
        
        for position in range(len(protein) - len(marker)) :     
            proteinVersion = protein[position:]
            errors = 0
            
            for char in range(len(marker)):         
                if proteinVersion[char] != marker[char] :
                    errors = errors + 1             
                    
            errorList.append(errors)    
            
        bestError = min(errorList)    
        bestPos = errorList.index(bestError)    
                            
        print("Sequence", i+1, "has", bestError, "errors at position", bestPos)
    
main()
    
