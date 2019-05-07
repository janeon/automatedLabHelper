




def testsequence(n, aminoacid, i, bestfit):
    tempsequence = n[i]
    temp1 = len(aminoacid)-len(tempsequence)-2
    temp = [0]*temp1
    for j in range(len(aminoacid)-1-len(tempsequence)-1):
        aminoacid = aminoacid[1:]
        for k in range(len(tempsequence)-1):
            if tempsequence[k] != aminoacid[k]:
                temp[j] = temp[j]+1
    temp1 = []
    for q in range(len(temp)):
        temp1.append(temp[q])
    print(temp1)
    temp1.sort()
    x = temp.index(temp1[0])
    print("Sequence", i, "has", temp1[0], "errors at position", x+1)
    
    

def main():
    bestfit = []
    inputFile = open("test.txt")
    n = inputFile.readlines()
    aminoacid = n[0]
    for i in range(1, len(n)):
        testsequence(n, aminoacid, i, bestfit)
    
        
    
    
main()