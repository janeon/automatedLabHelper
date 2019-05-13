




def isPrime(x):
    for i in range(2,x):
        if(x%i)==0:
            return 0
    return 1    
def main():
    print()
    goal_primes = eval(input("How many primes should I calculate? "))
    print()
    primes = 0
    x = 2
    prime1 = 2 
    twinprime = 0 
    while (x)<9223372036854775807:
        if (isPrime(x))==1:
            print(x," ",end="",sep="")
            primes = primes + 1
            prime0 = prime1
            prime1 = x
            prime2 = prime0
            if (prime1-prime2)==2:
                twinprime = twinprime + 1
        x = x+1
        if (primes)==goal_primes:
            print()
            print("Among these there are", twinprime, "twin primes.")
            print()
            exit()
main()