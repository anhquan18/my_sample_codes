# Return a dictionary cotain the global variable

a = ('hi', 10)
b = ('quan', 18)
c = [1,2,3,4]
d = [(100, 12)]


def inside():
    dic = globals()
    print dic


if __name__ == '__main__':
    inside()
