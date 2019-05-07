




def bestSeq (p,s):
    
    bestStart = 0
    bestMis = len(s)
    for j in range(0,len(p)-len(s)):
        mismatch = 0
        for i in range (0, len(s)):
            if s[i] != p[i+j]:
                mismatch = mismatch + 1
        if mismatch < bestMis:
            bestStart = j
            bestMis = mismatch
    return (bestMis, bestStart)
    
def main():
     x = True
     while x == True:
        try:
            fileName = input("Please enter a file name: ")
            inputFile = open(fileName,"r")
            x = False
            protein = inputFile.readline()
            sequence = inputFile.readline()
            sequenceList = inputFile.readlines()
            num = 1
            for sequence in sequenceList:
               bestMis,bestStart=bestSeq(protein[:-1],sequence[:-1])
               print("Sequence", num, "has", bestMis, "errors at position", bestStart)
               num = num+1
        except IOError:
            print("Looks like you entered the wrong file name, Try again!")
        
    
main()

