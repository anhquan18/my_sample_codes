class Fighter(object):
    def __init__(self):
        self.name = 'Tanaka'
        self.skill ='swing'
        self.HP = 1000
        self.MP = 200
        self.atk = 20
        self.df = 10
    
    def attack(self):
        print 'swing sword'


class Warrior(Fighter):
    def __init__(self):
        Fighter.__init__(self)
    
    def deffend(self):
        print 'deffend'

    def status(self):  # Can call out the attribute of parrent class
        print '\n'
        for name, value in self.__dict__.items():
            print name, value

    def rage(self):
        self.HP -= 400
        self.atk *= 10
        self.df -=5

if __name__ == '__main__':
    f = Fighter()
    w = Warrior()

    f.attack()

    w.attack()
    w.deffend()

    w.status()
    w.rage()
    w.status()
