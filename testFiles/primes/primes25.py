





def isPrime(x) :
    for f in range(2, x) :
        if (x % f) == False:
            return False
    
    return True

def main() :
    x = eval(input("Enter the number of primes to be computed: "))
    print("The first", x, "primes are:")
    count = 2
    numPrimes = 0
    holdPrime = 1
    twinPrimes = 0
    
    while numPrimes < x :
        if isPrime(count) == True :
            print(count, "", end='')
            numPrimes = numPrimes + 1
            if (count - 2) == holdPrime :
                twinPrimes = twinPrimes + 1
            holdPrime = count
        count = count + 1
    
    print()
    print("Amongst these there are", twinPrimes, "twin primes.")

main()