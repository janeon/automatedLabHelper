





def main():
    filename = input("What file would you like to use? ")
    inputFile = open(filename,"r")
    
    print("Your protein is",inputFile.readline(),end='')
    print()
    print("These are the sequences you have to check:")
    for line in inputFile:
        print(line,end='')
    print()
    inputFile.seek(0)
    protein=inputFile.readline()
    for line in inputFile:
        seqLine = line 
        print(seqLine,end='')
        bestStart,bestMis = bestSequence(seqLine,protein)
        print("Best start position:",bestStart,", Number of errors at this site:",bestMis-1)
    print()
    
def bestSequence(subseqS,protP):
    bestStart = 0
    bestMis = len(subseqS)
    for start in range(0,len(protP)-len(subseqS)):
        mismatch = 0
        for i in range(0,len(subseqS)):
            if subseqS[i] != protP[i+start]:
                mismatch=mismatch+1
        if mismatch < bestMis:
            bestStart=start
            bestMis=mismatch
    return bestStart,bestMis
    
    
    
main()

