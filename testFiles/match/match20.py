





def main():
    try:    
        file=input("Please enter text file you'd like to read!: ")
        txt = open(file,"r")
        sequence=0
        
        print()
        
            
        txt.seek(0)
        p=txt.readline()
        for line in txt:
            sequence=sequence+1
            subS=line
            beststart=0
            bestmis=len(subS)
            for i in range(0,len(p)-len(subS)):
                mismatch=0
                for j in range (0, len(subS)):
                    if subS[j]!=p[i+j]:
                        mismatch=mismatch+1
                    
                if mismatch<bestmis:
                    bestmis=mismatch
                    beststart=i
            print("Sequence", sequence, "has", bestmis-1, "errors at position", beststart)
    except IOError:
        print("Check that filename, yo.")
    except Exception as e:
        print("Something got messed up.")
        print(type(e))
        print(str(e))

main()