




import math
def isPrime(x):
    for i in range (2, int(math.sqrt(x)) + 1):
        if x%i == 0:
            return False
    return True
def main():
    n = eval(input("Please enter a positive integer: "))
    i = 2
    primes = 0
    twinprimes = 0
    lastprime = -1
    print("The first", n, "primes are:")
    while (primes < n):
        if isPrime(i):
            print(i, " ", end = '')
            if lastprime == i - 2:
                twinprimes = twinprimes + 1
            lastprime = i
            primes = primes + 1
        i = i + 1
    print()
    print("Amongst them there are", twinprimes, "twin primes.")
main()