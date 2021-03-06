import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import csv

from pprint import pprint

# set matplotlib fonts to CMU Serif
mpl.rc('font',**{'family':'serif','serif':['CMU Serif']})
mpl.rc('text', usetex=True)


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
    fit = np.polyfit(x[6:12], y[6:12], 1)
    
    return fit[0]

def makePlot(data, label):
    Vcm = np.arange(0, 5.01, 0.01)
    gm = []

    for subset in data:
        x, y = extract_xy(subset)
        gm.append(makeFit(x, y))

    plt.plot(Vcm, gm, label=label)

if __name__ == "__main__":

    PATH       = '../Data/'

    FILENAME1 = PATH + 'final_Vb0.76_V0.8.txt'
    FILENAME2 = PATH + 'final_Vb0.76_V1.0.txt'
    FILENAME3 = PATH + 'final_Vb0.76_V1.4.txt'
    FILENAME4 = PATH + 'final_Vb0.76_V1.8.txt'
    FILENAME5 = PATH + 'final_Vb0.76_V2.2.txt'
    FILENAME6 = PATH + 'final_Vb0.76_V2.6.txt'

    LABEL1    = '$\mathrm{V_{ref} = 0.8 V}$'
    LABEL2    = '$\mathrm{V_{ref} = 1.0 V}$'
    LABEL3    = '$\mathrm{V_{ref} = 1.4 V}$'
    LABEL4    = '$\mathrm{V_{ref} = 1.8 V}$'
    LABEL5    = '$\mathrm{V_{ref} = 2.2 V}$'
    LABEL6    = '$\mathrm{V_{ref} = 2.6 V}$'


    makePlot(getData(FILENAME1), LABEL1)
    makePlot(getData(FILENAME2), LABEL2)
    makePlot(getData(FILENAME3), LABEL3)
    makePlot(getData(FILENAME4), LABEL4)
    makePlot(getData(FILENAME5), LABEL5)
    makePlot(getData(FILENAME6), LABEL6)

    plt.xlabel('$\mathrm{V_{cm}}$ (V)', fontsize=14)
    plt.ylabel('$\mathrm{g_m}$ (S)', fontsize=14)
    plt.title('$\mathrm{g_m}$ vs. $\mathrm{V_{cm}}$ of a Modified Rail to Rail Diff Amp', fontsize=16)
    plt.legend(loc='lower right')
    plt.show()
