# Function can be a parameter of a function in python. Why, because 
#everything inside python is an object. We always attach the 
#orenthese to the function this one '()', why, because in python it
#mean call the function it was attached to, without orenthese, the 
#function in python are just data of an object like everything else
#like var, arg, str, int, ...

def output(name):
    print 'Hello', name

def run_func(func, y_name):
    func(y_name)

def outer(str):
    def inner(words):
        return 'Why would we do this'+words
    return inner(str)

def func(str):
    # Functinon that can change and remember the val created outside
    #the function
    def closure():
        return 'This how closure work'+str
    return closure


#But normally you won't do it because you can use the function from
#the scope
if __name__=='__main__':
    #run_func(output, 'Quan')
    
    #print outer('It is for the complex tasks inside a function')
    
    a = func('function')
    b = func('a thing')
    print a
    print a()
    print b
    print b()
