







def main():
    goodInput = False
    while not goodInput:
        try:
            filename = input("Please enter a text file name (eg. test.txt): ")
            inputFile = open(filename, "r")
            goodInput = True
        except:
            print("That file does not seem to exist.")
            print("Check your spelling and try again.")
    s = inputFile.readline()
    for j in range(1, 7):
        line = inputFile.readline()
        n = 0
        mismatch = 0
        bestmis = 0
        beststart = 0
        while n + len(line) <= len(s):
            for i in range(len(line)-1):    
                if s[i+n] != line[i]:
                    mismatch = mismatch + 1
            if n == 0:
                bestmis = mismatch
            else:
                if mismatch < bestmis:      
                    bestmis = mismatch
                    beststart = n
            mismatch = 0
            n = n+1                         
        print("Sequence", j, "has", bestmis, "errors at position", beststart)
            
        
main()