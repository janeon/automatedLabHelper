





def main():
    goodInput = False
    while not goodInput:        
        File = input("Enter file name: ")
        try:
            File = open(File,"r")
            File = File.readlines()
            goodInput = True
        except:
            print("Invalid file name")

    for i in range(len(File)-1):    
        p = File[0]
        p = p[:-1]
        mismatch = []
        s = File[i+1]
        if s[-1] == "\n":       
            s = s[:-1]
        for j in range(len(p)): 
            tally = 0
            p = p + "0"
            for k in range(len(s)):     
                if p[k+j] != s[k]:
                    tally = tally + 1
            mismatch = mismatch + [tally]
        found = False
        d = 0
        pos = []
        while not found:        
            for j in range(len(mismatch)):
                if mismatch[j] == d:
                    found = True
                    pos = pos + [j]
            d = d+1
        print("Sequence ",i+1," has ",mismatch[pos[0]]," errors at position ",pos[0],sep='')























main()