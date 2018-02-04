class Monster:
    def __init__(self, lv, hp, dfd, atk = 1):
        self.lv = lv
        self.hp = self.lv * hp
        self.atk = self.lv * atk
        self.dfd = self.lv * dfd 
        self.color = 'green'
        self.rage()
        self.status()
    
    def status(self):
        print 'LV:', self.lv
        print 'HP:', self.hp
        print 'ATK:', self.atk
        print 'DF:', self.dfd
        print 'COLOR:', self.color
    
    def rage(self):
        self.atk *= 2
        self.dfd /= 2
        self.color = 'red'
    
    def tired(self):
        self.atk /= 4 
        self.dfd /= 4
        self.color = 'green'



def main():
    slime = Monster(1, 5, 2)
    slime.rage()
    slime.status()


if __name__ == '__main__':
    main()
