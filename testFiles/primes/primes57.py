





def isPrime(n) :
    
    resultado = bool(1)
    
    for fac in range(2,n) :
        if (n % fac == 0) :
            resultado = bool(0)
        
            
    return resultado


def main() :
    
    n = eval(input("how many primes, say you? "))
    
    primecount=0
    check = 2
    prevprime = 1
    twinprimes = 0
    
    print()
    print("well then. the first", n, "primes are")
    
    while primecount<n :
        if isPrime(check) :
            print(check, " ", sep='', end='')
            primecount = primecount + 1
            if prevprime == check - 2 :
                twinprimes = twinprimes + 1
            prevprime = check
        check = check + 1
    
    print()
    print()
    print("hey what a coincidence there are", twinprimes, "twin primes here")
    
main()