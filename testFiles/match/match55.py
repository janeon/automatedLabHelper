




def Check(p,s):
    lenP=len(p)-1
    lenS=len(s)-1
    Match=[]
    for i in range (0,(lenP-lenS)):
        m=0
        for j in range(i,(i+lenS)):
            if p[j]==s[j-i]:
                m=m+1
        Match=Match+[m]
            
    L=Largest(Match)
    mismatches=lenS-L
    for i in range (len(Match)):
        if Match[i]==L:
            bestMatchSite=i
            break    
    return (mismatches,bestMatchSite)

def Largest(Match):
    for i in Match:
        count=0
        for j in Match:
            if i<j:
                count=count+1
        if count==0:
            return(i)
            break
        
def main():
    filename=input("Please enter the file you would like to load: ")
    file=open(filename,"r")
    P=file.readline()

    S=file.readlines()
    Mismatches=[]
    BestMatchSite=[]
    for i in range(0,(len(S))):
        string= S[i]
        (mm,bms)=Check(P,string)
        Mismatches=Mismatches+[mm]
        BestMatchSite=BestMatchSite+[bms]
    
    for j in range (0,len(S)):
        print("Sequence ",j+1," has ",Mismatches[j]," errors at position ",BestMatchSite[j],".",sep='')

    
    
main()


