



def isprime (n):
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for r in range (2, n):
        if (n%r) == 0:
            return False
    return True
    
def primes_up_to_n(n):  
    primes = []
    i = 1
    j = 2
    while i <= n:
        if isprime(j) == True:
            print(j,", ", sep='', end="")
            i = i+1
        j = j+1
            
def numbertwinprimes(n):
    i = 1
    j = 2
    while i <= n:
        if isprime(j) == True:
            i = i+1
        j = j+1
        twinprimes = 0
        if (i-j) == 2:
            twinprimes = twinprimes+1
            print (twinprimes)
            
def main () :
    n = eval(input("Enter a number here: "))
    if n == 0:
        print ("The first zero primes? That's a metaphysics question, you sap.")
    if n == 1:
        print("The first prime number is two, Einstein.")
    if n > 1:
        print ("The first", n, "primes are:")
        primes_up_to_n(n)
        print (" ")
        print ("Amongst these there are", numbertwinprimes(n), "twin primes.")


main ()