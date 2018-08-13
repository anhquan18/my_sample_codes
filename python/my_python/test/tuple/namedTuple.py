import collections

Point = collections.namedtuple('corrdinate', ['x', 'y'])

cord = Point(10, 20)

print cord.x, cord.y
print 'docstring', cord.__doc__
print 'named tuple', cord.__str__()
