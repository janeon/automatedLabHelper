




def main():

    n=input("Enter the name of the file you would like to scan: ")  


    inputFile= open(n, "r")     
    
    sequence=inputFile.readline()       
    littleSequences= inputFile.readlines()      

    mismatchlist=[]                         
    for i in range(len(littleSequences)):
        mismatchlist=mismatchlist+ [[]*len(littleSequences)]
    
    for j in range(len(littleSequences)):               
        ls=littleSequences[j]
        for i in range(len(sequence)-len(ls)-1):        
            count=0
            for x in range(i, i+len(ls)-1):             
                if sequence[x] != ls[x-i]:              
                    count=count+1                       
            
            mismatchlist[j]=mismatchlist[j]+[count]     
     
    
    minList=[]                                          
    PosList=[]                                          
    for i in range(len(mismatchlist)):
        currentList= mismatchlist[i]
        min=currentList[0]
        minPos=0
        for num in range(len(currentList)):
            if currentList[num] < min:
                min=currentList[num]
                minPos=num
        minList=minList+[min]
        PosList=PosList+[minPos]

    
    for i in range(len(littleSequences)):
        print("Sequence", i+1, "has", minList[i], "errors at position", PosList[i])
        
    
    
main()