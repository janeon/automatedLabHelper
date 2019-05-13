




def prime(x):

    b=0
    for f in range(2, x):
        
            
        
        if x!=2 and x%f == 0:
            b=b+1
            
        
            
            
        
            
            
            
            
    if b == 0:
       return True
    if b > 0:
        return False
     
            
        
def main():
    n = eval(input("Please tell me how many prime numbers you want:  "))

    current=1
    j=0
    omg=2
    
    for i in range (2, n*10):
        if prime(i):
            j=j+1
            if j==n :
                omg=i
    print("The first", n, "prime numbers are: ", end='')
    for v in range (2, omg+1):
        if prime(v):
            print(v, ", ", sep='', end='')
            
    print()
    print()
main()