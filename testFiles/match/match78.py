





def numAndPos(E):   
    pos = 0
    least = E[0]
    secondLeast = E[1]
    if E[1] < E[0]:
        least = E[1]
        secondLeast = E[0]
        pos = 1
    for i in range(2, len(E)):
        if E[i] < least:
            secondLeast, least = least, E[i]    
            pos = i     
    return (least, pos)


def main():
    x = 1
    E = []
    error = 0
    goodInput = False
    while not goodInput:
        try:
            fileName = input("Please enter the name of the text file you would like to use >>> ")
            inputFile = open(fileName, "r")
            sequenceList = inputFile.readlines()
            protein = str(sequenceList[0])  
            protein = protein.strip("\n")   
            for line in range (1, len(sequenceList)):
                sequence = str(sequenceList[line])
                sequence = sequence.strip("\n")     
                if sequence != "":
                    for j in range(len(protein)-(len(sequence)-1)):     
                        for k in range (len(sequence)):
                            if sequence[k] != protein[k+j]:
                                error = error + 1
                        E = E + [error]
                        error = 0
                    numErr, position = numAndPos(E)
                    print("Sequence ", x, " has ", numErr, " errors at position ", position, ".", sep = "")
                    E = []
                    x = x+1     
            goodInput = True
        except IOError:
            print()
            print("Hmm, I can't seem to find that file.")
            print("Make sure we're in the right directory,")
            print("and that you're opening a text file.")
            print("Please try again.")
            print()
        except UnicodeDecodeError:
            print()
            print("Are you sure that's a text file we're looking at?")
            print("Please try again.")
            print()
        except Exception:
            print()
            print("Oops! Something went wrong.")
            print("Please try again.")
            print()

main()