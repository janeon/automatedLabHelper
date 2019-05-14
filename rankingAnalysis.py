''' rankingAnalysis.py
    accepts a file name,
'''
#import numpy as np
import sys
import argparse
import matplotlib.pyplot as plt

def plot(data):
    pass
    #barGraph = plt.bar()

def total(data):
    sum = 0
    for line in data:
        sum += line[1]
    return sum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='should be an output file including the results of a run from ranking.py')
    args = parser.parse_args()

    data = list(open(args.file,"r")).split(":")
    print(data)

    cData = []
    rData = []
    wData = []
    eData = []
    fData = []
    # separating data by error type
    for line in data:
        if "C" in line[0]:
            cData.append(line)
        elif "R" in line[0]:
            rData.append(line)
        elif "W" in line[0]:
            wData.append(line)
        elif "E" in line[0]:
            eData.append(line)
        elif "F" in line[0]:
            fData.append(line)

    #cTotal = total(cData)
    #rTotal = total(rData)
    #wTotal = total(wData)
    #eTotal = total(eData)
    #fTotal = total(fData)

    plotData = [["C",total(cData)],["R",total(rData)],["W",total(wData)],["E",total(eData)],"F",total(fData)]
    plot(plotData)

if __name__ == "__main__":
    main()
