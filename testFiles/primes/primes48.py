






def isPrime(x) :
    if x==2 :
        return True
    else:
        for i in range (2, x) :
            if x%i==0 :
                return False
            elif i==x-1 :
                return True
                
def main():
    print("This program finds the first n prime numbers and the number")
    print("of twin primes in that range, provided that you, fair user")
    print("enter a number (n) for us to search.")
    x=eval(input("Enter a number: "))
    print()
    print("The first", x, "primes are:")
    count=0
    currTest=2
    prevPrime=2
    twinPrimes=0
    while (count < x ) :
        if isPrime(currTest)==True :
            print(currTest, " ", end="")
            count= count +1
            if currTest==prevPrime+2:
                twinPrimes=twinPrimes+1
            currTest, prevPrime =currTest+1, currTest  
        else :
            currTest=currTest+1
    print()
    print("Among these, there are", twinPrimes, "twin primes.")    

main()