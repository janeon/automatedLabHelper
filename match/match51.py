






def bestMatch(s, p):
    bestStart = 0
    bestMis = len(s)
    for j in range(0, len(p)-len(s)):
        mismatch = 0
        for i in range(0,len(s)):
            if (s[i]) != (p[i+j]):
                mismatch = mismatch + 1
        if mismatch < bestMis:
            bestStart = j
            bestMis = mismatch
    return (bestMis, bestStart)
        
    
def main():
    Bool = True
    while Bool == True: 
        try:
            inputFile = open(input("Enter a file name: "), "r")
            Bool = False
            protein = inputFile.readline()
            sequenceList = inputFile.readlines()
            sequenceNum = 0
            for sequence in sequenceList:
                (bestMis, bestStart) = bestMatch(sequence[:-1], protein[:-1])
                sequenceNum = sequenceNum + 1
                print ("Sequence",sequenceNum,"has",bestMis,"errors at position",bestStart)
        except:
            print("Something went wrong!")
main()