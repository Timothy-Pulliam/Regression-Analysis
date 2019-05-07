from statistics import mode, variance, pvariance, stdev, pstdev, StatisticsError
from matplotlib import pyplot as plt
import numpy as np
import logging

#TODO
# Identify Nominal, Ordinal and metric data
class UngroupedData(object):

    def __init__(self, x, isSample=True):

        self.descriptiveAnalysis(x, isSample)


    def descriptiveAnalysis(self, x, isSample=True):
        '''Performs basic analysis on a data set,
           calculates mean, median, standard deviation, etc.

           Inputs
           -------
           x : numpy.array object
               The dataset
           isSample : Boolean (True/False)
               Some statistical calculations depend upon whether
               the data is sample or population data
           showOutput : Boolean (True/False)
               Whether or not to print out the resulting statistics.
               Otherwise, the results will only be returned
               as a dictionary.

           Outputs
           -------
           stats : dictionary
               Dictionary containing the calculated statistics
        '''
        self.data = x

        # sample size
        self.size = x.size

        # range data
        self.min = np.min(x)
        self.max = np.max(x)
        self.range = self.max - self.min

        # Quartiles
        self.q1 = np.percentile(x, 25)
        self.q2 = np.percentile(x, 50)
        self.q3 = np.percentile(x, 75)
        self.interquartileRange = self.q3 - self.q1

        self.mean = np.mean(x)
        # Mode (most common number) is a robust measure of central location
        # for nominal level data
        try:
            self.mode = mode(x)
        except StatisticsError as e:
            logging.exception(e)
            # TODO what to do in this scenario? Need to set mode


        # The median is a robust measure of central location for ordinal level
        # data, and is less affected by the presence of outliers in your data.
        # When the number of data points is odd, the middle data point is
        # returned. When the number of data points is even, the median is
        # interpolated by taking the average of the two middle values
        #
        # This is suited for when your data is discrete, and you don’t mind
        # that the median may not be an actual data point.
        #
        # If your data is ordinal (supports order operations) but not numeric
        # (doesn’t support addition), you should use median_low() or
        # median_high() instead.
        self.median = np.median(x)

        if isSample:
            ## Sample Data
            self.stdev = stdev(x)
            # Variance, or second moment about the mean, is a measure of the
            # variability (spread or dispersion) of data. A large variance
            # indicates that the data is spread out; a small variance indicates
            # it is clustered closely around the mean.
            self.variance = variance(x) # == stdev**2
        else:
            ## Population Data
            self.stdev = pstdev(x)
            self.variance = pvariance(x)

        # Pearson's second skewness coefficient (median skewness)
        self.skewCoefficient = 3 * (self.mean - self.median) / self.stdev
        return self


    def getStats(self):

        stats = {'size': self.size, 'mean': self.mean, 'median': self.median, 'mode': self.mode,
                'min': self.min, 'max': self.max, 'range': self.range, 'stdev': self.stdev,
                'variance': self.variance, 'q1': self.q1, 'q2': self.q2, 'q3': self.q3,
                'interquartileRange': self.interquartileRange,
                'skewCoefficient': self.skewCoefficient,}
        return stats


    def printStats(self):

        print("sample size : {}".format(self.size),
              "",
              "Measures of Central Tendancy",
              "-----------------------------",
              "mean :   {}".format(self.mean),
              "median : {}".format(self.median),
              "Quartiles",
              "Q1: {}".format(self.q1),
              "Q2: {}".format(self.q2),
              "Q3: {}".format(self.q3),
              "",
              "Measures of Variability / Spread",
              "---------------------------------",
              "min value :         {}".format(self.min),
              "max value :         {}".format(self.max),
              "range :             {}".format(self.range),
              "Interquartile Range : {}".format(self.interquartileRange),
              "standard deviation: {}".format(self.stdev),
              "variance: {}".format(self.variance),
              "Skew Coefficient: {}".format(self.skewCoefficient),
              "",
              "Misc.",
              "----------",
              "mode: {}".format(self.mode), sep='\n')



class GroupedData(UngroupedData):

    def __init__(self, data, n=None):

        super().__init__(data)

        # if number of bins is not supplied, use Scott's Rules
        if not n:
            n = round(3.5*self.stdev*len(data)**(-1/3))

        # Create Bins array
        self.bins = []
        binSize = round(self.range / n)
        for i in range(0,n+1):
            self.bins.append(self.min + i*binSize)

        # self.mean =
        # self.median =
        # self.mode =
        # self.stdev =
        # self.variance =
