import numpy as np


def sample():
    print 'hello'
    a = numpy.arange(20).reshape(4,5)
    b = numpy.array([5,6,7])

    print a
    print a.ndim
    print a.dtype.name
    print a.itemsize
    print a.size
    print type(a)

    print b
    print type(b)

def create_array():
    a1 = np.array([2,3,4])                         # 1 dimensional
    a2 = np.array([1.2,3.4,5.6])
    b = np.array([(1.5, 2, 3), (4,5,6)])           # 2 dimensional <- sequences of sequences
    c = np.array([ [1,2], [3,4] ], dtype=complex)  # type of array can be initial
    d = np.mgrid[0:4, 7:10]                        # create two matrix with row size decided by the first array and 
    x1, y1 = np.meshgrid(np.arange(1, 11, 2), np.arange(-12, -3, 3)) # almost work like mgrid
    x2, y2 = np.ogrid[1:11:2, -12:-3:3]
    x3, y3 = np.broadcast_arrays(x2, y2)           # Act like mgrid, create two new matrix with the row size of first matrix and col size of second matrix
    rand = np.random.rand(3,2)                     # Randomly create array list

    print a1
    print a1.dtype

    print a2.dtype
    print b
    print c
    print d
    print x1, y1
    print x2, y2
    print rand

def initial_array():
    zero = np.zeros((3,4))
    one = np.ones( (2,3,4), dtype=np.int16 )
    vary = np.empty( (2,3) )    # Return an array of given shape and type without initialize 

    print zero
    print one
    print vary

def sequences():
    se = np.arange(10, 30, 5) # simialar to range but create array
    fl = np.arange(0, 2, 0.3)
    ''' when arange is used with floating arguments, it is hard to predict the number of elements obtained, 
    due to the finite floating point precision. That is why we have linspace that receive the amount of argument
    we want'''

    lin = np.linspace(0, 2, 9) # 9 numbers from 0 to 2
    x = np.linspace(0, 2*3.14, 100) # useful to evaluate function at lots of points
    fu = np.sin(x)

    print se
    print fl

    print 'linspace: ', lin
    print x
    print fu

if __name__ == '__main__':
    create_array()
    #sample()
    #initial_array()
    #sequences()
