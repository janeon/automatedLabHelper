





def match_test(line,sequence):
    global error
    n=len(line)
    startVal=0
    endVal=n
    error=[]
    for a in range(0,(len(sequence))-n):
        error.append(0)
        for i in range (startVal,endVal):
            if sequence[i+a]!=line[i]:
                error[a]=error[a]+1
    min_index=0
    old_error=error[0]
    for j in range(0,len(error)):
        new_error=error[j]
        if new_error<old_error:
            min_index,old_error=j,new_error
    print("Sequence",line,"has",old_error,"errors at position",(min_index))

def main():
    try:
        inputFile=open(input("Please enter a text document to compare pattern sequences: "),"r")
        sequence=inputFile.readline()
        print(sequence,end="")
        for line in inputFile:
            line=line.strip()
            match_test(line,sequence)
            print()
    except IOError:
            print("Load an existing file")
    except:
        print("Try loading a .txt file")
main()