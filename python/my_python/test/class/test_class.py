class Parent(object):
    def __init__(self, num):
        self.val = 10
        print 'This will run when child receive parent'
        self.num = num
    def show_v(self):
        print self.val


#init will run 
class Child(Parent):
    def show(self):
        print self.val
        print self.num
        Parent.__init__(self, 5)
child = Child(3)
child.show()
child.show()
