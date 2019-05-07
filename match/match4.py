















def bestMatch(protein,marker):
    bestPosition=0
    bestMismatch=len(protein)+1
    for i in range (len(protein)) :
        currPosition=i
        currMismatch=0
        for j in range (len(marker)) :
            try :
                if protein[i+j]!=marker[j] :
                    currMismatch= currMismatch+1
            except IndexError :
                currMismatch=currMismatch+len(marker[j:])
        if currMismatch < bestMismatch:
            bestPosition=currPosition
            bestMismatch=currMismatch
    return [bestMismatch, bestPosition]
        
def main() :
    filename=input("Please enter the name of the file you'd like to check: ")
    try:
        inputFile= open(filename,"r")
    except:
        print("Something went wrong with your input file! Try again!")
        print("Hint: The file you want read might not be in the correct directory!")
    protein= inputFile.readline()
    markerList= []
    markerList=markerList+inputFile.readlines()
    for i in range (len(markerList)) :
        markerList[i]=(markerList[i])[:-1]
        marker=markerList[i]
        markerList[i]=bestMatch(protein,marker)
        print("Sequence", i+1, "has", markerList[i][0], "errors at position", markerList[i][1])
main()