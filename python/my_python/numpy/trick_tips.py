import numpy as np
import matplotlib.pyplot as plt

# Automatic reshaping
def f1():
    a = np.arange(30)
    a.shape = 2,-1,3 # -1 mean whatever is needed
    print a.shape

# Vector stacking 
def f2():
    x = np.arange(0, 10, 2)
    y = np.arange(5)
    m = np.vstack([x,y])

    print m
    
    xy = np.hstack([x,y])

# Histogram
'''THe NumPy histogram function applied to an array returns a pair of vectors: the histogramof the array and the vector of bins
Beware: matplotlib also has a function to build histograms(called "hist", as in Matlab) that differs from the one in NumPy.
The main difference is that pylab.hist plots the histogram automatically while numpy.histogram only generates the data'''

# Build a vector of 10000 normal deviates with variance 0.5*2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)

def f3():
    # Plot a normalized histogram with 50 bins
    plt.hist(v, bins=50, density=1)  # matplotlib version (plot)
    plt.show()

def f4():
    # Compute the histogram with numpy and then plot it
    (n, bins) = np.histogram(v, bins=50, density=True) # NumPy version (no plot)
    plt.plot(.5*(bins[1:]+ bins[:-1]), n)
    plt.show()


if __name__ == '__main__':
    #f3()
    f4()
