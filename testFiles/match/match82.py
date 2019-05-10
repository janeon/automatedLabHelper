





def main():
    good = False
    while(good == False):
        try:
            toOpen = input("Please input a .txt filename to be read: ")
            file = open(toOpen)
            good = True
            
        except:
            print("That filename is invalid.")
    sequences = []
    
    for line in file:    
        line = line.replace("\n","")
        sequences += [line]
    
    long = sequences[0]
    
    for i in range(1,len(sequences)):    
        currentSeq = sequences[i]
        mismatches = []
        
        for j in range(len(long) - len(currentSeq) + 1):    
            count = 0
            
            for k in range(len(currentSeq)):    
                if currentSeq[k] != long[k + j]:
                    count += 1
                    
            mismatches += [count]
            
        min = mismatches[0]
        for l in range(len(mismatches)):  
            if mismatches[l] < min:
                min = mismatches[l]
                
        print("Sequence",i,"has",min,"errors at position",mismatches.index(min))
            
    
main()