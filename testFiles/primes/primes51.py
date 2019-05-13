





def main():
    n = eval(input("please enter a number: "))
    j = 0
    x = 2
    bloop = 0 
    moop = -1 
    while j < n :
        IsPrime = True
        for i in range(2,x):
            if x%i == 0 :
             IsPrime = False
        if IsPrime == True : 
            print(x)
            j = j+1
            if x - moop == 2 :
                bloop = bloop +1
            moop = x
        x = x+1
    print("the number of twin primes is:", bloop)
main()