





def main():
    goodinput=False
    while not goodinput:
        try:
            filename=input("Please enter the name of the file: ")
            file=open(filename,"r")
            goodinput=True
        except IOError:
            print("Invalid input. Please enter the correct name of the file. Don't forget to include file type!")
    seq=[]
    lenfile=0
    for line in file:
        lenfile=lenfile+1
        seq=seq+[line[:-1]]
    for i in range(1,lenfile):
        early=0
        c=[]
        for j in range(len(seq[0])-len(seq[i])+1):
            counter=0
            for z in range(len(seq[i])):
                if seq[i][z]==seq[0][j+z]:
                    counter=counter+1
            c=c+[counter]
        temp=c[0]
        for t in range(len(c)):
            if c[t]==0:
                early=early+1
        if early==len(c):
            posit=0
        else:        
            for f in range(len(c)):
                if c[f]>temp:
                    temp=c[f]
                    posit=f
        print("Sequence ",i," has ",len(seq[i])-c[posit]," errors at position ",posit,".",sep='')

main()