





def main():
    try:
        file=input("Please select a text file: ")
        txt=open(file,"r")
        print(txt.readline())
        txt.seek(0)
        p=txt.readline()
        count=0
        for line in txt:        
            subS=line
            count=count+1
            bestStart=0
            bestMis=len(subS)
            for i in range(0,len(p)-len(subS)):
                mismatch=0
                for j in range(0, len(subS)):
                    if subS[j]!=p[i+j]:
                        mismatch=mismatch+1
                if mismatch<bestMis:
                    bestMis=mismatch
                    bestStart=i    
            print("Sequence ",count," has ",bestMis-1," errors at position ",bestStart,".","\n",sep='',end='')
    except:
        print("Not a text file in the directory. Try again.")
main()