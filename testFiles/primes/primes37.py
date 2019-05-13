





def main() :
    print()
    n=eval(input("How many prime numbers would you like? "))
    print()
    i=1
    PRIME_CNT=0
    TWIN=0
    
    
    def isPrime(x) :
        i=1
        if x<=1 :
            return False
        elif x==2 :
            return True
        else :
            while i<x-1 :
                i=i+1
                if x%i==0 :
                    return False
        return True

   
    print("The first", n, "primes are:")
    while n > PRIME_CNT :
        i=i+1
        j=i-2
        if isPrime(i)==True :
            print(i, end=" ")
            PRIME_CNT=PRIME_CNT+1
            if isPrime(j) :
                TWIN=TWIN+1
                
    print()
    print("Amongst these there are", TWIN, "twin primes.")
    print()
    
main()
