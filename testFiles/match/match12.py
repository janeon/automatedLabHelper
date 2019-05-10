





def main():
    print("Time to play a matching game.")
    
    name="test.txt"
    file=open(name,"r")
    
    sequence=file.readline()    
    length=len(sequence)
    
    
    
    
    
    
    file.seek(length)           
    time=1
    for line in file:
        
        
        term=len(line)
        
        dif=length-term
        
        zed=0
        for r in range(dif):
            
            if sequence[r]==line[0]:
                agent(sequence,line,r,time)
                zed=zed+1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        if zed==0:
            print("Sequence",time,"has",term,"errors at position 0.")
        time += 1

def agent(sequence,line,r,timer):     
    length=len(sequence)
    term=len(line)
    dif=length-term
    match=[]
    check=[]
    terminus=0
    while terminus==0:
        for l in range(term):
            if sequence[r+l]==line[l]:
                match.append("yes")
            else:
                match.append("no")
            matchL=len(match)
            
        error=0
        for j in range(matchL):
            if match[j]=="no":
                error=error+1
            check.append([error])
        L=len(check)
        
        terminus=1
        
        
        
    print("Sequence",timer,"has",error,"errors at position ",end='')
    print(r,".",sep='')
    
    
main()