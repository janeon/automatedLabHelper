





def main():
    n = eval(input("Pick a number of primes: "))
    if n == 0:
        print("There are no primes in this range")
    else:
        print()
        print("The first", n, "primes are: ")
        isPrime(n)
        print()
        
def isPrime(n):
    i = 2
    if prime(i) == True:
        print(i, end=' ')
        i = i + 1
    numPrimes = 1
    numTwinPrimes = 0
    while numPrimes < n:
        if prime(i) == True:
            numPrimes = numPrimes + 1
            print(i, end=' ')
        i = i + 2
        if prime(i) == True and prime(i + 2) == True and numPrimes < n-1:
            numTwinPrimes = numTwinPrimes + 1
    print()
    if n == 1 or n == 2:
        print("Amongst these there are", numTwinPrimes, "twin primes")
    else:
        print("Amongst these there are", numTwinPrimes + 1, "twin primes")
            
def prime(n):
    if n == 2:
        return True
    for x in range(3,n//2,2):
        if n % x == 0 :
            return False
    return True

main()