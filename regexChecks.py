""" input: string line
    return vals:
        0 didn't match any regexes
        1 trying to use a python keyword in assignment
        2 forgetting a ":" at the end of a function call
        3 forgetting "()" at the end of a function call
        4 forgetting a ":" at the end of a for loop
        5 forgetting a ":" at the end of a conditional statement
        6 forgetting a ":" at the end of a while loop
        7 using () instead of [] to call an index of a list
            this one is commented out b/c i'm not totally sure about it. it would work in a specific case, but not all

        others we could implement: stuff for incorrect bracket types???
"""
import re
regex1 = re.compile("^(False|None|True|and|as|assert|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield) = [a-zA-Z0-9-+_\[\]{}(),:]*")
regex2 = re.compile("^def [a-zA-Z_][a-zA-Z0-9_]*\(\)$")
regex3 = re.compile("^def [a-zA-Z_][a-zA-Z0-9_]*:")
regex4 = re.compile("^for .* in [^:\n]*$")
regex5 = re.compile("^(if |elif |else)[^:\n]*$")
regex6 = re.compile("^while [^:\n]*$")
#regex7 = re.compile("^[a-zA-Z_][a-zA-Z0-9_]* = [a-zA-Z_][a-zA-Z0-9_]*\(.*\)$")

def check(line):
    if (regex1.match(line)):
        return "Looks like you tried to use a python keyword in your variable assignment."
    elif (regex2.match(line)):
        return "Looks like you forgot a colon at the end of your function call."
    elif (regex3.match(line)):
        return "Looks like you forgot the parentheses after your function name."
    elif (regex4.match(line)):
        return "Looks like you forgot a colon at the end of your for loop."
    elif (regex5.match(line)):
        return "Looks like you forgot a colon at the end of your conditional statement."
    elif (regex6.match(line)):
        return "Looks like you forgot a colon at the end of your while loop."
    #elif (regex7.match(line)):
        #return "Looks like you tried to use () rather than [] when accessing an array item"
    return ""

#def main():
    #l1 = "for = 8"
    #print("check for ","\"",l1,"\""," is ",check(l1))
    #l2 = "def foo:"
    #print("check for ","\"",l2,"\""," is ",check(l2))
    #l3 = "def foo()"
    #print("check for ","\"",l3,"\""," is ",check(l3))

#main()
