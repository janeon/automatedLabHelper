''' rankingAnalysis.py
    accepts a file name,
'''

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

def plot(data):
    objects = ('Convention', 'Refactor', 'Warning', 'Error', 'Fatal')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]


    plt.bar(y_pos, data, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Prevalence')
    plt.title('Pylint Message Prevalence by Type')

    plt.show()

    # with help from: https://pythonspot.com/matplotlib-bar-chart/

def total(data):
    sum = 0
    for line in data:
        sum += line[1]
    return sum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='should be an output file including the results of a run from ranking.py')
    args = parser.parse_args()

    rawData = list(open(args.file,"r"))
    data = []
    for line in rawData:
        line = line.strip("\n").split(": ")
        data.append([line[0],int(line[1])])
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

    plotData = [total(cData),total(rData),total(wData),total(eData),total(fData)]
    plot(plotData)

if __name__ == "__main__":
    main()
