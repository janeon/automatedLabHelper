


def main():
        file = input("What is the name of the file you want to open?: ")
        inputfile = open(file, "r")
        protein = inputfile.readline()
        string1 = "0"
        while string1 != "":
            b=[]
            string1 = inputfile.readline()
            if string1 != "":
                for k in range(0, len(protein)-len(string1)):
                    x=-1
                    for j in range(len(string1)):
                        if string1[j] != protein[j+k]:
                            x=x+1
                    b = b + [x]
                minimum = b[0]
                minimum2 = b[1]
                minspot = 0
                if b[0]>b[1]:
                    minimum, minimum2 = minimum2, minimum
                    minspot = 1
                for i in range(2,len(b)):
                    if b[i] < minimum:
                            minimum2 = minimum
                            minimum = b[i]
                            minspot = i
                print("the number of mismatches is", minimum, end='')
                print(" and the location of the best match is", minspot)
                print()
main()