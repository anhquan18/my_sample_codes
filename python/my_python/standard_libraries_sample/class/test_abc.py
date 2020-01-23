import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    id = 1
    # When you use @abc.abstractproperty the property become read-only 
    #and you won't be able to use it 
    @abc.abstractproperty
    def value(self):
        return 'Should not get here'


class Implementation(Base):
    
    @property
    def value(self):
        return 'concrete property'

    @property 
    def r_id(self):
        return self.id


try:
    b = Base()
    print 'Base.value:', b.value
except Exception as err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value
print i.r_id()
