




def isPrime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False  
    return True 
            

def main():
    print("\nPrimes have twins, just like me!\n")
    n = eval(input("Enter the number of prime numbers you wish to see: "))
    print("\nThe first", n, "primes are: ")
    primes = 0 
    twins = 0
    x = 2 
    while primes<n: 
        if isPrime(x) == True:  
            print(x," ", end='') 
            primes = primes + 1 
            if isPrime(x-2):
                twins = twins + 1
        x = x + 1 
    print()
    print("Amongst these there are", twins, "twin primes.")    
main()