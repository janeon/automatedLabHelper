





def calculation(s, line):
    best = len(line)
    failure = 0
    position = 0
    for i in range(0, len(s) - len(line) - 1):
        match = 0
        mismatch = 0
        for j in range(0, len(line) - 1):
            if s[j+i] == line[j]:
                match = match + 1
            if s[j+i] != line[j]:
                mismatch = mismatch + 1
        if mismatch < best:
            best = mismatch
            position = i
            failure = mismatch
    print("Sequence", line[:-1], "has", failure, "errors at", position)


def main():
    inputFile = open("test.txt", "r")
    s = inputFile.readline()
    print()
    for line in inputFile:
        calculation(s, line)
    print()

main()