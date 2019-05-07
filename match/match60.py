





def main(): 
    
    try:
        fileName = input("Enter the name of a file that contains a string s representing a protein sequence, along with some number of strings, each representing a pattern sequence: ")
        psFile = open(fileName,"r")
        p=psFile.readline() 
        sequence = 0
        for line in psFile:  
            line = line.strip()  
            mismatches = []
            for start in range((len(p)-len(line))):  
                newP = p[start:]  
                mismatch = 0
                for ch in range(len(line)):  
                    if newP[ch] != line[ch]:
                        mismatch = mismatch + 1
                mismatches.append(mismatch)
            minMismatch = min(mismatches)
            position = mismatches.index(minMismatch)
            sequence = sequence+1
            print("Sequence ", sequence, " has ", minMismatch, " errors when starting at position ", position, ".", sep='')
    except FileNotFoundError:
        print("Enter the file name of an existing file. Try adding \".txt.\"")
    except ValueError:
        print("This file does not include a protein to match to.")
    except Exception as e:
        print(type(e))
        print("You're doing it all wrong!")
    
main()