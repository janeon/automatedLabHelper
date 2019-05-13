





def isPrime(x):
    if x <= 1 :
        return False
    elif x == 2:
        return True
    else:
        for f in range (2,x):
            if x % f == 0 :
                return False
        return True

def main():
    n = eval(input("How many primes do you want to see? "))
    print()
    print("The first", n, "primes are:")
    countPri = 0
    countTwi = 0
    cur = 2
    
    for i in range(1000000000000):
        if isPrime(i) is True:
            countPri = countPri +1 
            
            if countPri <= n:
                print(i, end = " ")
                
                if i - cur == 2:
                    countTwi = countTwi + 1
                cur = i
            
            else:
                break
    print()
    print("Amongst these there are", countTwi, "twim primes.")
    print()
        
main()