




def main():
    
    try:
        userFile = eval(input("enter the name of the text file (use .txt) "))
        inputFile = open(userFile, "r")
        
        s = inputFile.readlines()
        protein = s[0]
        
        print(protein)
        for i in range(1, len(s)):
            cursor = s[i]
            starter = 0
            minErrors = len(cursor)
            
            for j in range(len(protein)-len(cursor)):
                count = 0
                for k in range(len(cursor)-1):
                    if protein[j+k] != cursor[k]:
                        count = count + 1
                    if count < minErrors:
                        minErrors = count
                        starter = j
            print("sequence", " ", i, " ", "has", " ", count, " ", "errors at position", " ", starter, ".", sep='')
    except NameError:
        print("did you enter the name correctly? don't forget the extension!")

main()