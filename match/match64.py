




def bestseq(subseqS, protoP):
    bestStart = 0 
    bestMis = len(subseqS) 
    print()
    for start in range(0, len(protoP) - len(subseqS)):
        mismatch = 0
        for i in range (0, len(subseqS)):
            if subseqS[i] != protoP[i+start]:
                mismatch = mismatch + 1
        if mismatch < bestMis:
            bestStart = start
            bestMis = mismatch
    print("beststart=", bestStart)
    print("bestMis=", bestMis)
    print()
    

def main():
    inputFile = open("test.txt","r")
    x = inputFile.readlines() 
    protoP = x[0] 
    print(protoP)
    
    for line in x[1:]: 
        line = line.strip()
        print(line[:], end="")
        subseqS = line 
        bestseq(subseqS, protoP) 
        
    
    
main()