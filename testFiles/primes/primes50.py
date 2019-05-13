






def isPrime(x):
    isPrime = True
    counter = 2
    while (isPrime==True and counter<=x//2+1):
        if x%counter==0:
            isPrime = False
        counter = counter +1
    return isPrime


def main():
    n = eval(input("Please enter a number: "))
    x = 2
    primeNums = 0
    twin = 0
    print("The first", n, "primes are:")
    print("2", "", end ='')
    while primeNums < n - 1:
        if isPrime(x)==True:
            primeNums = primeNums + 1
            print(x, "", end = '')
            if isPrime(x-2)==True and (x-2)!=1:
                twin = twin+1
        x = x + 1
        
    print()
    print("There are", twin, "twin primes." )

                   
main()
    
    
    