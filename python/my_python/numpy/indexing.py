import numpy as np

'''In order to understand all of this indexing you need to read the document about broadcasting rules'''

def f1(): # Indexing with Arrays of Indies
    a = np.arange(12)**2
    i = np.array( [1,1,3,8,5])  # an array of indices
    print 'a[]:'
    print a

    print 'a[i]:'
    print(a[i]) # the element of a at position i

    j = np.array([ [3,4], [9,7] ]) # a bidimensional array of indices

    print 'a[j]:'
    print a[j]

def f2():
    '''When indexed array a is multidimensional, a single array of indices refers to the first dimension of a.
    THe following example shows this behavior by converting an image of labels into a color image using a palette
    '''
    palette = np.array([ [0,0,0],           # Black
                         [255, 0, 0],       # Red
                         [0, 255, 0],       # Green
                         [0, 0, 255],       # Blue
                         [255,255,255] ])   # WHite
    image = np.array( [ [0, 1, 2, 0],   # each value corresponds to a color in the palette
                        [0, 3, 4, 0] ] ) 

    # After each ',' the next element of the array will turn into a row ( a dimension), and each element inside the element-list will
    #be a column

    print 'palette[image]:'
    print palette[image]  
    print palette[image].shape

def f3():
    '''We can also give indexes for more than one dimension. the array of indices for each dimension must have the same shape'''
    a = np.arange(12).reshape(3,4)
    i = np.array([ [0,1],
                   [1,2] ])
    j = np.array([ [2,1],
                   [3,3] ])
    l = [i, j]

    print a
    print 'a[i,j]'
    print a[i,j]
    print 'a[i,2]:'
    print a[i,2]
    print 'a[:,j]:'
    print a[:,j]
    print 'a[l]'
    print a[l]
    ''' You can't put i and j into an array, because this array will be interpreted as indexing the first dimension of a 
    Ex: s = np.array([i,j])
        a[s] -> Index error: index(3) out of range(0<=index<=2) in dimension 0 
        a[tuple(s)] # same as a[i,j] '''

def f4(): # Another  common use of indexing with arrrays is the search  of the maximum value of time-dependent series
    time = np.linspace(20, 145, 5) # time scale
    data = np.sin(np.arange(20)).reshape(5,4) # 4 time-dependent series
    ind = data.argmax(axis=0)                 # Index of the maxima for each series / axis 0 is col and 1 is row
    time_max = time[ind]                      # time correspondng to the maxima
    data_max = data[ind, range(data.shape[1])]# -> data[ ind[0],0 ], data[ ind[1],1 ]

    print(time)
    print(data)
    print(ind)
    print time_max
    print data_max
    print np.all(data_max == data.max(axis=0))
    ''' You can also use indexing with arrayss as a target to assign to:
    a = np.arange(5)
    a[[1,3,4]] = 0
    a -> array([0,0,2,0,0])
    However when the list of indices contains repetitions, the assignment is done several times, leaving behind the last value
    a[[0,0,2]] = [1,2,3]
    a -> array([2,1,3,3,4])
    
    Watch out if you want to use Python's += construct, as it may not do what you expect:
    a[[0,0,2]] += 1
    a -> array([1,1,3,3,4])
    Eventhough 0 occur twice in the list of indices, the 0th elemnt is only incemented once. This is becaus Python requires 
    "a +=1" to be equivalent to "a = a + 1". '''

def f5(): # Indexing with Boolean Arrays
    ''' When we index arrays with arrays of integer incdeices we are providing the list of indices to pick.
    With boolean indices the approach is different; we explicity choose which items in the array we want and which ones we don't
    The most natural way one can think of for boolean indexing is to use boolean arrays that have the same shape shapes as the origianal
    array:'''
    a = np.arange(12).reshape(3,4)
    b = a > 4
    
    print a
    print 'a > 4'
    print b
    print 'a[b]:'
    print a[b]

    ''' THis property can be very useful in assignments:'''
    a[b] = 0
    print a

def f6(): 
    '''The second way of indexing with booleans is more similar to integer indexing for each dimension of 
    the array we give a 1 D boolean array selecting the slices we want '''
    a = np.arange(12).reshape(3,4)
    b1 = np.array([False,True,True])  # first selection
    b2 = np.array([True,False,True,False]) # second selection

    print a[b1,:] # selecting array
    print a[b1]   # samething
    print a[:,b2] # selecting columns
    print a[b1,b2]# a weird thing to do

if __name__ == '__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    #f5()
    f6()
