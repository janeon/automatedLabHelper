





def isPrime(z):
    for y in range (z-1,1,-1):
        if z%y==0:
            return False
    return True

def isTwin(z):
    z=z-2
    for y in range (z-1,1,-1):
        if z%y==0:
            return False
    return True
  
def main():
    n=eval(input("Please give the number of primes you would like: "))
    primecounter=0
    twinprimes=0
    z=1
    while primecounter<n:
        z=z+1
        if isPrime(z)==True:
            print(z," ", sep='',end='')
            primecounter=primecounter+1
            if isTwin(z)==True:
                twinprimes=twinprimes+1
    print()
    print ("Among the first",n,"primes, there are",twinprimes-2,"twin primes.")
    
 
main()
    
