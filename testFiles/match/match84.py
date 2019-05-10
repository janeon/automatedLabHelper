





def main():




    
    
    done = False
    while not done:
        FileName = input("What file would you like to check: ")
        try:
            inputFile = open(FileName, "r")
            P = inputFile.readline()
            Q = inputFile.readlines()
            done = True
        except:
            print("There is no such file please try to type another one")
        
    
    
    
    for line in Q:
        S = []
        
        for i in range (0, (len(P)-len(line))):
            Mis = 0
            
            for j in range (0, (len(line )-1)):
                        
                if line[j] != P[i+j]:
                    Mis = Mis + 1
            S.append(Mis)
            
            
            
        
            counter = -1
            count = 0
            smallest = S[0]
            for x in S:
                counter = counter + 1
                if x < smallest:
                    smallest = x
                    count = counter

                
        print ("for sequence:", line, end = '')
            
        print ("Best Mixmatch site at",count)
        print ("Where there are", smallest, "mismatches")
            



        


main()
