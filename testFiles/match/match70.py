





def main():
    file = input("Give me a file name: ")
    inputFile = open(file, "r")
   
    s = inputFile.readline()
    
    sequence = []
    for v in range (6):                     
        a = inputFile.readline()
        list= [a]
        sequence = sequence + list
    
    for m in range(6):  
        k = sequence[m]
        smallesterrors = len(s) + 10
        bestposition = 0
        for i in range(0,len(s)-len(k)): 
            errors = 0
            for j in range(len(k)-2):   
                if s[i+j] != k[j%len(k):(j+1)%len(k)]:
                    errors = errors + 1
            if errors < smallesterrors: 
                smallesterrors = errors
                bestposition = i
        print("Sequence", m+1, "has",smallesterrors, "errors at position", bestposition)
    
main()