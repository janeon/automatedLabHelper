













def main():
    fileName=input("What file would you like to open? " )
    inputFile=open(fileName, "r")
    firstLine=inputFile.readline()
    firstLine=firstLine.strip()
    lines=inputFile.readlines()
    print(firstLine)
    for i in (lines):
        i=i.strip()
        w=len(i)+1
        x=0
        
        for k in range (0,len(firstLine)-len(i)):
            m=0
            for j in range (len(i)):
                if firstLine[k+j]==i[j]:
                    m=m
                else:
                    m=m+1
            if m<w:
                w=m
                x=k
                
        print("Sequence", i, "has", w, "errors at position", x)
main()


