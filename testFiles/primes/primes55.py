








def isPrime(x):
    z=0
    for i in range (2,x):
        if x%i==0:
            z=z+1
    if z==0:
        return True
    else:
        return False


def main():
    lastPrime=2
    twins=0 
    x=1
    numOfPrimes=0
    prime= eval(input("How many prime numbers do you want? " ))
    while (numOfPrimes<prime):
        x=x+1
        if isPrime(x)==True:
            y=x-lastPrime
            if y==2:
                twins=twins+1
            numOfPrimes=numOfPrimes+1
            print(x, " ", end='')
            lastPrime=x
    print("There are ", twins, "twin primes.")            
    
        
main()    