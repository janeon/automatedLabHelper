




def main():
    file=input("Enter file name: ")
    try:
        p=open(file,"r")
        print(p.readline())
        for line in p:
            print(line, end='')
        print()
        p.seek(0)
        PROtein=p.readline()
        for line in p:
            marks=line
            begin,mar=sequence(PROtein,marks)
            print("Best start position: ",begin,"with", mar-1,"errors")
    except:
        print("You did something wrong, are you sure that was a file name?")

   
def sequence(PROtein,marks):
    begin=0
    besmissy=len(marks)
    marxist=len(marks)
    dabest=len(PROtein)
    
    for i in range(0,dabest-marxist):
        mismatch=0
        for j in range(0,len(marks)):
            if marks[j]!=PROtein[j+i]:
                mismatch=mismatch+1
        if mismatch<besmissy:
            begin=i
            besmissy=mismatch
    return (begin,besmissy)










    
    
        
main()