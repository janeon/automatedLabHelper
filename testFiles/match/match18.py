






def bestSequence(subseqS,protP):
    bestStart = 0 
    bestMis = len(subseqS) 
    print()
    for start in range(0, (len(protP)-len(subseqS))): 
        mismatch= 0                                              
        for i in range(0,len(subseqS)): 
            if subseqS[i] != protP[i+start]: 
                                             
                mismatch = mismatch +1
        if mismatch < bestMis: 
                           
            bestStart = start
            bestMis = mismatch
    print("Above sequence has", bestMis,"errors at position", bestStart)
    print()
    


def main():
    inputFile = open("test.txt","r") 
    x = inputFile.readlines() 
    protP = x[0] 
    print("The protein is", protP) 
    for line in x[1:]: 
        line = line.strip()
        print(line[:], end="") 
        subseqS = line 
        bestSequence(subseqS,protP) 
    
    
main()
    