






def bestSequence(S, scount):
    bestStart = 0
    mismatch = 0
    commonLetterCount = 0
    most = -1
    protein = "STTECQLKDNRAWTSLFIHTGHTECA"
    
    
    
    
    
    
    
    
    
    
    
    for x in range(len(protein)-len(S)):
        commonLetterCount = 0
        for y in range(len(S)):
            if protein[x+y] == S[y]:
                commonLetterCount = commonLetterCount + 1
        if commonLetterCount > most:
            bestStart = x
            most = commonLetterCount

    errors = len(S)- most
    print("Sequence", scount, "has", errors-1, "errors at position", bestStart)
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def main():
    S = []
    protein = "STTECQLKDNRAWTSLFIHTGHTECA"
    filename = input("Please enter your .txt file to be read: ")
    s = open(filename, "r")
    for line in s:
        S.append(line)
        print(s)
    for k in range(len(S)):
        bestSequence(S[k], k) 
        
main()           