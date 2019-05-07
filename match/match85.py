




def main():
    yes=False
    while yes==False:
        try:
            user_input=input("Please enter the file you wish to use: ")
            text=open(user_input,"r")
            yes=True
        except:
            print("Please try again and enter a text file that exists.")
        
    text_list=text.readlines()
    
    if text_list[0] != "\n":
        new_text_list=[]
        for i in range(len(text_list)):
            new_text_list=new_text_list+[""]
            for j in range(len(text_list[i])-1):
                new_text_list[i]=new_text_list[i][0:j]+text_list[i][j]
        text_list=new_text_list
        for x in range(1,len(text_list[1:])+1):
            matchstart,matches=check(text,text_list,x)
            mismatches=len(text_list[x])-matches
            if len(text_list[x])!=0 or text_list[x]!="":
                print("Sequence ", x, " has ",mismatches," errors at position ",matchstart,".",sep="")
            else:
                print("Sequence",x, "is blank.")
    else :
        print("The master sequence was blank.")
def check(text,text_list,x):
    matches=0
    previous_matches=0
    matchstart=0
    total_matches=0
    for i in range(len(text_list[0])):
        for j in range(len(text_list[x])):
            if text_list[0][i]==text_list[x][j]:
                previous_matches=matches
                matches=0
                try:
                    for k in range(len(text_list[x])):
                        if text_list[0][(i-j)+k]==text_list[x][k]:
                            matches=matches+1
                except:
                    Z=1
                if matches>total_matches:
                    matchstart=len(text_list[0][:i-j])
                    total_matches=matches
    return(matchstart,total_matches)
                
main()

