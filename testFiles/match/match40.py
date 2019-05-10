





def bestSequence(S, P):
    bestStart = 0
    bestMis = len(S)
    for start in range (0, len(P)-len(S)):
        mismatch = 0
        for j in range (start, start+len(S)):
            if S[j-start] != P[j]:
               mismatch = mismatch + 1
        if mismatch < bestMis:
            bestStart = start
            bestMis = mismatch
    return bestMis, bestStart
    
def main():
    try: 
        inputFile = open(input("Please input a file: "), "r")
        
        P = inputFile.readline()
        print("Your protein sequence is", P, end='')
        for line in inputFile:
            S = inputFile.readline()
            best = bestSequence(S[:-1], P[:-1])
            print("Sequence", line, "has", best[0], "errors at position", best[1])
    except:
        print("Are you sure the file you put in exists? Maybe you put in the wrong type of file. Anyway I can't read this...sorry")

main()
