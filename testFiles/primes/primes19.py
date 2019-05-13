






def IsPrime( number ):
    for i in range(2, number ):
        if (number%i) == 0:
            return False
    return True

def Main():
    n = eval( input( "How many prime numbers would you like? " ) )
    primesFound = 0
    twinPrimes = 0
    
    previous = 2
    number = 2
    done = False
    while not done:
        if primesFound == n:
            done = True
        else:
            if IsPrime( number ):
                print( number, "", end = "" )
                primesFound = primesFound+1
                if (number-previous) == 2:
                    twinPrimes = twinPrimes+1
                previous = number
            number = number+1
    print()
    print( "Amongst these there are {0} twin primes.".format( twinPrimes ) )
    
    
Main()
