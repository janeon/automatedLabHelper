





def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

def firstNPrimes(n):
    l=[2]
    counter=1
    number=3
    while counter < n:
        if isPrime(number):    
            counter += 1
            l.append(number)
        number += 1
    return l

def main():
    n=eval(input("Please input the number of primes you would like to print out: "))
    l = firstNPrimes(n)
    numTwinPrimes=0
    for i in range(0, n-1):
        if l[i] == l[i+1]-2:
            numTwinPrimes += 1
    print("The first", n, "primes are:")
    print(l)
    print("Amonst these there are", numTwinPrimes, "twin primes.")
    
main()