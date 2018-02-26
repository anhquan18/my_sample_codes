#This abc help you define an abstract of a class to help you remmber the role of a class and what
#are those function stand for
import abc  

class M_abc(object):
    __metaclass__ = abc.ABCMeta

M_abc.register(tuple) 

assert issubclass(tuple, M_abc)
assert isinstance((), M_abc)
