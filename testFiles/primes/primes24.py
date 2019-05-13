





def isPrime(x):
    for y in range(x-1,1,-1):
        if x%y==0:
            return False
    return True

def isTwin(x):
    x=x-2
    for y in range(x-1,1,-1):
        if x%y==0:
            return False
    return True

def main():
    n=eval(input("How many primes would you like?: "))
    print("The first",n,"primes are:")
    primes=0
    twinprimes=0
    x=1
    while primes < n:
        x=x+1
        if isPrime(x)==True:
            print(x," ",sep="",end="")
            primes=primes+1
            if isTwin(x)==True:
                twinprimes=twinprimes+1
    print()
    print("There are",twinprimes-2,"twin primes in the first",n,"primes.")
    
main()