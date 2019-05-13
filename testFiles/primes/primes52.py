


















def isprime(x): 
    
    z = 0
    for dive in range(2,x):
        if x % dive == 0 :
            z = z + 1
    if z == 0:
        return True
    else:
        return False


def ifprime():
    x = eval(input("What 
    print("The first", x, "primes are: ")
    print()
    count = 0 
    twincount = 0
    n = 2 
    curr = -3 
    while count <= x : 
        if isprime(n) == True : 
            if n == curr+2 : 
                twincount = twincount+1 
            curr = n 
            count = count + 1 
            print(n, end=' ')
        n = n + 1 
    print()   
    print("And there are", twincount, "twin primes among em")
    print()
    
def main():
    
    ifprime()
    
main()
