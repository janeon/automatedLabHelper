





def main():
    n=eval(input("How many primes would you like master?: "))
    prime=0
    current=2
    past=2
    twin=0
    x=0
    while prime < n:
        for i in range (2, current):
            z=current%i
            if z==0:
                x=x+1
            else:
                x=x+0
        if x == 0:
            if current-past==2:
               twin=twin+1
            print(current, end=" ")
            prime=prime+1
            past=current
        current=current+1
        x=0
    print()
    print("The number of twin primes in this set is", twin)
main()