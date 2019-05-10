






def fileName():
    fileName=input("Please enter the file name you would like me to use: ")
    return fileName


def numMark(inputFile):
    inputFile.seek(0)
    numlines=0
    for line in inputFile:
        numlines=numlines+1
    numMarkers=numlines-1
    return numMarkers




def proteins(inputFile):
    inputFile.seek(0)
    P= inputFile.readline()
    Protein=[]
    for i in range (0,len(P)-1):
        Protein.append(P[i])
    return Protein



def marker (inputFile,numMarkers):
    Markers=[]
    for i in range (0,numMarkers):
        Q=[]
        M=inputFile.readline()
        for j in range (0,len(M)-1):
            Q.append(M[j])
        Markers.append(Q)
    return Markers


def smallestErrors(Mismatches, sequence,S):
    Position = 0
    Smlst= len(S)
    for k in range (0, len(Mismatches)):
        if Mismatches[k] < Smlst:
            Smlst= Mismatches[k]
            Position=k
    print("Sequence ", sequence, "has ", Smlst, "errors at position ", Position)
    
        



def matches(S,P,sequence):
    Mismatches=[]
    for i in range (0, len(P)-len(S) +1):
        mismtch=0
        L=i
        for j in range (0,len(S)):
            if P[L] != S[j]:
                mismtch=mismtch+1
            L=L+1
        Mismatches.append(mismtch)
    smallestErrors(Mismatches,sequence,S)
    
    
    


def compare(markers,protein):
    for i in range (0,len(markers)):
        sequence = i +1
        matches(markers[i],protein, sequence)
    
    
    
def main():
    try:
        inputFile=open(fileName(),"r")
        numMarkers=numMark(inputFile)
        protein=proteins(inputFile)
        markers=marker(inputFile,numMarkers)
        compare(markers, protein)
    except IOError:
        print ("I'm sorry I could not find that file")
    except Exception as e:
        print (type(e))
        print (str(e))
main()