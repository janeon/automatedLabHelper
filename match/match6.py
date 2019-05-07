






def match(inPutFile):
    protein = inPutFile.readline()
    line = 0
    for sequence in inPutFile:
        bestStart = 0
        start = 0
        mismatch = []
        line = line + 1
        bestMis = len(sequence)
        for possibleStart in range(0,(len(protein) - len(sequence))):
            mismatch = mismatch + [0]
            for i in range (0, (len(sequence) - 1)):
                if sequence[i]!=protein[i+ possibleStart]:
                    mismatch[start] = mismatch[start] + 1       
            if mismatch[start] < bestMis:
                bestMis = mismatch[start]
                bestStart = start
            start = start + 1
        print ("Sequence", line,  "has", bestMis, "errors at position", bestStart)

def main():
    inPutFile = open("test.txt", "r")
    match(inPutFile)
        
main()