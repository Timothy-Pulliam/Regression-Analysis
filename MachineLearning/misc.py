'''A confusion matrix is a table that is often used to describe the performance of a classification model
(or "classifier") on a set of test data for which the true values are known.'''

import numpy

def confusionMatrix(A):
    # A is a numpy matrix of the form [True Positive, False Positive; False Negative, True Negative]
    # total =  tp + fp + fn + tn
    total = A.sum()

    tp, fp, fn, tn = A[1,1], Ap[1,2], A[2,1], A[2,2]

    accuracy = (tp + tn) / total # value ranging [0,1], best case fn = fp = 0 and accuracy = 1.
    error_rate = 1 - accuracy
    positivePredictiveValue = tp / (tp + fp)
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)

    
