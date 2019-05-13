





def main():
    print("Welcome to the awesome prime calculator")
    n = eval(input("input number of primes: "))
    x = 2
    print("The first ",n," primes are :\n",x," ",end='',sep='')
    twin = 0
    tCount = 0
    while n > 1:
        x = 1+x
        if isPrime(x) == True:
            print(x,"",end='')
            n = n-1
            if twin == x-2 :
                tCount = tCount+1
            twin = x
    
    print()
    print(tCount,"of these are twin primes!")

def isPrime(x):
    remainder = 1
    for f in range(2,x-1):
        if remainder != 0:
            remainder = x%f
    return remainder != 0



main()