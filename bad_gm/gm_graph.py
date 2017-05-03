import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from pprint import pprint

def getData(FILENAME):
    data = []
    subset = []

    with open(FILENAME, 'r') as f:
        content = csv.reader(f, delimiter='\t')

        for i, row in enumerate(content):
            if i==0 or i==1: continue
            elif row[0][0:4] == 'Step':
                data.append(subset) # add subset of data to main data array
                subset = [] # reset subset data array
                continue
            subset.append(row)
        data.append(subset)

    return data


def extract_xy(subset):
    x = []
    y = []

    for row in subset:
        x.append(float(row[0]))
        y.append(float(row[1]))
    
    return np.array(x), np.array(y)


def makeFit(x, y):
    fit = np.polyfit(x[18:23], y[18:23], 1)
    
    return fit[0]

if __name__ == "__main__":
    data = getData('postlab9.txt')
    
    Vcm = np.arange(0, 5.05, 0.05)
    gm = []
    
    for subset in data:
        x, y = extract_xy(subset)
        gm.append(makeFit(x, y))
    
    plt.plot(Vcm, gm)
    plt.xlabel('$V_{cm}$ (V)', fontsize=14)
    plt.ylabel('$g_m$', fontsize=14)
    plt.title('$g_m$ vs. $V_{cm}$ of a Rail to Rail Diff Amp', fontsize=16)
    plt.show()
