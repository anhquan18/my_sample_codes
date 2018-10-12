import numpy as np


def printing():
    one = np.arange(6)
    two = np.arange(12).reshape(4,3)
    three = np.arange(24).reshape(2,3,4)

    print (one)
    print (two)
    print (three)
    print (np.arange(10000).reshape(100, 100))

def operation():
    a =  np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a - b

    print (c)
    print (b**2)
    print (10*np.sin(a))
    print (a<35)

def matrix_elementtwise():
    A = np.array([[1,1], [0,1]])
    B = np.array([[2,0], [3,4]])

    print (A*B)  # elementtwise product
    # only in python3.5 and after
    print (A@B) # matrix product
    print (A.dot(B)) # another matrix product

if __name__ == '__main__':
    #printing()
    #operation()
    matrix_elementtwise()

