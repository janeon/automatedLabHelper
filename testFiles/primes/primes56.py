





def isPrime(x):
    for i in range(2,x//2):
        if (x%i) == 0:
            return False
        if x == i:
            return True


def main():
    n = eval(input("?"))
    primes = [2]
    if n == 1:
        print(primes)
    else:
        x = 3
        while len(primes) < n:
            if isPrime(x)==True:
                primes.append(x)
            x = x+1
        print(primes)

main()
