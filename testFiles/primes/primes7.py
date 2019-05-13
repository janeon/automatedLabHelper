




def isPrime(n):
    if n<2:
        return(False)
    for i in range(2,n):
         if n%i==0:
             return(False)
    else:
         return(True)


def main():
    x=eval(input("How many prime numbers can you handle? "))
    numStart=0
    z=0
    lastPrime=2
    counter=0
    print("The first",x,"primes are:")
    while z<x: 
         if isPrime(numStart)==True:
             z=z+1
             print(numStart," ",end=" ")
             lastPrime=numStart
         numStart=numStart+1
         if numStart-lastPrime==2:
             counter=counter+1
    print()         
    print("Amongst these there are",counter,"twin primes.")
main()            