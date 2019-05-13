





def isPrime(x):
    factors = 0
    for f in range(1, x+1):
        if x%f == 0:
            factors = factors + 1
    if factors == 2:
        return(True)
    
def isTwin(x):
    x = x - 2
    factors = 0
    for f in range(1, x+1):
        if x%f == 0:
            factors = factors + 1
    if factors == 2:
        return(True)
    
def main():
    primes = 0
    twins = 0
    number = 1
    n = eval(input("How many primes? "))
    print("The first", n, "primes are: ")
    while primes < n:
        number = number + 1
        if isPrime(number) == True:
            print(number, " ", sep='', end='')
            primes = primes + 1
            if isTwin(number) == True:
                twins = twins + 1
    print()
    print("Among these there are ", twins, " twin primes.", sep='')
    
main()
    

