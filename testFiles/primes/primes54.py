





def prime(n):
    
    if n== 0:
        return "There are no primes."
    
    if n==1:
        return "2"
    
    if n>=2:
        primes=[]
        check=2
        while len(primes)<n:
            if isPrime(check):
                primes.append(check)
            
            check=check+1
                    
        return primes
    
        
def isPrime(x):
    for i in range(2,x):
        if x % i==0:
            return False
    return True
        
        

def main():
    
    n=eval(input("Enter the number of primes you would like to see: "))
    
    if n==1:
        print("The first prime is: ")
    else:
        print("The first", n, "primes are: ")
    
    primes=prime(n)
    print(primes)
    
    
    twinprime=0
    if n !=0:
        for i in range(len(primes)-1):
            difference=primes[i]-primes[i+1]
            if difference== -2:
                twinprime=twinprime+1
            

        
    print("Amoungst these there are", twinprime, "twinprimes.")
                
main()