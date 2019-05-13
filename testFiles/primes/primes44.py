







def isPrime(n):
    twinprimes = 0
    current = 2
    previous = current
    count = 0
    while count < n:
        isPrime = True
        divisor = 2
        while divisor < current:
                if current%divisor == 0 and isPrime:
                    isPrime = False
                divisor = divisor + 1
        if isPrime:
            print(current, end = " ")
            count = count + 1
            if current-previous == 2:
                twinprimes = twinprimes + 1
            previous = current
        current = current + 1
    print()
    print("the number of twin primes in this set:", twinprimes)


def main():
    n = eval(input("Give number of primes desired: "))
    print("The first", n, "primes are:")
    isPrime(n)
        

main()
