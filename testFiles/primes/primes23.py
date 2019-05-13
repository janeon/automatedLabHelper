





def isPrime(x):
    for i in range (2,x):
        if x%i==0:
            return False
    return True

def isTwin(x):
    if x<5:
        return False
    x=x-2
    if isPrime(x)==True:
        return True
    

            
def main ():
    n=eval(input("How many primes would you like generated:"))
    countprimes=0
    counttwins=0
    x=2
    previous=0
    print("The first",n,"primes are:")
    while n > countprimes:
        if isPrime(x)==True:
            countprimes=countprimes+1
            print (x," ",end='')
            if isTwin(x)==True:
                counttwins=counttwins+1
        x=x+1
    print()
    print("Amongst these there are",counttwins,"twin primes.")
            
main()


