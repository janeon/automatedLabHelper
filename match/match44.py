









def getBestMatch(P,S): 
    bestStart = 0   
    bestMis = len(P)    
    for i in range(0,len(P)-len(S)): 
                                     
                                     

        mismatch = 0
        for j in range(0,len(S)-1):                             
            if S[j] != P[j + i]: 
                mismatch = mismatch + 1
        if mismatch < bestMis:
            bestStart = i  
            bestMis = mismatch 
    return(bestMis,bestStart)

def main():

    a = input("What file would you like to use? ")
    v = open(a,"r")
    P = v.readline()    
    cnt = 1
    for line in v:
        x,y = getBestMatch(P, line)
        print("Sequence", cnt, "has", x, "errors at position", y)
        cnt = cnt + 1
main()