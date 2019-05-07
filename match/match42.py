



def main() :
    filename = input("What file would you like to open? ")
    inputFile = open(filename,"r")

    try:
        linelist = inputFile.readlines()
        numlines = len(linelist) 
        protP = linelist[0] 
        print()
        print ("This program has searched the string", protP,"and located the best match for each of the", len(linelist)-1, "substrings.")
        print()
        for j in range (1, numlines): 
            subseqS = linelist[j]
            beststart = 0
            bestMis = len(subseqS)
            for s in range (0, (len(protP)-len(subseqS))): 
                mismatch = 0
                for c in range (0, len(subseqS)): 
                    if subseqS[c] != protP[s+c]: 
                        mismatch = mismatch+1
                if mismatch < bestMis: 
                    bestMis = mismatch-1
                    beststart = s
            print ("Substring", j, ":",subseqS," This sequence fits best at position", beststart, "but has", bestMis, "errors.")
        print ()
            
    except LookupError:
        print ("File not found.")
main()