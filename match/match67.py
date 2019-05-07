





def main():
    try:
        filename = input("Please enter a file name: ")
        inputFile = open(filename, "r")
        s = inputFile.readline()
        a = inputFile.readline()
        b = inputFile.readline()
        c = inputFile.readline()
        d = inputFile.readline()
        e = inputFile.readline()
        f = inputFile.readline()
        sequences = [a, b, c, d, e, f]
        for k in range (6):
            minerror = 100
            
            q = sequences[k]
            for i in range (len(s)-len(q)):
                errors = 0
                for j in range (len(q)-1):
                    
                    if s[i+j] != q[j]:
                        errors = errors + 1
                        
                if errors < minerror:
                    minerror = errors
                    position = i
            print("Sequence ", k+1, " has ", minerror, " errors at position ", position, ".", sep='')
    except Exception:
        print("Enter a text file name that exists!")
main()