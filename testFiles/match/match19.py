





def bestSequence(S, P):
    guess=len(P)
    bestPosition=0
    for i in range(0, len(S)-len(P)):
        if errorSequence(S, P, i) < guess:
            guess=errorSequence(S, P, i)
            bestPosition=i
    return (guess, bestPosition)
            
def errorSequence(S, P, position):
    errors=0
    for i in range(0, len(P)-1):
        if S[position+i]!=P[i]:
            errors+=1
    return errors

def main():
    userFile=input("Please select a file to input:")
    file=open(userFile, "r")
    S=file.readline()
    x=0
    for line in file:
        P1=line
        x+=1
        print("Sequence", x, "has", bestSequence(S, P1)[0], "errors at position", bestSequence(S, P1)[1])
main()

