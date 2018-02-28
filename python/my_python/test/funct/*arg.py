# Remmeber python don't have pointer


# If you give a parameter a *  it will group all the parameters 
#received into a tuple
def p_tup(*arg):
    print 'This will turn into a tuple:', arg


def output(ar1, ar2, *rest):
    print 'first:', ar1
    print 'second', ar2
    print 'the rest', rest


# If you give it two it will ... into a dictionary
#The argument's name will be the keys and the value will be value
#kwargs will be the dictionary's name
def p_kwargs(**kwargs): # Print keyword argument
    print ('Keyword arguments:', kwargs)


if __name__ == '__main__':
    #p_tup(1,2,3,'Hello', 'Hi')
    #output('Hello', "I'm Quan", 12,3,4,5,6)
    
    p_kwargs(wine='wiskey',fruit='apple',age=20,anime='KonoSuba')
    p_kwargs(winner='me',fry='chicken',aniver=20,studio='MadHouse')
