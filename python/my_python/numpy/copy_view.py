import numpy as np

''' Some times when oparating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. 
This is often a source of confusion(Ex: a list with two names a = [], b = a/ a list with copy a = [], b =a[:]
'''
def check_id(x): # Python passes mutable objects as references, so function calls make no copy
    print (id(x))

def f1(): # No copy
    a = np.arange(12) # no new object is created
    b = a # a and b are two names for the same ndarray object
    print 'b is a:', b is a
    b.shape = 3,4
    print (a.shape)
    print (id(a)) # id is a unique indentifier of an object
    check_id(a)

def f2(): # View or Shallow copy 
    a = np.arange(12)
    c = a.view()   # construct c as a's data with view, read numpy.ndarray.view document for more detail
    a.shape = 3, 4
    print (a)
    print ('#'*20)
    print ('c is a:', c is a)
    print ('c.base is a:', c.base is a)
    print(c.flags.owndata)
    c.shape = 2,6
    print (a.shape)
    c[0,4] = 1234
    print(a)

    print('#'*20)
    s = a[:, 1:3]  # spaces added for clarity; could also be written "s = a[:,1:3]"
    print(a)
    print (s)
    s[:] = 10
    print (a)

def f3(): # Deep copy
    a = np.arange(12) 
    d = a.copy()

    print('d is a:', d is a)
    print('d based a:', d.base is a)
    
    d[:] = 999
    print(d)
    print(a)

if __name__ == '__main__':
    #f1() 
    #f2()
    f3()
