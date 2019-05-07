










def large(a, seq) :   
    x=0
    length = 0
    for k in a : 
        length = length + 1
    for i in range(length) : 
        p = 0
        x = 0
        for j in range(length) :
            for w in range(1, length) :    
                if a[i] < a[j]: 
                    x = x + 5 
                if a[i] == a[j] and a[i] < a[w]: 
                    x = x + 5 
                else :
                    x = x 
        if x == 0 :
            errors = len(seq)-a[i] 
            largest = i
            li = a[0:largest] + a[largest+1: len(a)]
            
            return errors, i 





def match(protien, seq):
    count = 0
    li = []
    x = 0
    y = len(seq)
    while y < len(protien): 
        h = 0
        count = 0
        for i in protien[x:y]: 
            if i == seq[h]: 
                count = count + 1 
            h = h+1 
        li = li + [count]
        x = x + 1 
        y = y + 1
    er, pos = large(li, seq)        
    return er, pos 





def textinfo():
    try:    
        text = input("Please select a .txt file you would like to be evaluated: " )
        text = open(text, "r")
        protien = text.readline()
        protien = protien.strip()
        numlines = 0
        for line in text :
            numlines = numlines +1
        text.seek(0)
        text.readline()
        seq = "shit"
        for i in range(1, numlines+1):     
            seq = text.readline()
            seq = seq.strip()    
            er, pos = match(protien, seq)
            print("sequence", i, "has", er, "errors at position", pos)
    except FileNotFoundError :
        print()
        print("You may have incorrectly entered the document's name.")
        print()







def main():
    try:
        textinfo()
    except NameError :
        print()
        print("Sorry, we can't seem to find that file, try another")
        print()
main()




