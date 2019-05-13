





def isPrime(n, prime = 1) :
    for i in range(n-1,1,-1) :
        if n%i == 0 :
            prime = 0
    return prime

def twinCounter(k) : 
    twin = k - 2
    twinBool = isPrime(twin)
    if twinBool == 1 :
        return 1
    else :
        return 0 
        
def printPrimes(n, primeCount = 0, k=2, twinTest = 0, twinCount = 0) :
    print("The first",n, "primes are:")
    while k < k+1 :  
        if primeCount == n:
            break
        else:
            prime = isPrime(k)
            if prime == 1 :
                print(k, " ", sep='', end = '')
                primeCount += 1
                
                
                if k > 3 : 
                    twinCount += twinCounter(k)
                k +=1
            else :
                k += 1
    print()
    print("Amongst these there are", twinCount, "twin primes.")
 
def main() :
    print()
    n = eval(input("Please give me a natural number: "))
    
    if n > 0 and type(n) == int :
        printPrimes(n)
        print()
        
    else :
        print("That wasn't a natural number!")
        
main()
        