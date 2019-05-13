




def primes(n):
    current = n
    while current < n**2:
        for i in range(2, n):
            if n%i == 0:
                return(False)
            current = current + 1
    return(True)
    
    
def main():
    n = eval(input("Peer into the magic ball, and say the number of primes you wish: "))
    print("So sayeth the crystal, the first", n, "primes are: ")
    x = 1
    j = 3
    twin = -1
    twinprimes = 0
    print(2, end=' ')
    while n > x:
        check = primes(j)
        if check == True:
            print(j, end=' ')
            if j == twin+2:
                twinprimes = twinprimes + 1
            twin = j
            j = j+1
            x = x+1
        else: j = j+1
    print()
    print("Amongst these there are", twinprimes, "twin primes.")
        
    
main()