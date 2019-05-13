




def main():
    
    n = eval(input("Please enter the number of primes you would like!: "))
    numPrimes = 0
    i = 1
    Primes = [ ]
    while numPrimes < n:
        if isPrime(i):
            numPrimes = numPrimes + 1
            Primes.append(i)
            i = i+1
        else:
            i = i+1

    
    twinPrimes = 0
    
    for j in range(1, n):
        if Primes[j] - Primes[(j-1)] == 2:
            twinPrimes = twinPrimes + 1 
    print("The first", n, "Primes are: ", Primes)
    print("There are", twinPrimes, "twin primes")

def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x%i == 0:
            return False
    return True 
main()
