





def checker(targetSequence,checkerSequence):
    
    leastMismatch=len(targetSequence)
    bestPosition=0
    positionCounter=-1
    
    
    
    for i in range(len(targetSequence)-(len(checkerSequence))):
        mismatchCounter=-1
        positionCounter=positionCounter+1
        for j in range( len(checkerSequence)):
            
            
            
            if not targetSequence[j+positionCounter]==checkerSequence[j]:
                mismatchCounter=mismatchCounter+1
            
        
        if mismatchCounter<leastMismatch:
            leastMismatch=mismatchCounter
            bestPosition=positionCounter
        
    return(leastMismatch,bestPosition)
    

def main():
    sequenceNumber=0
    goodInput=True
    while goodInput:
        try:
            fileName = input("What file would you like to use?: ")
            print (fileName)
            inputFile = open(fileName,"r")
            goodInput=False
        except:
            print("I'm Sorry, i dont have that file. Try again")
    targetSequence= inputFile.readline()
    print ("This is your target protein sequence")
    print(targetSequence)
    print("thats an... interesting protein sequence")
    print("Sorry, thats the inner bio student talking. Down to business")
    print()
    for line in inputFile:
        sequenceNumber=sequenceNumber+1
        checkerSequence=line
        
        leastMismatch,bestPosition=checker(targetSequence,checkerSequence)
        
        print("sequence",sequenceNumber, checkerSequence,end='')
        print("has",leastMismatch,"errors at position",bestPosition,)
        print()
    
main()