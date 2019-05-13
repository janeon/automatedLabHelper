





def main() :
    i = 2
    numPrimes = 0
    twins = -1
    prev = 0
    n = eval(input("Enter number of primes to print: "))
    if n == 1:
        print("Here is the first prime number:")
    if n > 1:
        print("As per requested, sir, here are the first", n, "primes:")
    while numPrimes < n :        
        if isPrime(i) == True :
            if i-2 == prev : 
                twins = twins + 1
            prev = i
            numPrimes = numPrimes + 1
            print(i, " ", end='', sep='')
            i = i + 1
        if isPrime(i) == False :
            i = i + 1
    print()
    if n == 0 :
        print("You asked for nothing so that is what I gave you.")
    if n == 1 :
        print("This prime is all alone in the world.")
    else :
        if twins > 0 :
            print("Of these lovely primes,", twins, "are twin primes. How scrumptious.")            
        if twins == 0 :
            print("Of these lovely primes,", twins, "are twin primes. How unscrumptious.")

def isPrime(i):
    for h in range(2, i):
        if i%h == 0 :
            return False            
    return True

main()