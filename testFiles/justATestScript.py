import sys
import collections

flavors = []
f = open("flavors","r")
for line in f:
    list = line.split("?")
    for item in list:
        # item =
        flavors.append(item.strip("\t"))

o = open("orderings","r")
preferences = []
cleanprefs =[]
for line in o:
    preference = line.split("Group")
    preference.pop(0)

    pref = []
    for item in preference: # each item is an ordering
        item = item.split("?")
        item.pop(0)
        # print(item)
        # print()
        # preferences.append(item)
        for i in item:
            pref.append(i.strip("\t"))
        preferences.append(pref)

flavors.pop(len(flavors)-1)
for pref in preferences:
    # pref.pop(len(flavors)-1)
    for i in range (len(pref)):
        if pref[i] == "\n":
            pref.pop(i)

orderings = {} #dict of preferences
for i in flavors:
    for j in flavors:
        if i == j:
            continue
        else:
            orderings[(i,j)] = 0


for group in preferences: # storing pairwise comparison counts
    for i in range(len(group)):
        for j in range (i+1,len(group)):
            orderings[(group[i],group[j])] += 1

counts = {}
for f in flavors:
    counts[f] = 0

for f in flavors: # making sure that it is preferred by 6 or more groups for ALL flavors]
    count = 0
    for g in flavors:
        if f == g:
            continue
        else:
            if orderings[(f,g)] >= 6:
                count += 1
    if count > 30:
        print(f, "is a winner")
