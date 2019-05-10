





def removeNewLine(markerStrings):
    for l in range(len(markerStrings)):
        temp = markerStrings[l]
        markerStrings[l] = temp[:-1]
def main() :
    errorCounterList = []
    currentMarker = 0
    positionList = []
    inputFile = open("test.txt", "r")
    protein = inputFile.readline()
    markerStrings = inputFile.readlines()
    removeNewLine(markerStrings)


    for line in range(len(markerStrings)) : 
        
        
        positionList = positionList + [0]
        errorCounterList = errorCounterList + [len(markerStrings[currentMarker])] 
        
        for starter in range( len(protein) - len(markerStrings[currentMarker]) ): 
            reuseErrorCounter = [0]
            for i in range(len(markerStrings[currentMarker])) :
                if protein[starter + i] != markerStrings[currentMarker][i] :
                    reuseErrorCounter[0] = reuseErrorCounter[0] + 1 
                    
            if reuseErrorCounter[0] < errorCounterList[currentMarker]:
                errorCounterList[currentMarker] = reuseErrorCounter[0]
                positionList[currentMarker] = [starter]
        currentMarker = currentMarker + 1
        
    for j in range (currentMarker) :
        x = 0
        if positionList[j] != 0:
            x = str(positionList[j])[1:-1] 
        
        
        print ("Sequence", j + 1 , "has", errorCounterList[j], "errors at position", x)
    
    
        




main()