





def main():
    worked = False 
    while worked==False: 
        fileName = input("Input file name for match.py. Make sure the first line of the text file is the protein sequence. ") 
        try:
            file = open(fileName,"r")
            lines = 0 
            for line in file: 
                lines = lines+1
            file.seek(0) 
            protein = file.readline() 
            if len(protein)-1==0:
                print("The protein has a length of zero")
                exit()
            for sequenceNumber in range(1,lines): 
                listA = [] 
                sequence = file.readline() 
                for positionStart in range(0,len(protein)-len(sequence)+1): 
                    mismatches = 0
                    for positionNow in range(positionStart,positionStart + len(sequence)-1): 
                        if protein[positionNow]!=sequence[positionNow-positionStart]: 
                            mismatches = mismatches + 1
                    listA = listA + [mismatches] 
                for i in range(0,len(sequence)-1): 
                    if listA.count(i)!=0:
                        positionAnswer = listA.index(i)
                        mismatches = i
                        break
                    else:
                        positionAnswer = 0
                        mismatches = len(sequence)-1
                print("There are", mismatches, "mismatches at position", positionAnswer,"for sequence", sequenceNumber,".") 
                worked = True
        except IOError as err:
            print("Please make sure the file exists and is in the same folder as match.py:")
        
main()