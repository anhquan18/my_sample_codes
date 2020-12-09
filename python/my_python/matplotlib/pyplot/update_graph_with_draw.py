import matplotlib.pyplot as plt
import numpy as np
import random
import time

if __name__ == '__main__':
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)

    #lines, = ax.plot([], [], 'o')
    lines, = ax.plot([], [])
    ax.plot([(-0.25, -0.25), (0.0,0.0)], 'o')

    #print(lines)

    for i in range(10000):
        s = time.time()
        a = [random.random() for i in range(10)]
        b = [random.random() for i in range(10)]

        lines.set_xdata(a)
        lines.set_ydata(b)
        #print(ax.scatter(a, b))

        #ax.relim()
        #ax.autoscale_view()

        fig.canvas.draw()
        fig.canvas.flush_events()

        #ax.draw() 
        
        print(time.time() - s)
        #time.sleep(1.0)
        #fig.canvas.clear()
