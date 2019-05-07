





def check(line):        
    s=line[0]
    s=s.strip()
    if s=='':
        print("The first line should be the protein sequence")
        print("There is no protein in this file")
    else:
        for h in range (1,len(line)):   
            new=line[h]
            new=new.strip()
            if new=='':
                print("Sequence", h, "is blank")
            else:
                TotalErrors=len(new)
                Position=0
                for i in range (len(s)-len(new)):       
                    errors=0
                    for j in range (len(new)):      
                        if s[i+j] != new[j]:
                            errors=errors+1
                    if errors<TotalErrors:
                        TotalErrors=errors
                        Position=i
                print("Sequence", h, "has", TotalErrors, "errors at position", Position)
        

def main():     
    try:
        print()
        print("This program tests protein strings against different marker sequences")
        filename=input("What is the name of your text document to test: ")
        print()
        file=open(filename,'r')
        line=file.readlines()
        if len(line)==0 or len(line)==1:
            print("This document is not long enough")
        else:
            check(line)
        print()
    except IOError:
        print("Uh oh. That file doesn't work. Sorry")
        
main()