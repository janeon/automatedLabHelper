





def isPrime(blah):
    DummyVar = 0
    for i in range(2,blah):
        if blah%i == 0:
            DummyVar = 1
    if DummyVar != 1:
        return True
    else:
        return False



def main():
    n = eval(input("How many primes would you like to print out?: "))
    if n == 0:
        print("Until next time I guess... =(")
    elif n == 1:
        print("2 is the first prime and there are no twins.")
    else:
        numTwins = 0
        numprimes = 1 
        blah = 3
        print("The first ",n," primes are: 2 ",end='',sep='')
        while (numprimes < n):
            if isPrime(blah) == True :
                print(blah," ",end='',sep='')
                if blah>4:
                    if isPrime(blah-2) == True:
                        numTwins = numTwins+1
                numprimes = numprimes+1
            blah = blah+1
        print()
        print("Amongst these there are",numTwins,"twin primes.")
    
    
main()