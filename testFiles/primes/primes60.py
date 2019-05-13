






def isPrimes(X):
        Y=0
        for i in range(2,X):
            
            Y=(X%i)
           
            if Y==0:
                return(False)
        return(True)
def main():
    X=3   
    TWINPRIMECOUNTER=0
    PRIMECOUNTER=1
    PRIMES=True
    NUMBERS=eval(input("How many primes would you like to know?: "))
    print()
    print("The first", NUMBERS, "primes are")
    print("2 ",end='')
    TEMPPREVIOUS=0
    TEMPCURRENT=0
    
    while(PRIMES):   
        if isPrimes(X):
           PRIMECOUNTER=PRIMECOUNTER+1 
           TEMPPREVIOUS=TEMPCURRENT
           TEMPCURRENT=X
           print (X, " ",end='')
           if TEMPCURRENT-TEMPPREVIOUS==2:
            TWINPRIMECOUNTER=TWINPRIMECOUNTER+1
        if PRIMECOUNTER==NUMBERS:
                PRIMES=False
        
        X=X+1
    
    print( )
    print("Their are ", TWINPRIMECOUNTER," twin primes in this set")
    
main()