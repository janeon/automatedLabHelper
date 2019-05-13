








    
    
def main() :
    
    n = eval(input("Enter number of primes desired:"))
    prime = 0 
    x = 2
    twin = 0 
    previousPrime = -1
    print("The first", n, "primes are:")
    while prime < n : 
        isPrime = True 
        for f in range(2,x) : 
            if x%f == 0 : 
                isPrime = False   
        if isPrime == True :
            print(x," ",end="")
            prime = prime + 1
            if x - previousPrime == 2 :
                twin = twin + 1 
            previousPrime = x 
        x = x + 1
    print()
    print("The number of twin primes within the first ", n, " primes is ", twin,".",sep="")

main()
   
