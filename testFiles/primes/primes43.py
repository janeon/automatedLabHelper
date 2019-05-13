






def main() :
    
    twinPrimes = 0
    count=0
    o=2
    n=2

    def isPrime(n) :
        for i in range(2,n) :
            if n%i == 0 :
                return False
        return True
    
    numPrimes = eval(input("Hi User. Please enter an integer: "))
    print("The first",numPrimes,"primes are:")
    print()
    
    while count < numPrimes :
        if isPrime(n) is True :
            count = count + 1
            print(n, " ", end='')
            
            if n-o == 2 :
                twinPrimes = twinPrimes+1
            o=n
        n=n+1
    
    print()
    print("Within these there are", twinPrimes, "twin primes.")
    print()
    
    
    
main()