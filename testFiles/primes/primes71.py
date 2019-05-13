





def isPrime(x):
    
    for f in range (2,x):
        if x%f==0:
           return False
    return True
    
    
    
def twinPrimes(r):
    
    for j in range (3,r):
        if isPrime(r) and isPrime((r-2)):
            return True
        else:
           return False

def main():
    print()
    n=eval(input("Give me a number of primes you would like to see and I shall list the primes and tell you how many twin primes are among them. "))
    numPrimes=0
    numTwins=0
    i=2 
        
    
    print()
    print("The first", n, "primes are: ")
    
    while numPrimes<n:
        if isPrime(i):
            print(i," ", end='') 
            numPrimes=numPrimes+1
        if twinPrimes(i):
            numTwins=numTwins+1
        i=i+1 
        
    print ()
    print ("Amongst these there are", numTwins, "twin primes.")    
    print ()
main()


