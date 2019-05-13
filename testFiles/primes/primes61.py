





import math

def main():   
    n = eval(input("Please insert number of primes you would like: "))
    primes = 0 
    test = 1 
    twins = -1 
    lastprime = 0
    y = 0
    print("The first ", n," prime numbers are: ")
    while primes < n:
        test = test + 1
        x = 0
        if IsPrime(test) == True:
            primes = primes + 1
            y = test - lastprime
            if y == 2:
                twins = twins + 1
            print(test, " ", end='')
            lastprime = test
    print()
    print("There are ", twins, " twin primes.")

def IsPrime(test):
    for i in range(2,test):
        x = test%i
        if x == 0:
            return False
    else:
        return True

main()

