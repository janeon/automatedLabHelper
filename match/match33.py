



def main():
    inputfile = open("text.txt","r")
    prot = inputfile.readline()
    print(prot)
    seq = 0
    minmismatch = 0
    minmismatchposition = 0
    s = inputfile.readline()
    while s != "":
        s = s[:-1]
        minmismatch = len(prot)+1
        for i in range (len(prot) - len(s)):
            protslice = prot[i:len(s)+i]
            mismatch = 0
            for j in range (len(protslice)):
                if protslice[j] != s[j]:
                    mismatch = mismatch +1
            if mismatch < minmismatch:
                minmismatch = mismatch
                minmismatchposition = i
        s = inputfile.readline()
        seq = seq + 1
        print ("sequence",seq,"You have",minmismatch, "errors","starting at position",minmismatchposition)
main()

