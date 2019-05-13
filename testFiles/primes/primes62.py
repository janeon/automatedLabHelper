






def isPrime(x):
    prime = True
    for j in range (2,x):
        if x%j == 0:
            prime = False
    return prime

def main():
    n = eval(input("Pretty please enter a number: "))
    primeCount = 0
    twinCount = 0
    x = 2
    lastX = 1
    done = False
    while not done:
        prime = isPrime(x)
        if prime == True:
            print (x, " ", sep = "", end = "")
            primeCount = primeCount + 1
            if primeCount < n:
                done = False
            else:
                done = True
            if x-lastX == 2:
                twinCount = twinCount + 1
            lastX = x
        x = x+1
    print("There are ", twinCount, "twin primes")
    
main()