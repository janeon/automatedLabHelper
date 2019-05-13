





n = eval(input("How many prime numbers would you like to calculate? "))
counter = 0

def isPrime(x):
    for i in range(2, ((x//2) + 2)):
        if x%i == 0:
            return False
    return True

def compilePrime():
    print("The first",n,"prime numbers are: 2, ",end="")
    counter = 1
    twins = 0
    current = 0
    j = 1
    while counter < n:
        j = j + 1
        if (isPrime(j)):
            print(j,", ",sep="",end="")
            counter = counter + 1
            previous = current
            current = j
            if previous == (current - 2):
                twins = twins + 1
    print()
    print("Of these primes, there are",twins,"pairs of twin primes.")

compilePrime()