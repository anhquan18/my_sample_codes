# A decorator is a function that take one function as input
#and returns another function. When you want to add something to a
#function but you kind of want to keep the source code of that 
#function use a decorator
def document_it(func):
    def new_function(a, b):
        print('Running function:', func.__name__)
        print('Positional arguments:', a, b)
        #print('Keyword arguments:', kwargs)
        result = func(a, b)
        print('Result:', result)
        return result
    return new_function

# when you use add_ints it will become new_func, normally the new function
#add_ints(20, 5)

def new_func(object):
    print 'new func worked'
    def new_object(a,b,*c):
        object(a,b)
        print a*b
        return a*b
    return new_object

@new_func
def add(a,b):
    return a+b

#print add(1,2,3,4,5)


# Do this and the add_ints will become the parameter of the document_it
@new_func
@document_it
def add_ints (a,b):
    print a,b
    return a+b

add_ints(20,5)
