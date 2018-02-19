# Execute help you execute the python code inside a python file
exec('print len([1,3,4,5])') # the argument for exec is str or function or code

code = """
def func(a):
    a += 10
    print a
"""

exec code
func(2)
