





def isPrime(n):
    prime = True
    for x in range (2, n):
        if n%x == 0:
            prime = False
    return prime

def generateprime(n):
    total = 0
    while total < n:
        if isPrime(n) == True :
            print (n)
            total = total +1
        else:
            n = n+1
    
def main():

    n = eval(input("How many primes do you want? "))
    generateprime(n)

    
main()  