




def main():

    guessopen = open("test.txt","r")
    check = guessopen.readline() 
    starting,error,location,len1 = 0,0,0,(len(check)-1)
    
    
    for line in range(1,10):
        guess = guessopen.readline() 
        len2 = len(guess)-1 
        n = len2 
        
        while starting <= (len1 - len2):
            for indexp in range(0,len2): 
                if check[indexp+starting] != guess[indexp]:
                    error = error + 1
            if error < n:
                n = error 
                location = starting
            error = 0    
            starting = starting + 1
        print("Sequence", line, "has", n, "errors at position", location, end='')
        print()
        location = 0
        starting = 0
        error = 0
    print()

main()
    
