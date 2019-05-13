





import math

def main() :
    
    counterOne = 0
    counterTwo = 0 
    i = 2
    
    print(" ")
    print("Welcome, this program generates prime numbers.")
    n = eval(input("How many prime numbers would you like?: "))
    print(" ")
    print(" ")
    print("The first ", n, " prime numbers are:", sep="")
    
    while counterOne != n:
        
        if isPrime(i) == True:
            counterOne = counterOne +1
            print(i, end=" ")
            
            
            if isPrime(i-2) == True:
                counterTwo = counterTwo + 1
        
        
        i = i+1
    
    print()
    print("Amongst these there are ", counterTwo," twin primes.", sep="")
    print(" ")
    
def isPrime(i) :
    
    
    if int(math.sqrt(i)) == math.sqrt(i):
        return False
    
    else:
        for j in range (2,10):
            
            if i != j:
                if i % j == 0:
                    return False
                elif j == 9:
                    return True

main()

    