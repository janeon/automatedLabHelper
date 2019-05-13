







def isPrime(x):
    for f in range(2, x):
        if x%f == 0:
            return False
    if x <= 1:
        return False
    return True

def main():
    print()
    print("This program will print out prime numbers and twin primes.")
    n = eval(input("Please enter the number of prime numbers you wish to see: "))
    primecounter = 0
    twincounter = 0
    lastprime = 2
    i = 2
    while primecounter < n:
        if isPrime(i) == True:
            primecounter = primecounter + 1
            print(i, end=" ")
            if i - lastprime == 2:
                twincounter = twincounter + 1
            lastprime = i
            i = i+1
        else:
            i = i+1
    print()
    print("Amongst these there are", twincounter, "twin primes.")
    
main()


