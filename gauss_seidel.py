import sys
import matplotlib.pyplot as pyplot

def gauss_seidel(x1, x2, x3):
    x1 = (10.0 - x2 - x3)/5.0
    x2 = (12.0 - x1 - x3)/4.0
    x3 = ( 13.0 - 2.0*x1 - x2)/3.0
    return x1, x2, x3

def get_array():
    list = []
    for num in range(int(sys.argv[1])):
        list.append(map(float,raw_input().split(' ')))
    return list

if __name__ == '__main__':
    list1 = []
    list2 = []
    list3 = []
    x1 = x2 = x3 = 10.0

    for i in range(20):
        list1.append(x1)
        list2.append(x2)
        list3.append(x3)

        x1, x2, x3 = gauss_seidel(x1, x2, x3)
    
    pyplot.plot(list1, 'blue', list2, 'red', list3, 'green')
    pyplot.show()
