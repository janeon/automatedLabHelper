






def primetest(x):
    i = 1
    for i in range(2,x//2+1):
        if x%i == 0:
            return False
    if x//2 == i:
        return True
def twins(list):
    twin = 0
    for j in range(len(list)-1):
        if list[j+1]-list[j] == 2:
            twin = twin+1
    print("There are",twin,"twin primes.")
        

def main():
    n = eval(input("How many primes are you interested in?"))
    list = [2]
    if n == 1:
        print(list)
    else:
        x = 3
        while len(list) < n:
            if primetest(x) == True:
                list.append(x)
            x = x+1
        print(list)
        twins(list)

main()