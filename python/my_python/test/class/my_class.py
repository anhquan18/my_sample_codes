import sys

sys.path.append('../')

import check

class Monster(object):
    def __init__(self, lv, hp, dfd, atk = 1):
        self.lv = lv
        self.hp = self.lv * hp
        self.atk = self.lv * atk
        self.dfd = self.lv * dfd 
        self.color = 'green'
        self.rage()
        self.status()
    
    def status(self):
        print ('LV:', self.lv)
        print ('HP:', self.hp)
        print ('ATK:', self.atk)
        print ('DF:', self.dfd)
        print ('COLOR:', self.color)
    
    def rage(self):
        self.atk *= 2
        self.dfd /= 2
        self.color = 'red'
    
    def tired(self):
        self.atk /= 4 
        self.dfd /= 4
        self.color = 'green'
    
class Action(object):
    def roar(self, name):
        print "I'm going to kill you", name


class Alien(Monster):
    class Tail(object):
        def __init__(self, atk, enemy_hp, enemy_def):
            self.atk = atk
            self.enemy_hp = enemy_hp
            self.enemy_def = enemy_def
            print 'Tail worked'
        def swing(self):
            self.enemy_hp -= self.atk - self.enemy_def
            print self.enemy_hp
    # When the child class's function has the same name with the parent class's
    #function the child's one will replace the parent's one, use super() to call
    #the parent's one
    
    # Super cannot use with old style class in python 2 that why if you call out
    #a class like class Monster:, or class Moster(): python will give you an error
    
    # In order to use the super() you have to overriden the function that you are going to
    #call, if you don't do it, python will return error
    def __init__(self, lv, hp, dfd, atk):
        # Do this you can still call out the Alien self.atribute
        Monster.__init__(self,lv, hp, dfd, atk)
        self.action = Action()
        print 'First atk:', self.atk
        print 'Oh, you missed'
        super(Alien, self).status()
        try:
            # This is how you use super() in python3 to compile use python3 
            # file_name.py
            super().__init__(lv,hp,dfd,atk)
        except Exception:
            pass
        self.__tail = self.Tail(self.atk, 4000, 400)
    
    @property
    def tail(self):
        return self.__tail
    
    def introduce(self):
        print ("I'm an alien, Woohoo")
    
    def roar(self, name):
        return self.action.roar(name)


if __name__ == '__main__':
    #slime = Monster(1, 5, 2)
    
    predator = Alien(10, 100, 40, 100)
    # Just want to let you know that when python run the class what will the self
    #be
    #Alien.call(predator)
    predator.tail.swing()
    me = predator
    me.introduce()
    me.roar('Quan')
    print Alien.__name__
    print Alien.__doc__
    print predator.__dict__
    print predator.__class__
    print predator.__class__.__name__

