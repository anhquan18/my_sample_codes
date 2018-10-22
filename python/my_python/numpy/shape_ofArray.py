import numpy as np
from numpy import newaxis

def f1():
    a=np.floor(100*np.random.random((3,4)))
    print(a)
    print(a.shape)

def f2(): # This command can change shape but won't modify the array
    a= np.arange(20).reshape(4,5)
    print (a)
    print (a.ravel())         # return the array flattened ( the rightmost index changes the fastest, this is "C-style")
    print(a.reshape(10,2))    # return the modified shape
    print(a.T)                # return the array transposed remmember T in array
    print(a.T.shape)
    print (a.shape)
    ''' If the array is reshaped, again array will be treated as C-style. 
    You can also use FORTRAN-style for reshape and ravel'''

def f3(): # This will modify the array
    a = np.arange(20)
    a.resize(2,10)
    print(a)

def f4():
    a = np.arange(18)
    print(a.reshape(3,-1)) # If a dimension is given -1 the other dimension automatically calculated
    print(a)

def f5(): # Stack over array
    a = np.array([[1,2], [3,4]])
    b = np.array([[8,0], [0,11]])
    c = np.arange(3)
    d = np.arange(3,6)

    print('\n','A:', a.shape, a)
    print('\n','B:', b.shape, b)
    print('\n',np.vstack((a,b)))
    print('\n',np.hstack((a,b)))
    print('\n',np.column_stack((a,b)))
    print('\n',np.column_stack((c,d)))
    print('\n',a[newaxis, :], a[newaxis,:].shape)
    print('\n',a[:, newaxis])  # This allow to have 2D columns vector
    print('\n',b[:,newaxis])
    ''' newaxis help you add another dimension to the arrays 
    1D -> 2D
    2D -> 3D
    3D -> 4D
    array([2, 0, 1, 8])
    A[np.newaxis, :] -> array[[2,0,1,8]] a.shape(1,4) Row vector
    A[:,np.newaxis] -> array[[2],
                             [0],
                             [1],
                             [8]]        a.shape(4,1) Columnvector
    '''
    print(np.column_stack((a[:,newaxis],b[:,newaxis])))
    print(np.hstack((a[:newaxis],b[:,newaxis]))) 


def f6():
    ''' Numpy.r_ have 2 uses:
    1. If the index expression comma separated arrays, then stack them along their first axis
    2. If the index expression contains slice notation or scalars then create a 1-D array with a range indicated by the slice notation.

    If slice notation is used, the syntax start:stop:step is equivalentto np.arange(start, stop, step) inside the brackets.
    However, if step is an imaginary number  then its interger portion is interpred as a number-of-points desired and the start and stop
    are inclusive. In other words start:stop:stepj is interpred as np.linspace(start, stop, step, endpoint=1).After expansion of slice
    notation, all comma sparated sequences are concatenated together.

    Optional character strings placed as the first element of the index expression can be used to change the output. 
    THe strings 'r' or 'c' result in arrays output. If the result is !-D and 'r' is specified a 1 x N(row) arrays is produced.
    If the result is 1-D and 'c' is specified, then a Nx1 (column) arrays is produced. If the result is 2-D 
    then both provide the same arrays result.

    #### The axis in here is the number of dimension of the arrays
    '''
    print(np.r_[np.array([1,2,3]), 0, 0, np.array([4,5,6])])
    print('#'*10) 
    print(np.r_[-1:1:6j,[0]*3, 5, 6])
    a = np.array([[0, 1, 2], [3,4,5]])
    b = np.array([[10, 11, 12], [13,14,15]])
    print('#'*10) 
    print(np.r_['-1', 10*np.sin(a),a,b]) # concatenate along last axis
    print(np.r_['0', 10*np.sin(a),a,b]) # concatenate along last axis
    print(np.r_['1', 10*np.sin(a),a,b]) # concatenate along last axis
    print('#'*10) 
    print(np.r_['0, 2', [1,2,3], [4,5,6]]) # concatenate along first axis , dimension>=2
    print('#'*10) 
    print(np.r_['0,1', [1,2,3],[0, 0, 0], [4,5,6], [7,8,9]]) # you can fix the dimesion of the array by r_ which is pretty powerfull
    print('#'*10) 
    print(np.r_['0,2', [1,2,3],[0, 0, 0], [4,5,6], [7,8,9]]) # you can fix the dimesion of the array by r_ which is pretty powerfull
    print('#'*10) 
    print(np.r_['0,3', [1,2,3],[0, 0, 0], [4,5,6], [7,8,9]]) # you can fix the dimesion of the array by r_ which is pretty powerfull
    print('#'*10) 
    print(np.r_['0,4', [1,2,3],[0, 0, 0], [4,5,6], [7,8,9]]) # you can fix the dimesion of the array by r_ which is pretty powerfull
    '''Read more about the concatenate function '''
    print('#'*10) 
    print(np.c_[np.array([1,2,3]), np.array([4,5,6])])
    print('#'*10) 
    print(np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]) # column stack
    print('#'*10) 
    print(np.r_['0,2,0', [1,2,3], [4,5,6]])
    print('#'*10) 
    print(np.r_['1,2,0', [1,2,3], [4,5,6]])
    print('#'*10) 
    print(np.r_['r', [1,2,3], [4,5,6]]) # use 'r' or 'c' as first argument to create matrix

def f7(): # Split array
    a = np.floor(10*np.random.random((2,12))) 
    print(a)
    print(np.hsplit(a,3)) # Split into 3 array
    print(np.hsplit(a,(3,4))) # Split a by third and fourth column
    print(np.hsplit(a,(2,5,7))) # Split a by second and fifth and senventh column
    # And we have vsplit for vertical as well and array_split allows one to specify along which axis to split

if __name__=='__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    #f5()
    #f6()
    f7()
