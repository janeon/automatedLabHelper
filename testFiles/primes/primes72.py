







def Prime():
    n = eval(input("Please give me a number and I will list that many prime numbers: "))
    j = 0 
    x = 2
    counter = 0
    holder = -1
    while j < n:   
        IsPrime = True
        for i in range(2, x):
            if x % i == 0:
                IsPrime = False
        if IsPrime == True:
            print(x)
            j = j + 1
            if x - holder == 2:
               counter = counter + 1
            holder = x
        x = x+1
    print("There are", counter, "twin primes in this sequence.")


Prime()