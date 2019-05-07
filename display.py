import matplotlib.pyplot as plt
import numpy as np

def frequencyDistribution(x, n=None):
    """Creates a histogram displaying a frequency distribution of data.
    Especially useful for Nominal or Ordinal data

       Inputs
       -------
    x : numpy.array object
        The dataset
    n : int
        Number of bins (classes) to use to group the data. If n is
        not supplied, it will be calculated using Scott's Rule
    """
    # x = dataSet (python list)
    # n = number of bins

    # if number of bins is not supplied, use Scott's Rules
    if not n:
        n = round(3.5*self.stdev*len(data)**(-1/3))

    # Create Bins array
    self.bins = []
    binSize = round(self.range / n)
    for i in range(0,n+1):
        self.bins.append(self.min + i*binSize)

    hist, bins = np.histogram(x, bins)
    plt.hist(x, bins, alpha=0.5, ec='black')
    plt.title("histogram")
    plt.show()


def simpleRegression(x, y):
    # number of observations/points
    assert len(x) == len(y), "Datasets must be the same length"

    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
            marker = "o", s = 30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.grid(linestyle='--')
    plt.show()

def main():
    # observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    x = np.array([95,85,80,70,60,])
    y = np.array([85,95,70,65,70])

    # estimating coefficients
    b = simpleRegression(x, y)
    print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()
