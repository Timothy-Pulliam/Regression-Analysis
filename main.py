#!/usr/bin/env python
from analysis import UngroupedData
import numpy as np

# uri = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# from preprocessing import importData
# importData(uri)

def boxPlot(x):
    plt.boxplot(x, vert=False, showmeans=True)
    plt.grid(axis='x',linestyle='--')
    plt.show()

# example usage
x = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
X = UngroupedData(x,isSample=False)
X.printStats()
a = X.getStats()
#print(a['mean'])
boxPlot(X.data)


a = np.array([1,2,3,4,4])
A = GroupedData(a)
A.printStats()

x = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
X = UngroupedData(x)
frequencyDistribution(X.data, n=None)
