





def isPrime(num):
    prime = True
    
    for i in range(2, num//2 + 1):
        if num%i == 0:
            prime = False
            
    return prime

def main():
    primesNeeded = eval(input("\nIf you give me a number, I shall reward you with that many primes,\nand as a bonus, I will tell you how many twin primes I have shown you: "))
    
    primesFound = 0
    mightBePrime = 2
    previousPrime = 1
    twinPrimes = 0
    
    print("\nThe first", primesNeeded, "primes are as follows:")
    
    while primesFound < primesNeeded:
        if isPrime(mightBePrime) == True:
            if mightBePrime - previousPrime == 2:
                twinPrimes += 1
                
            primesFound += 1
            previousPrime = mightBePrime
            print(mightBePrime, " ",sep='',end='')
            
        mightBePrime += 1
    
    print("\n\nAmong these there are", twinPrimes, "twin primes.")
    
main()