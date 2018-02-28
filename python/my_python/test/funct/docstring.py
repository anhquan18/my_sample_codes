# Attach a documentation inside of a functino will create  the 
#function docstring (those str come out when you use help())
# You can see the raw docstring with print function_name.__doc__
def output(*arg):
    '''Print all of the args that the parameter received and 
    turn them all into a tuple'''
    print arg

output('whatever','whoever')
