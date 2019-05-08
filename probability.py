#!/usr/bin/env python

import numpy as np

def factorial(n):
    '''Calculate n!
    Input
    -----
    n : int
    
    Return
    -------
    n! : int
    '''
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
        
def combinations(n, k):
    '''Returns the number of k-element subsets for an n-element set, without 
    replacement. Order does not matter. Also known as n Choose k.
    
    Usage
    ------
    combinations(4,2)
    6.0
    
    e.g. 12, 13, 14, 23, 24, 34 
    
    Input
    ------
    n : int
    k : int
    
    Return
    ------
    int
    '''
    return factorial(n) // (factorial(n-k) * factorial(k))

def permutations(n, k):
    '''Return the number of possibile permutations without replacement of 
    k-element subsets for an n-element set.

    Usage
    ------
    permutations(4,2)
    12.0
    
    e.g. 12, 13, 14, 23, 24, 34
         21, 31, 41, 32, 42, 43
    
    Input
    ------
    n : int
    k : int
    
    Return
    ------
    int
    '''
    return factorial(n) // factorial(n-k)
    

def binomialCoefficients(n):
    '''Generates the first n Binomial Coeffiecients
    
    Usage
    -----
    a = binomialCoefficients(4)
    next(a)
    1
    next(a)
    3
    
    Alternatively, you can create a list from the generator, although this will
    be less efficient than using a generator.
    
    b = list(a)
    b
    [1, 4, 6, 4, 1]
    
    Input
    ------
    n : int
    
    Return
    -------
    tuple
    '''
    for i in range(n + 1):
        yield combinations(n, i)


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
