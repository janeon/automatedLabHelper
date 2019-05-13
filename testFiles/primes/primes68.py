









def main() :
    
    
    
    n = -1
    while n<0:
        n = eval(input("gimme a number: "))
        if n<0:
            print("homie don't play that game! enter a POSTIVE integer!")
    
    
    
    numPrimes=0
    num = 1
    lastPrime = -1
    numTwinPrimes = 0
    
    
    while numPrimes != n:
        if isPrime(num) == True:
            numPrimes += 1
            print(num," ",end='')
            
            if num - lastPrime == 2:
                numTwinPrimes += 1
            lastPrime = num
        num += 1
    
    print("\nThere are",numTwinPrimes,"twin primes.")
    

def isPrime(x):
    if x==1:
        return False
    
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

main ()