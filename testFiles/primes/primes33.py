





def main() :
    print()
    print("Welcome to Prime Time!")
    print()
    n = eval(input("How many primes do you want to look at? : "))
    count = n
    x = 0
    previous = 1
    twins = 0
    if n == 0 :
        print("You can't look at 0 of something, silly!")
    else :
        while count > 0 :
            x = x + 1
            if isPrime(x) != 0 :
                if x != 1:
                    count = count - 1
                    print(x, " ", sep='', end='')
                    if x - previous == 2 :
                        twins = twins +1
                    previous = x
        print()
        if twins > 0:
            print(twins, "of these are twin primes! Isn't that cool?")
        else :
            print("There are no twin primes here. Sorry!")
    


def isPrime(x) :
    rem = 1
    for f in range (2, (x // 2)+1) :
        rem = x % f
        if rem == 0 :
            break
    return rem

main()
