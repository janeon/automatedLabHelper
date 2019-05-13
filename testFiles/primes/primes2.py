





def main():
    curr = 2
    prev = 2
    prime = 0
    factor = 0
    twin = 0
    print("I can give you a list of the first however many prime numbers!")
    n = eval(input("So, how many do you want? "))
    while prime < n:
        for j in range (2, curr):
            if curr % j == 0: 
                factor = factor + 1 
        if factor == 0:
            prime = prime + 1 
            if curr-prev == 2: 
                twin = twin + 1 
            prev = curr 
            print(curr, " ", sep ="", end = "") 
        curr = curr + 1 
        factor = 0 
    print()
    print("There are", twin, "twin primes in the first", n, "primes.")
main()



