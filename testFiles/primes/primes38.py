





def main():
    n = eval(input("How many prime numbers would you like? "))
    def isPrime(n):
        for f in range(2, n):
            if n % f == 0:
                return False
        return True
    primes = []
    j = 2
    while len (primes) < n:
        if isPrime(j) == True:
            primes.append (j) 
        j = j+1
    print(primes)
    twinprimes = 0
    for k in range(n-1):
        if primes[k+1] == primes[k] + 2:
            twinprimes = twinprimes + 1
    print("Amongst these there are", twinprimes, "twin primes.")
    isPrime(n)
   
   
main()