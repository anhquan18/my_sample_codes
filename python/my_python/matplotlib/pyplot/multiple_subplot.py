import matplotlib.pyplot as plt
import numpy as np

def fig(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211) # number of rows 2, number of cols 1, figure 1
plt.plot(t1, fig(t1), 'bo', t2, fig(t2), 'k')

plt.subplot(212) # number of rows 2, number of cols 1, figure 2
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()
