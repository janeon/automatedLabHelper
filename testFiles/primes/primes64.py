







def isPrime(i):
    for factor in range(2,i):
        if i%factor == 0:
            return False
    
    return True

def main():
    nth = eval(input("Please feed me a number \"nth\" number of prime sequence index: "))
    print("The first", nth, "primes are:")
    numbercounter = 0
    twins = 0
    previous = 3
    for i in range(2, 100000):
        if numbercounter < nth:
            if isPrime(i) == True:
                numbercounter = numbercounter + 1
                print(i," ", end='')
                if i - previous == 2:
                    twins = twins +1
                previous = i
               
    print("Amongst these there are", twins,"twin primes")
                  
main()

