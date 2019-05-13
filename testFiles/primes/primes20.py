













def isPrime(n) :
    for i in range(2, n//2 + 1) :
        if n%i == 0 :
            return False
        if n < 2 :
            return False
    return True

def main() :
    n = eval(input("How many prime numbers do you want computed: "))
    prime = 0
    twinprimes = 0
    z = 2
    print("The first", n, "prime numbers are:")
    while prime < n :
        if isPrime(z) :
            print(z, end = ' ')
            prime = prime + 1
            if isPrime(z-2) :
                twinprimes = twinprimes + 1
        z = z + 1
    print()
    print("Amongst these there are",twinprimes - 2, "twin primes")
main()