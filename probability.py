#!/usr/bin/env python

import numpy as np

class MarkovChain(object):

    def __init__(self, n, n_iter):
        """Creates n by n matrix of probability states"""
        # Matrix of Probability States
        # pij is the probability of going from state i to state j
        #self.p = np.random.random((n,n))

        self.p = np.array([[0.16439222, 0.05485619, 0.32974946],
                           [0.32964551, 0.80615303, 0.32773613],
                           [0.50596227, 0.13899078, 0.34251441],]
                           )

        # normalize the columns of p
        # TODO, handle roundoff error
        for col in range(n):
            self.p[:, col] /= sum(self.p[:, col])

        # Initialization Vector
        self.vi = np.array([1,0,0])

    def timeStep(self):
        "Advance the time by one epoch"
        self.p = np.matmul(self.p, self.p)

    def printState(self):
        print(self.p)
        print()
        print(self.vi)

if __name__ == '__main__':
    mc = MarkovChain(3,4)
    mc.printState()
    mc.timeStep()
    mc.printState()
    mc.timeStep()
    mc.printState()
    mc.timeStep()
    mc.printState()
    mc.timeStep()
    mc.printState()
    mc.timeStep()
    mc.printState()
    mc.timeStep()
    mc.printState()
    mc.timeStep()
    print()
    print(np.matmul(mc.p, mc.vi))
