






def main() :
    try :
        print()
        print("Welcome to the Sequence Tester!")
        print()
        print("This program matches the sequences you give it together")
        print("and tells you where the ideal placement for minimum")
        print("mistakes is.")
        print()
        fileName = input("What file would you like me to open? : ")
        print()
        inputFile = open(fileName, "r")
        test = inputFile.readline()
        seq = inputFile.readlines()
        mistake = 0
        minMistake = len(test)
        idealSpot = 0
        seqcount = 1
        for sequence in seq :
            for i in range(0, len(test) - len(sequence)):
                for j in range(0, len(sequence) - 1) :
                    if sequence[j] != test[i + j] :
                        mistake = mistake +1
                if mistake < minMistake :
                    minMistake = mistake
                    idealSpot = i
                mistake = 0
            print("Sequence ", seqcount, " has ", minMistake, " errors at ", idealSpot, ".", sep='')
            seqcount = seqcount + 1
            minMistake = len(test)
    except :
        print("Sorry, something broke.")
        print("Are you sure you typed a real file name?")

main()


