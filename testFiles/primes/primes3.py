






def isPrime(x):
    for f in range (2, x):
        if x%f==0:
            return False
    else:
        return True

def main():
    n= eval(input("please enter the number of primes you want: "))
    primes=0
    x=3
    lastPrime=2
    twinCount=0
    print ("The first", n, "primes are: ")
    print("2", " ",end='')
    while primes < (n-1):
        if isPrime(x):
            print(x, " ", end='')
            primes=primes+1
            if x-lastPrime==2:
                twinCount=twinCount + 1
            lastPrime=x
            
        x=x+1
    print()
    print("Amongst these there are", twinCount, "twin primes.")
main()
