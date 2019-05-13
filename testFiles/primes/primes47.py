





def isPrime(x):
    for f in range(2, x):
        if (x%f)==0:
            return False
    return True

def main():
    n=eval(input("Please enter a number of primes to print:"))
    counter=0
    x=2
    xprev=x
    twinprime=0
    print("The first", n, "primes are:")
    while(counter<n):
        if isPrime(x):
            counter = counter+1
            print(x, "", end='')
            if (x-xprev)==2:
                twinprime=twinprime+1
            xprev=x
        x=x+1
    print()
    print("Among these primes there are", twinprime, "twin primes.")
main()
        