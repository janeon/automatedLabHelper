






def main() :
    goodInput=False   
    while not goodInput :
        try :
            print()
            FILE=input("Please enter the name of the text file: ")
            print()
            inputFile=open(FILE,"r")
            goodInput=True
        except Exception as e :
            print("Sorry, that's not a valid file name")
    PROTEIN=inputFile.readline()
    SEQS=inputFile.readlines()
    bestMatch=[0,99]
    bestFirstMatch=[0,0]
    errors=0
    x=1
    for i in range(0,len(SEQS)) :
        STRING=SEQS[i]
        STRING=STRING[:-1]
        for i in range(0,len(PROTEIN)-len(STRING)) :
            for j in range(0,len(STRING)) :
               if i+j<len(PROTEIN) :
                    if STRING[j]!=PROTEIN[i+j] :
                        errors=errors+1
               if bestMatch[1]==bestFirstMatch[1] :
                    bestMatch[0]=bestFirstMatch[0]
               if i==0 :
                    bestMatch[1]=errors
                    bestFirstMatch[1]=errors
                    bestFirstMatch[0]=i
            if errors<bestMatch[1] :
                bestMatch[0]=i
                bestMatch[1]=errors
            errors=0
        if len(STRING)>0 :
            print("Sequence", x, "has", bestMatch[1], "errors at position", bestMatch[0] )
            x=x+1
    print()
    
main()