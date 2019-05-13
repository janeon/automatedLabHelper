






import math

def main() :
    print()
    n = eval(input("Type an integer: "))
    print()
    
    seriesPrime(n)
    
def seriesPrime(n) :
    print("The first", n, "primes are:")
    current = 0
    previous = 0
    twinCount = int(-1)
    primeCount = 0
    i = 2
    while primeCount < n :
        if isPrime(i)==i :
            primeCount = primeCount + 1
            previous = current
            current = i
            dif = current-previous
            if dif==2 :
                twinCount = twinCount+1
        if primeCount==n :
            print()
            print("Amongst these there are", twinCount, "twin primes.")
            print()
            return
        i = i+1

    
    
def isPrime(n) :
    div = 0
    for i in range(2,n//2+1) :
        test = n%i
        if test==0 :        
            div = div+1
    if div>0 :
        return(int(0))                        
    if div==0 and n>1 :     
        print(n, " ", end="")
        return(int(n))
    
main()