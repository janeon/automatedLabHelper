




import math

def isPrime(prime):
    for i in range(2,prime):
        if prime%i==0:
            
            return False
            break
    else:
        return True
        

def main():
    
    
    counter=3
    primes=eval(input("How many primes would you like me to print? ")) 
    if primes==0:
        print(":/")
    elif primes==1:
        print("Well...the 1st prime is two...and that would mean this set has no twins.")
        print("Why would you only ask for one prime?")
        print("What's wrong with you?")
        print("Don't you have any imagination?")
    else:
        limit=primes-1
        printed=0 
        twins=0 
        temp=0 
        print("The first", primes,"primes are:", "2",' ', end='')
        while True:
            dharma=True
            for i in range(2,counter):
                if isPrime(counter):
                    print(counter,' ',end='')
                    printed=printed+1
                    if temp==counter-2:
                        twins=twins+1
                    temp=counter
                    break
                else:
                    dharma=False
                    break
            counter=counter+1
            if printed==limit:
                break
        print()
        print("This set contains", twins, "twin primes.")

main()