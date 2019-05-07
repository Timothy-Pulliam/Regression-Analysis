#!/usr/bin/env python

import pandas as pd
from perceptron import Perceptron
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import tkinter
import numpy as np

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
df.tail()

# Extract the fourth feature (collumn) from samples (rows) 0-100
y = df.iloc[0:100, 4].values
print(y)

# Replace asll instances of "Iris-setosa" with -1, else replace with +1
y = np.where(y == "Iris-setosa", -1, 1)
y

# Retrieve the 1st and 3rd feature (collumn) from the first 100 samples
# 1st feature is Sepal Length, 3rd feature is Petal Length
X = df.iloc[0:100, [0,2]].values
X

plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='veriscolor')
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend(loc='upper left')
plt.show()

ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X,y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.grid(True)
plt.xticks(np.arange(1,11,1))
plt.xlabel('Epoch')
plt.ylabel('Number of Missclassifications')
plt.show()


# Visualize the decision boundary (which is disontinous)
def plotDecisionRegions(X, y, classifier, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # Plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim=(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # Plot case samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y ==cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

plotDecisionRegions(X, y, classifier=ppn)
plt.xlabel('sepal length (cm)')
plt.xlabel('petal length (cm)')
plt.legend(loc='upper left')
plt.show()
