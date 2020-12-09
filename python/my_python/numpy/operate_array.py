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

    print (A*B)  # elementtwise product also is np.multiply()
    # only in python3.5 and after
    print (A@B) # matrix product        also is np.matmul()
    print (A.dot(B)) # another matrix product

def modify_array():
    a = np.ones((3,4), dtype=int)
    b = np.random.random((3,4))
    a *= 3
    b += a  # Cannot do this cause different type

    print (a)
    print (b)
    a += b
    print (a) 

def modi2():
    a = np.ones(3, dtype = np.int32)
    b = np.linspace(0, np.pi, 3)
    c = a+b
    d = np.exp(c*1j)

    print (c, 'C type is:', c.dtype.name)
    print (d, 'D type is:', d.dtype.name)

def modi3():
    b = np.arange(12).reshape(3,4)

    print (b)
    print (b.sum(axis=0))   # sum of dimension 0
    print (b.sum(axis=1))
    print (b.cumsum(axis=0))# cumulative sum along each row
    print (b.min(axis=1))

if __name__ == '__main__':
    #printing()
    #operation()
    matrix_elementtwise()
    #modify_array()
    #modi2()
    #modi3()
