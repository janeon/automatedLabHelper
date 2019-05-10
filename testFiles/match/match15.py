






def check(a,b): 
    maximum = 0
    errors = len(b)
    position = 0
    for i in range(len(a)-len(b)):
        COUNTER = 0
        for j in range(len(b)):
            if a[i+j] == b[j]:
                COUNTER = COUNTER + 1
        if COUNTER > maximum:
            maximum = COUNTER
            position = i
            errors = len(b)-COUNTER
    return(position,errors)


def main():
    print()
    valid = False
    while valid == False:
        try:
            openfile = input("Please enter a text file: ")
            inputFile = open(openfile,"r")
            valid = True
        except:
            print()
            print("Enter valid file type.")
            print()
    print()
    a = list(inputFile.readline())
    a = a[:-1]
    i = 0
    for line in inputFile: 
        i = i + 1
        b = line[:-1]
        pos, err = check(a,b)
        print("Sequence ",i," has ",err," errors at position ",pos,".",sep='')
    print()
    
main()


