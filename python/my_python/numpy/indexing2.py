import numpy as np


def f1(): # THe ix_() function
    ''' The Ix_() function can be used to combined different vectors so as to obtain the result
    for each n-uplet. For example, if you want to compute all the a+b*c for all the triplets taken from each of 
    the vectors a, b and c:'''

    a = np.array([2,3,4,5])
    b = np.array([8,5,4])
    c = np.array([5,4,6,8,3])
    ax, bx, cx = np.ix_(a, b, c)

    print ax
    print '#'*10
    print bx
    print '#'*10
    print cx
    print '#'*10
    print ax.shape, bx.shape, cx.shape

    result = (ax + bx * cx)

    print (ax + bx * cx)
    print result[3,2,4]
    print a[3] + b[2] * c[4]

    print '#'*10
    print ufunc_reduce(np.add, a, b, c)

'''You can also implement the reduce as follows:'''
def ufunc_reduce(ufct, *vectors): # Seach more about this to understand later
    vs = np.ix_(*vectors)
    r = ufct.identity
    print 'r', r
    for v in vs:
        r = ufct(r,v)
    return r


if __name__ == '__main__':
    f1()
