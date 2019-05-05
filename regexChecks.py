""" input: string line
    return vals:
        0 didn't match any regexes
        1 trying to use a python keyword in assignment
        2 forgetting a ":" at the end of a function call
        3 forgetting "()" at the end of a function call
        4 forgetting a ":" at the end of a for/while loop
        5 forgetting a ":" at the end of a conditional statement
"""
import re
regex1 = re.compile("(False|None|True|and|as|assert|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield) = [a-zA-Z0-9-+_\[\]{}(),:]*")
regex2 = re.compile("def [a-zA-Z_][a-zA-Z0-9_]*:")
regex3 = re.compile("def [a-zA-Z_][a-zA-Z0-9_]*\(\)")
regex4 = re.compile("")

def check(line):
    if (regex1.match(line)):
        return "This error occured because you tried to use a python keyword in your variable assignment."
    elif (regex2.match(line)):
        return "This error occured because you forgot a colon at the end of your function call."
    elif (regex3.match(line)):
        return "This error occured because you forgot the parentheses after your function name."
    elif (regex4.match(line)):
        return "This error occured because you forgot a colon at the end of your loop."
    elif (regex5.match(line)):
        return "This error occured because you forgot a colon at the end of your conditional statement."
    return ""

#def main():
    #l1 = "for = 8"
    #print("check for ","\"",l1,"\""," is ",check(l1))
    #l2 = "def foo:"
    #print("check for ","\"",l2,"\""," is ",check(l2))
    #l3 = "def foo()"

#main()




#test_str = ("for i in range(2):\n"
	#"for = 5\n"
	#"fdsa = 2\n"
	#"continue = 3\n\n\n\n")

#matches = re.finditer(regex, test_str, re.MULTILINE)

#for matchNum, match in enumerate(matches, start=1):

    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

    #for groupNum in range(0, len(match.groups())):
        #groupNum = groupNum + 1

        #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
