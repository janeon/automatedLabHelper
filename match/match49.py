





def main():
    x = input("Input a file to be read:")
    F = open(x, "r")
    L = []
    for line in F:
        L.append(line[:-1])
    protein = L[0]
    patterns = L[1:]
    print("Protein:", protein)
    print("Patterns:", patterns)
    print()
    print()
    
    for pattern in patterns:
        save = []
        position = 0
        for letter in protein:
            mismatch = 0
            attempt = protein[position:(position + len(pattern))]
            position = position +1
            for x in range(len(pattern)):
                if len(attempt) == len(pattern):
                    if pattern[x] != attempt[x]:
                        mismatch = mismatch + 1
                
            save.append(mismatch)
        del save[(len(save)-(len(pattern)-1)):]
        pos = (save.index(min(save)))
        val = min(save)
        print()
        
        print("Sequence", pattern, "has", val, "errors at position", pos)
                

main()
