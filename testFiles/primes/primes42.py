





def main() :
    n = eval(input("How many primes do you want me to search? "))
    if n == 0:
        print ("The first 0 primes is... what..?")
    else:
        print ("The first", n,  "primes are...")
        counter = 2
        prime1 = -1
        prime2 = -1
        twinprimes = 0
        x = 1
        
        while (x == 1) :
            
            if isPrime(counter) == 1:
                print (counter, " ", sep="", end="")
                prime2 = prime1
                prime1 = counter
                
                if (prime1 - prime2) == 2:
                    twinprimes = twinprimes + 1
                
                counter = counter + 1
                n = n-1
                
            else:
                counter = counter + 1
                
            if n == 0:
                x = 0
                
        print()
        print ("Amongst these there are", twinprimes, "twin primes")
    
    
def isPrime(counter) :
    
    for j in range (2, counter):
        
        if counter % j == 0:
            return 0
    
    return 1

main()
                