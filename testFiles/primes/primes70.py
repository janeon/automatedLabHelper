





def isPrime(x):
    y = True
    for i in range(2,x):
        if (x%i ==0):
            y = False
    return y
    
            
def main():
    twinPrimeCounter = 0
    L = [] 
    f = eval(input("How many primes to print out? "))
    x = 0
    primeCounter = 0
    while primeCounter < f:
        x = x + 1
        isPrime(x)
        if isPrime(x) == False:
            pass
        else:
            primeCounter = primeCounter + 1
            L.append(x)
    for x in range(1,f):
        if L[x] - L[x-1] == 2: 
            twinPrimeCounter = twinPrimeCounter + 1 
    print("The first ", f, "primes are: ")
    print(L)
    print("Among these are ", twinPrimeCounter, "twin primes.") 
                
main() 