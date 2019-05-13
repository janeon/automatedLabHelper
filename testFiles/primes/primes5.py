





def isPrime(start):
    start = start*1
    for i in range(2,start):
        if start % i == 0:
            return False
    else:
        return True

def main():
    n = eval(input("Enter a number: "))
    print("The first", n, "primes are:")
    count = 0
    twincount = 0
    prevtc = 2
    j = 2
    while count < n:
        if isPrime(j):
            if j - prevtc == 2:
                twincount = twincount + 1
            prevtc = j
            count = count + 1
            print(j, " ", sep='', end='')
        j = j + 1
    print()
    print("Amongst these there are", twincount, "twin primes")
main()