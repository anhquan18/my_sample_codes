import numpy as np
import matplotlib.pyplot as plt

def graph():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50 , normed=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probabbility')
    plt.title('HIstogram of IQ')

    # r will turn string into raw string -> disable the \ in python meaning
    plt.text(60, .025, r'$\mu=100,  \sigma=15$') # text written inside $$ and have \ will turn into mathematical sign 
    plt.text(60, .015, r'$\sigma_i = 15$')

    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

def annonate():
    # annonate
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line , = plt.plot(t, s, lw=2)
    plt.annotate('local max', xy=(3, 1), xytext=(4, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.ylim(-2.2)

    ''' There are basic and advance annotation tutorial in the website so if you want to learn more about annotation
        just search it in pyplot tutorial'''
        

if __name__ == '__main__':
    annonate()
    plt.show()
