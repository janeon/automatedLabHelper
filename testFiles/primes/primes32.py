





def isPrime(x) : 
    for i in range (2,x) :
        if x == 2 :
            return True
        if x%(i)==0 :
            return False
    return True 

def twin(x,p) : 
    for i in range (3,x) :
        if (x+1)-p == 2 :
            return True

def main () :
   
    n= eval(input("How many prime numbers would you like? "))
    x=2 
    y=0 
    p=0 
    t=0 

    print ("The first", n, "primes are: ")
    while y < n: 
       
        if isPrime(x):
            
            y=y+1
            print (x, " ", end= "")
        p=x
        x=x+1
       
        if twin(x,p) :
            t=t+1 
    print ("Of these, there are", t, "twin primes")
   
main ()


