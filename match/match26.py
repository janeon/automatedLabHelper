







def main():
    print()
    print("Welcome to my protein matching program!")
    goodInput = False
    while not goodInput:
        try:
            print()
            n=input("Which text file would me to use?     ")
            inputFile = open(n, "r")
            
            
            p=inputFile.readline()
            
            
            seq = 0
            
            
            print()
            for pattern in inputFile: 
                
                bStart=0
                bMismatch=len(p)
                
                for start in range (0,(len(p)-len(pattern))+1): 
                    mismatch=0
                    
                    for i in range (0,len(pattern)-1):
                        
                        if pattern[i]!=p[i+start]: 
                            mismatch=mismatch+1
                            
                    if mismatch<bMismatch: 
                        bStart=start
                        bMismatch=mismatch
                        
                seq = seq + 1
                
                print("Sequence ", seq, " has ", bMismatch, " errors at position ", bStart, ".", sep="")
            print()
            goodInput=True
        except IOError:
            print()
            print("You have entered an improper file. Please try again.")
            print()
        except Exception as e:
            print()
            print("Whatever you did, it was wrong. Do it differently!")
            print()
            print(type(e))
            print(str(e))
main()