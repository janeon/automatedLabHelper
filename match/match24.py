





def Match(comparee, tester):
    length = len(comparee)
    longeur = len(tester)
    worst_possible_thing = longeur
    match_site = 0
    for i in range(0, length-longeur-1):
        mismatches = 0
        for j in range(0, longeur-1):
            if tester[j] != comparee[i+j]:
                mismatches = mismatches + 1
        if mismatches < worst_possible_thing:
            match_site = i
            worst_possible_thing = mismatches
    print("Sequence ", tester[:-1], " has ", worst_possible_thing, " errors at position ", match_site, ".", sep='')
    print()

def main():
    done = False
    while not done:
        try:
            name = input("Pick a file to read: ")
            strings = open(name, "r")
            done = True
            comparee = strings.readline()
            for tester in strings:
                Match(comparee, tester)
        except IOError:
            print("No dice, try again.")
            
main()


