class Parent(object):
    def __init__(self, num = 0):
        self.val = 10
        print 'This will run when child receive parent'
        self.num = num
        self.__yell = self.Yell()
        self.__number = 9
    
    def number(self):
        return self.__number
    
    @property
    def yell(self):
        return self.__yell
    
    def show_v(self):
        print self.val
    
    class Yell(object):
        def action(self):
            print 'Hey what are you doing'


#init will run 
class Child(Parent):
    def __init__(self):
        Parent.__init__(self, 5)
        if Parent.
        self.__id = 1
    def show(self):
        print self.val
        print self.num
        child.yell.action()
    @property
    def id(self):
        return self.__id

class Boy(Parent):
    def tell(self, a_num):
        Parent.__init__(self, a_num)
        print self.num
        print self. val
        #You can't receive secret variable from parent class but you can do this
        #print self.__number
    def number(self):
        return Parent.number(self)


child = Child()
child.show()
child.show()
if child.id:
    print child.id

boy = Boy()
boy.tell(4)
print boy.number()
