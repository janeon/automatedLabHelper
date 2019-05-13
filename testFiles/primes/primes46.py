





import math

def main():
    n = eval(input("How many primes should I print out?"))
    for i in range (1,n+1):
        x = 2
        isPrime(x)
        while isPrime(x) == True:
            print(x)
        x = x+1

def isPrime(x):
    for f in range(1, x):
        if x%f==0:
            return False
        else:
            return True

main()

