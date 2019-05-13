






def main():
    n = eval(input("How many primes would you like to generate?")) 
    numPrimesGen = 0        
    x = 2                   
    twin = 0
    prevPrime =-1
    
    while numPrimesGen < n:         
        isPrime = True              
        for f in range(2, x):       
            if x%f == 0:            
                isPrime = False         
        if isPrime == True:             
            print( x, " ", end="")       
            numPrimesGen = numPrimesGen + 1     
            if x-prevPrime == 2:
                twin=twin+1
            prevPrime=x
        x = x + 1
    print("Amongst these first", n, "primes there are", twin, "twin primes.")
main()
    