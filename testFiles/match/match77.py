





while True:
    try:
        fileName = input("Please enter the name of the file you would like to use: ")
        file = open(fileName,"r")
        prot = file.readline()
        break
    except:
        print("The file you chose does not seem to be working. Please try again.")

def main():
    sequence = 0
    
    for line in file:
        tempsucc = 0
        temppos = 0
        permsucc = 0
        permpos = 0
        tempprot = prot
        
        for i in range(len(prot)):
            
            for j in range(len(prot)):
                tempprot = prot + " "*(len(line))
                
                if (j+i) < len(tempprot) and j < len(line)-1:
                    
                    if tempprot[j+i] == line[j]:
                        tempsucc = tempsucc + 1
                    
                    if tempsucc > permsucc:
                        permsucc = tempsucc
                        permpos = temppos
            temppos = temppos + 1
            tempsucc = 0
        tempprot = " " + tempprot
        sequence = sequence + 1
        print("Sequence",sequence,"has",((len(line)-permsucc-1)),"errors at position",permpos)
    return

main()
