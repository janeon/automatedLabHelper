def bestmatch(s,p):
    beststart = 0
    bestmismatch = len(s)
    for i in range(0,(len(p)-len(s))):
        mismatch = 0
        for j in range(0, len(s)):
            if p[i+j] != s[j]:
                mismatch = mismatch + 1
        if mismatch < bestmismatch:
            bestmismatch = mismatch
            beststart = i
    return beststart, bestmismatch
            
def main():
    x = True
    while x:
        try:
            filename = input("Please enter your <text>.txt file to input: ")
            inputFile = open(filename,"r")
            pline = inputFile.readline()
            sline = inputFile.readlines()
            snumb = 0
            for sequence in (sline):
                (s,p) = bestmatch(sequence[:-1], pline[:-1])
                snumb = snumb + 1
                print("Sequence", snumb, "has", p, "errors at position", s,".")
            for line in (inputFile):
        
                print(line)
            x = False    
        except:
            print("That file doesn't appear to work. Try another .txt file")
           
main()   