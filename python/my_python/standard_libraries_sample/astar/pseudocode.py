import math


def mahatan_dis(point1, point2):
    x1,y1, x2,y2 = point1, point2
    return abs(x1 - x2) + abs(y1 -y2)


def euclucidian_dis(point1, point2):
    x1,y1, x2,y2 = point1, point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def a_star():
    pass


class Node(object):
    def __init__(self, cord):
        self.x, self.y = cord
        self.f_val = None
        self.g_val = None
        self.h_val = None

    
