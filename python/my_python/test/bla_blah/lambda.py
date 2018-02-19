#lambda help you create anonymous function
g = lambda x: x**2
# g contain the construct of the function create with lambda

#lamda help you return a whole function'construct

def make_func(a, b):
    return lambda y: (y+a)*b

#lambda help you create a function for another function
n_fun = make_func(2, 6)

print n_fun(8)

print make_func(3,10,)(10)

list = [1,2,3,4,5,6,7,8,9,10]

print filter(lambda x: x % 2 == 0, list)
print reduce(lambda x, y: x + y, list)
print map(lambda x: x*2+10, list)

num = range(2, 50)
for i in range(2, 8):
    num = filter(lambda x: x == i or x % i, num)

print num


#change word to length
words = 'It is a beautiful day'.split()
length = map(lambda x: len(x), words)
print length

def find_mount():
    import commands
    # Write like this
    mount = commands.getoutput('mount -v')
    lines = mount.splitlines()
    
    #Or
    lines = commands.getoutput('mount -v').splitlines()
    
    #Or
    points = map(lambda line: line.split()[2], commands.getoutput('mount -v').slitlines())
    print points

find_mount()
