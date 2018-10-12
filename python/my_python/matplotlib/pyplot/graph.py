import matplotlib.pyplot as plt
# Numpy array ussually used with matplotlib

if __name__ == '__main__':
    # Plot numbers
    plt.plot([1.0, 2.0, 3.0, 4.0], [2.0, 4.0, 6.0, 8.0], 'green')
    plt.plot([1.0, 3.0, 5.0, 7.0], [10.0, 8.0, 5.0, 2.0])        # x first y later
    plt.plot([10.0, 6.0, 8.0, 20.0, 3.0], 'red')                # one list -> y only
    plt.plot(range(0, 8, 3), 'o--')
    plt.plot(range(4, 20, 4), 'p-')

    # Line properties
    plt.plot(range(1, 10, 2), range(1, 10, 2), 'black', linewidth=4.0) # Linewidth
    lines = plt.plot(1, 5, 2, 6)  # Line 2D object
    print lines
    
    lines[1].set_antialiased(False) # Turn off aliasing
    plt.setp(lines, color='r', linewidth='2.0') # Keyword style
    plt.setp(lines, 'color', 'r', 'linewidth', 2.0) # MATLAB style
    # Read the document for setp
    ''' And a bunch of value for line properties in website document'''

    # Value for axes y first x later
    plt.axis([0., 30., 0., 30.])

    # Label
    plt.ylabel("some numbers")
    plt.xlabel("other numbers")

    plt.show()

