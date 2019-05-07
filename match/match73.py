



def main():
    
    filename=input("What file would you like to open? Enter its name here. ")
    
    inputFile=open(filename, "r")
    print()
    
    print ("Your protein is",inputFile.readline())
    
    print("These are the  possible marker sequences:")
    for line in inputFile:
        print(line, end='')
    print()    
    inputFile.seek(0)
    
    proteinsequence=inputFile.readline()
    
    for line in inputFile:
        marker=line
        print ("For marker ", marker, sep='',end='')
        bestStart,bestMis=findSequence(proteinsequence,marker)
        print("Best start: postion ", bestStart, "; largest number of errors: ", bestMis-1, sep="")

def findSequence(proteinsequence,marker):
    proteinlength=len(proteinsequence)
    markerlength=len(marker)
    bestStart=0
    bestMis=markerlength
    for i in range(0,(proteinlength-markerlength)):
        error=0
        for j in range(0,len(marker)):
            if marker[j]!=proteinsequence[j+i]:
                error=error+1
        if error<bestMis: 
            bestStart=i
            bestMis = error
    return bestStart,bestMis

main()

  