





def countdracula(x):
    counter=0
    for i in range(1,x+1):
        if x%i==0:
            counter=counter+1
    if counter==2:
        return True   

def main():
    n=eval(input("How many primes? "))
    x=1
    w=0
    y=0
    print("The first",n,"prime numbers are")
    while w<n:
        x=x+1
        isPrime(x)
        if countdracula(x)==True:
            w=w+1
            if isTwin(x)==True:
                y=y+1
    print("and there are",y,"twin primes.")
    
def isPrime(x):
    counter=0
    for i in range(1,x+1):
        if x%i==0:
            counter=counter+1
    if counter==2:
        print(x,end=' ')
        
def isTwin(x):
    x=x-2
    counter=0
    for i in range(1,x+1):
        if x%i==0:
            counter=counter+1
    if counter==2:
        return True
    
main()