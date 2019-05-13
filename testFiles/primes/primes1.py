





import math
def isPrime(x):
    counter=0
    for f in range(2,x):
        if x%f==0:
            counter=counter+1    
    if counter==0:
        return True
    else:
        return False


def main():
    n=eval(input("Please enter number n: "))
    found=0
    start=2
    twin=0
    d1=1
    print("The first",n,"primes are:")
    while found<n:
        if isPrime(start):
            d2=start
        if d2==d1+2:
            twin=twin+1
        if isPrime(start):
            d1=start
            print(start,end=' ')
            found=found+1
        start=start+1
    print()
    print("Amongst these there are",twin,"twin primes")

  
main()