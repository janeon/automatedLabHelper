







def isPrime(x):
    if x<=0:
        print("Sorry, you have to use a value greater than 0.")
    else:
        for f in range(2,x):
            if x%f==0:
                return False  
        return True
        
def main():
    print()
    print("Welcome to the Primes program!")
    print("This program calculates the first x prime numbers,")
    print("And the number of double primes among them,")
    print("When x is a number that you give me.")
    print()
    x=eval(input("How many prime numbers do you want me to find?: "))
    print()





    twincount=0
    curr=0
    prev=0
    count=0
    num=0
    print("Here you go:")
    while count < x:
        if isPrime(num)==True:
            print(num," ",end='')
            prev=curr
            curr=num
            if curr-prev==2:
                twincount=twincount+1
            num=num+1
            count=count+1
        else:
            num=num+1
    print()


    print("Amongst these there are",twincount-1,"twin primes.")
    print()

main()


