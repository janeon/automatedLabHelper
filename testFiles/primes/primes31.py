





def kind(a):
    m = True
    if a==2:
        m=True
    elif a==1:
        m=False
    elif a<=0:
        m=False
    else:
        for i in range(2,a):
            if a%i==0:
                m = False
    return(m)

def body(n):
    if n>1:
        print("The first",n,"primes are:")
    elif n==1:
        print("The first prime is:")
    count = 0
    check = 2
    twin = 0
    while(count<n):
        if kind(check)==True:
            print(check, end=' ')
            if kind(check-2)==True:
                twin=twin+1
            count=count+1
        check=check+1
    print()
    print("Among these there are",twin,"twin primes.")
    print()
    
def main():
    print()
    print("This program will print out a given number of primes")
    print("and the number of twin primes among said primes.")
    print()
    n = eval(input("Please enter a postitive integer: "))
    print()
    if n>=1:
        body(n)
    else:
        print("Please try again with a POSITIVE INTEGER.")
        print()
main()