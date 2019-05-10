







def main():
    inputFile = open("test.txt", "r")
    s = inputFile.readlines()
    protein = s[0] 
    print("Protein = ",protein)
    for line in s[1:]:
        bestStart = 0
        min_errors = len(line)
        for t in range(len(protein)-len(line)):
            errors = 0
            for p in range(len(line)-1):
                if protein[t+p] != line[p]:
                    errors = errors + 1
            if errors < min_errors :
                min_errors = errors
                bestStart = t
        print("Sequence", line, "has", min_errors, "errors at position", bestStart,".")



main()