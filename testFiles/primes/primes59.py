





def main():
    n = eval(input("enter a number: "))
    nprimes = 0
    i = 0
    tprimes = 0
    print("The first", n, "prime numbers are:")
    while nprimes < n:
        i = i + 1
        if isPrime(i):
            print(i, end=' ')
            nprimes = nprimes + 1
            if nprimes < n and isPrime(i + 2):
                tprimes = tprimes + 1
    print()
    print("The number of twin primes is ", tprimes)

def isPrime(p):
    if p == 1:
        return False
    for x in range(2,p):
        if p % x == 0:
            return False
    return True
    
main()