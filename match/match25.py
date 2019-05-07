







def countLines(file):
    file.seek(0)
    lines = 0
    for i in file:
        lines = lines + 1
    lines = lines - 1
    return lines


def proteinList(file):
    file.seek(0)
    P = []
    protein = file.readline()
    for ch in protein:
        P.append(ch)
    P.pop(-1)
    return P


def subList(file, lines):
    file.seek(0)
    S = []
    for i in range(lines+1):
        list = []
        subsequence = file.readline()
        for ch in subsequence:
            list.append(ch)
        S.append(list)
        list.pop(-1)
    S.pop(0)
    return S
        

def findMatches(file, S, P):
    sequenceMatches = []
    matches = 0
    k = 0
    for i in S:
        positionMatches=[]
        for j in range(len(P)-len(i)):
            k = j          
            for ch in i:
                if ch == P[k]:
                    matches = matches + 1
                    k = k + 1
                else:
                    k = k + 1
            positionMatches.append(matches)
            matches = 0
        sequenceMatches.append(positionMatches)
    return sequenceMatches
    

def answer(file, S, sequenceMatches):
    lengthsequence = []
    for h in S:
        lengthsequence = lengthsequence + [len(h)]
    z = 0
    for i in sequenceMatches:
        if i == []:
            print("Sequence",z+1,"has no matches.")
        else:
            matches = max(i)
            position = i.index(matches)
            print("Sequence ",z+1," has a best match with ",lengthsequence[z]-matches," errors at position ",position,".",sep="")
        z = z + 1
        
def main():
    print("Welcome to my protein matching program!")
    try:
        document = input("Please enter the name of your desired file: ")
        file = open(document, "r")
        print()
        
        lines = countLines(file)
        P = proteinList(file)
        S = subList(file, lines)
        sequenceMatches = findMatches(file, S, P)
        file = open(document,"r")
        proteinList(file)
        subList(file, lines)
        matches = findMatches(file, S, P)
        answer(file, S, sequenceMatches)
    except IOError:
        print()
        print("Oops! I couldn't find the file you're looking for. Please make sure you're typing the proper file name and extension and try again.")
    except Exception as e:
        print (type(e))
        print (str(e))
    
main()