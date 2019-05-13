








def isPrime(n): 
    x=0
    a=2
    t=0
    z=2
    while x<n: 
        prime=1
        for i in range(2,a):
            if a%i==0:
                prime=0
        if prime==1:
            print(a,"",end='')           
            x=x+1
            if a==z+2: 
                t=t+1 
            z=a
        a=a+1
    print()
    print("There are",t,"twin primes.")
        
        

def main():
    n=eval(input("Please enter an integer: "))
    print("The first",n,"prime numbers are")
    isPrime(n)
main()


