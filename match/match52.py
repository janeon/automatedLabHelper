



                    
def main():
    text=True
    while text==True:
        try:
            fileName=input("Please enter the text file you would like to test: ")
            inputFile=open(fileName,"r")
            s=inputFile.readline()
            s=s[:-1]
            counter=0
            lines=inputFile.readlines()
            length=len(lines)
            inputFile.seek(0)
            inputFile.readline()
            for j in range(length): 
                marker=inputFile.readline() 
                marker=marker[:-1]
                start=0
                counter=0
                error=len(marker)
                for i in range(len(s)): 
                    if len(s[i:])>=len(marker): 
                        match=0
                        x=s[i:i+len(marker)]
                        for k in range(len(marker)):
                            if x[k]==marker[k]:
                                match=match+1
                        if match>counter:
                            counter=match
                            start=i
                            error=len(marker)-match
                print("Sequence",j+1,"has",error,"errors at position",start)
                text=False
                
        except IOError:
            print("Please enter a text file in your directory")
        
    
    
main()

