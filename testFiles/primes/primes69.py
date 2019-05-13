





def isPrime(x):
	for f in range(2, x) :
		if x % f == 0:
			return False
	return True
			
def main():
    n = eval(input("How many prime numbers would you like me to list? "))
    print("The first",n,"primes are:")
    numPrimes = 0
    numTwins = 0
    previousPrime = 2
    x = 3
    print("2  ",end="")
    while numPrimes < n :	
    		if isPrime(x):
    			print(x," ",end="")
    			numPrimes = numPrimes + 1
    			if x - previousPrime == 2:
    				numTwins = numTwins + 1
    			previousPrime = x
    		x = x + 1 
    		
    print()
    print("Amongst these there are",numTwins,"twin primes.")

main()
