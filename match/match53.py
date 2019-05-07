





def main():
    try:
        
        filename = input("What file would you like to use?")
        file = open(filename,"r")
        protein = file.readline()
        protein = protein.strip()
        prot = []
        for char in protein:
            prot.append(char)
        mark = []
        for line in file:
            mark.append(line.strip())
        mini = []
        for i in range(len(mark)):
            d = len(prot) - len(mark[i])
            mismatch = []
            for pos in range(d+1):
                t = test(mark,i,prot,pos)
                
                mismatch.append(t)
            
            tiniest = min(mismatch)
            
            potn = mismatch.index(tiniest)
            
            numPos = [mismatch[potn],potn]
            print("Sequence",i+1,"has",numPos[0],"errors at position",numPos[1])
    except Exception as e:
        print(e)
        print(str(e))
        
    
def test(list,x,tein,d):
    j = len(list[x])
    errors = 0
    for y in range(j):
        if list[x][y] != tein[d+y]:
            errors += 1
    return errors
            
        
    


main()