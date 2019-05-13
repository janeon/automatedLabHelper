




def aigis():
    print("You have chosen to run the Prime Calculator And Analysis program.")
    print("My designation is Aigis.")
    n = eval(input("Please enter the number n of prime integers to be calculated: "))
    print("Very well. Processing...")
    isprime(n)
    
    
    
def isprime(n):
    print("The first",n,"prime numbers are:")
    c=1
    m=0
    twin=0
    while n>m:
        if c==1:
            print(end='')
        elif 1<c<4:
            print(c," ",sep='',end='')
            m=m+1
        elif c==5:
            print(c," ",sep='',end='')
            m=m+1
            twin=twin+1
        elif c==7:
            print(c," ",sep='',end='')
            m=m+1
            twin=twin+1
        elif (c%2)==0 or c%3==0 or c%7==0 or c%5==0:
            print("",sep='',end='')
        else :
            print(c," ",sep='',end='')
            if (c-2)%2==0 or (c-2)%3==0 or (c-2)%5==0 or (c-2)%7==0:
                twin=twin
            else:
                twin=twin+1
            m=m+1
        c=c+1
    print()
    print("In addition, this set contains", twin,"sets of twin primes.")
    print("Function completed.")
    print("Deactivating...")
    
aigis()