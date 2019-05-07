







def main():
    try:
        n=input("What text file would you like to use?")
        inputFile = open(n, "r")
        p=inputFile.readline() 
        psequence = 0 
        
        for line in inputFile: 
            bestStart=0
            bestMismatch=len(p)
            for start in range (0, (len(p)-len(line))+1): 
                mismatch=0
                for i in range (0, len(line)-1): 
                    if line[i] != p[i+start]: 
                        mismatch=mismatch+1
                if mismatch<bestMismatch: 
                    bestStart=start
                    bestMismatch=mismatch
            psequence = psequence + 1
            print("Sequence ", psequence, " has ", bestMismatch, " errors at position ", bestStart, ".", sep="")
    except IOError:
        print()
        print("Please enter a valid file.")
        print()
main()