





def main():
    print()
    fyle = input("Enter a file name: ")
    inputFile = open(fyle,"r")
    s = inputFile.readline()
    p = []
    for i in range(0,6):
        q = inputFile.readline()
        p.append(q)
    for a in range(len(p)): 
        print(p[a],end='')
        errors = []
        for n in range(0,len(s)-len(p[a])): 
            mismatches = -1
            for b in range(len(p[a])): 
                if s[b+n] != p[a][b]: 
                    mismatches += 1 
            errors.append(mismatches)
        min1 = errors[0]
        for n in range(len(errors)):
            if errors[n] < min1:
                min1 = errors[n]
                index = n
        print("Sequence",a+1, "has", min1, "errors at position", index)

main()