''' rankingAnalysis.py
    mostly for quickly plotting our results for various parameters.
'''

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

def plot(data):
    objects = ('Convention', 'Refactor', 'Warning', 'Error', 'Fatal')
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, data, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Prevalence')
    plt.title('Pylint Message Prevalence by Type')

    plt.show()

    # with help from: https://pythonspot.com/matplotlib-bar-chart/

''' plot not including convention messages '''
def plotWithoutC(data):
    objects = ('Refactor', 'Warning', 'Error', 'Fatal')
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, data, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Prevalence')
    plt.title('Pylint Message Prevalence by Type')

    plt.show()

''' plots the 10 most common messages, with their prevalences
    here, data should be in the form of a list of [warning, prevalence] pairs'''
def mostCommon(data, type):
    objects = []
    prevalences = []
    for index in range(5):
        objects.append(data[index][0])
        prevalences.append(data[index][1])

    y_pos = np.arange(len(objects))

    plt.bar(y_pos, prevalences, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Prevalence')
    plt.title('Prevalences of the 5 Most Common '+type+' Messages')

    plt.show()



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
    plotDataWithoutC = [total(rData),total(wData),total(eData),total(fData)]
    #plot(plotData)
    #plotWithoutC(plotDataWithoutC)
    #mostCommon(wData, "Warning")

if __name__ == "__main__":
    main()
