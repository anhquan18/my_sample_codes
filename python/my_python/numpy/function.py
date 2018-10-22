import numpy as np

def f1():
    a = np.arange(3)
    print (np.exp(a)) # e** over each element
    print (np.sqrt(a)) 

    b = np.array([2., -1., 4.])
    print (b)
    print (np.add(a,b))

    print (a)

def f2(): #Indexing, slicing, iterating
    a = np.arange(10)**3 # each element will be **3
    print (a)
    print (a[2])
    print (a[1:6])
    a[:6:2] = -1000 # every 2 element from 0 to 6 will be changed to -1000
    print (a)
    print (a[::-1]) # reversed

    for num in a:
        print(num **(1/3.))

def f(x, y):
    return 10*x+y

def f3():
    a = np.fromfunction(f, (5,4), dtype=int)
    print(a)
    print(a[2,3])  # access from the outside [] to the inside
    print(a[0:5,1])
    print(a[:, 1])
    print(a[1:3, :])
    print(a[-1])  # last row

def f4():
    '''
    Numpy allow you to use dots( . ) as much as you want to replace a char like below
    array[3,2,....] equavilent to array[3,2,:,:,:,:]
    array[...,3] equavilent to array[:,:,:,:,3]
    array[3,...,2,:] equavilent to array[3,:,:,2,:] '''
    a = np.array([[[0, 1, 2],
                   [10,11,12]],
                  [[100,101,102],
                   [110,111,112]]])
    print (a.shape)  
    print (a[1,...]) # a[1,:,:]
    print (a[...,2]) # a[:,:,2]

def f5():
    a = np.arange(30).reshape(5,6)
    for row in a:
        print (row)

    print('\n')
    for element in a.flat:
        print (element)

if __name__ == '__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    f5()
