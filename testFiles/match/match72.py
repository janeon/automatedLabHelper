






def line_counter(inputFile) : 
    list_lines = []
    for line in inputFile :
        temp = line[0]
        list_lines.append(temp)
    num_lines = len(list_lines)
    return num_lines

def main() :
    print("Welcome to Acme Optimal Pattern Matcher.")
    promptLoop = False 
    while promptLoop == False : 
        try :
            fileName = input("Please enter a text file: ")
            inputFile = open(fileName, "r")
            promptLoop = True 
        except IOError :
            print()
            print("That file does not seem to exist.")

    num_lines = line_counter(inputFile)
    inputFile.seek(0)
    P = inputFile.readline()

    for i in range(num_lines - 1) :
        S = inputFile.readline()
        S = S[0:len(S) - 1]
        
        errors = []; start = 0; error_count = 0 
        num_checks_with_P = len(P) - len(S)
        
        for start in range(num_checks_with_P + 1) : 
            for j in range(len(S)) :
                if S[j] != P[start + j] :
                    error_count += 1
            
            errors.append(error_count)
            
            error_count = 0
        
        best_match = 0
        for k in range(len(errors) - 1) : 
            if errors[k + 1] < errors[k] and errors[k + 1] < errors[best_match]:  
                best_match = k+1     
        
        print("Sequence ", i + 1, " has ", errors[best_match], " errors at position ", best_match, ".", sep='')

main()
    
                