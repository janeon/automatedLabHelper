









def main():
    
    inputFile = open("test.txt","r")
    
    
    protein = inputFile.readline()
    protein = protein[:-1]
    
    
    maybetop = 0
    
    yestop = 0
    
    numline = 1
    
    position = 0
    
    for line in inputFile :
        line = line[:-1]
        for i in range(0,((len(protein)-1)-(len(line)-1))):
            for z in range(0,len(line)-1):
                if line[z] == protein[i+z]:
                    maybetop+=1
                if maybetop > yestop:
                    yestop = maybetop
                    position = i
            maybetop = 0

        
        if yestop == 0:
            print("Sequence",numline,"has",len(line),"errors at position 0")
        else:
            print("Sequence",numline,"has",len(line)-yestop-1,"errors at position",position)
        yestop=0
        numline+=1
            




main()

