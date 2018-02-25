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


class Alien(Monster):
    # When the child class's function has the same name with the parent class's
    #function the child's one will replace the parent's one, use super() to call
    #the parent's one
    # Super cannot use with old style class in python 2 that why if you call out
    #a class like class Monster:, or class Moster(): python will give you an error
    def __init__(self, lv, hp, dfd, atk):
        Monster.__init__(self,lv, hp, dfd, atk)
        Monster.tired(self)
        super(Alien, self).status()
        try:
            # This is how you use super() in python3 to compile use python3 
            # file_name.py
            super().__init__(lv,hp,dfd,atk)
        except Exception:
            pass
    def call(self):
        print ("I'm an alien, Woohoo")


class


def main():
    slime = Monster(1, 5, 2)
    
    predator = Alien(10, 100, 40, 100)
    # Just want to let you know that when python run the class what will the self
    #be
    Alien.call(predator)


if __name__ == '__main__':
    main()
