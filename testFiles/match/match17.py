





def main():
    giventxt = open("test.txt","r")
    protsequence = giventxt.readline()
    blah=giventxt.readlines() 
    
    
    count=1
    for k in blah: 
        matches = 0
        for i in range((len(protsequence)-1)-(len(k)-1)): 
            counter = 0
            for j in range(len(k)-1): 
                if protsequence[i+j]==k[j]: 
                    counter=counter+1 
            if counter>matches:
                matches=counter
                bestposition=i
                numerrors=len(k)-1-counter
        if matches==0:
            bestposition=0
            numerrors=len(k)-1
        print("Sequence ",count," has ",numerrors," errors at position ",bestposition,".",sep='')
        count=count+1
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
main()