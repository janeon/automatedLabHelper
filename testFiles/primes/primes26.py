





def main():
    n = eval(input("Please enter the number of primes you wish to display: "))
    print("The first", n, "primes are:")
    prime_counter=0
    twin_prime_counter=0
    i=2
    previous_prime=1
    while (prime_counter < n):
        isPrime(i)
        if isPrime(i) == 0:
            prime_counter = prime_counter +1
            print(i," ",end='', sep='')
            if i-2==previous_prime:
                twin_prime_counter=twin_prime_counter+1
            previous_prime=i
        i=i+1
    print()
    print("Among these primes, there are", twin_prime_counter, "twin primes.")
    
        
def isPrime(x):
    xisprime = 0
    for i in range(2,x):
        f = x%i
        if f == 0 :
            xisprime = 1
    return(xisprime)
main()
