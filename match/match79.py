


def main():
    test = open("test.txt", "r")
    p = test.readline()
    counter = 0
    for s in test:                 
        bestStart = 0
        bestMis = len(s)
        for i in range(len(p)-len(s)):
            error = 0
            for j in range(len(s)):
                if p[i+j] != s[j]:
                    error = error + 1
            if error < bestMis:
                bestMis = error
                bestStart = i
        counter = counter + 1
        print("Sequence ", counter, " has ",bestMis-1,
              " errors at position ", bestStart, ".", sep='')
            



    

main()