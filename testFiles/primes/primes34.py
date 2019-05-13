





def twinPrime(x):
    z = x - 2
    isPrime(z)
    if isPrime(z) == True:
        return True

def isPrime(x):
    z = 0
    for f in range(2, x):
        if x%f == 0:
            z = z + 1
    if z == 0:
        return True     
    if z != 0:
        return False       

def main():
    n = eval(input("How many primes would you like to see?: "))
    x = 0
    y = 2
    z = 0
    print()
    print("The first", n, "primes are:")
    while x != n:
        isPrime(y)
        if isPrime(y) == True:
            print(y, "", end='')
            twinPrime(y)
            if twinPrime(y) == True:
                z = z + 1
            x = x + 1
            y = y + 1
        if isPrime(y) == False:
            y = y + 1
    print()
    print("Amongst these there are", z - 2, "twin primes")

main()