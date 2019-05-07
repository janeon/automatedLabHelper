






def main():
    z = input("What file do you want to use? (test.txt for test) ")
    f = open(z, "r")
    k = [] 
    for line in f :
        k.append(line[0:len(line)])
    p = k[0] 
    s = k[1:len(k)] 
    for i in range(len(s)):  
        m = mismatches(p,s[i])
        m.sort()
        x = m[0] 
        n = position(p,s[i],x)
        print("Sequence",i+1,"has",x,"errors at position",n)

def mismatches(p,s): 
    m = []
    for i in range(0,len(p)-len(s)-1): 
        mismatch = 0
        for j in range(0,len(s)-1): 
            if p[j+i] != s[j]:
                mismatch = mismatch + 1
        m.append(mismatch)
    return m

def position(p,s,x):
    n = 0
    for i in range(0,len(p)-len(s)-1): 
        mismatch = 0
        for j in range(0,len(s)-1): 
            if p[j+i] != s[j]:
                mismatch = mismatch + 1
        if mismatch == x:
            n = i
            break
    return n
    
main()