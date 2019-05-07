







def seq(line, protein, sequence):
    errors = len(line)
    position = 0
    for i in range(0,len(protein)-len(line)):
        y = 0
        for j in range(i, len(line) + i):
            if(line[j-i] != protein[j]):
                y = y + 1
        if y < errors:
            position = i
            errors = y
    print("Sequence", sequence, "has", errors, "errors at position", position)
    print()


def main():
    inputFile = open("test.txt", "r")
    input("Name the file you would like to use: ")
    protein = inputFile.readline()
    print(protein)
    sequence = 1
    for line in inputFile:
        line = line[:-1]
        seq(line, protein, sequence)
        sequence = sequence + 1
main()