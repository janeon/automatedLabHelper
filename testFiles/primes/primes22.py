





def main():
    n = eval(input("How many primes do you want to see? "))
    p = 2
    primecount = 0
    twincount = 0
    print("The first", n, "primes are: ")
    while primecount <= n-1:
        if isPrime(p) == True:
            print (p, " ",end='')
            primecount = primecount + 1
            if isTwin(p) == True:
                twincount = twincount + 1
        p = p + 1
    print()
    print("Amongst these there are", twincount, "twin primes.")
    
def isPrime(p):
    for f in range(2, p):
        if p%f == 0:
            return False
    
    return True

def isTwin(p):
    if p < 5:
        return False
    p = p-2
    if isPrime(p) == True:
        return True
            
main()

