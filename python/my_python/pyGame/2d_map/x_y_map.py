import sys
from commands import getoutput as gput
from random import shuffle

x_max = 3
y_max = 4
x_min = 0
y_min = 0

w = 'w'
a = 'a'
s = 's'
d = 'd'
q = 'q'

purple = '\033[1;35m'
yellow = '\033[1;33m'
red = '\033[1;31m'
reset = '\033[1;37m'

ap = 'apple'
eg = 'egg'

def info():
    print reset+'YOU have to find the apple to win the game'
    print'   MOVE: use "w" to go up'
    print'         use "s" to go down'
    print'         use "a" to go left'
    print'         use "d" to go right'
    print'   EXIT: use "q" to exit the game'
    print' The game will be terminated if you go outside of the map\n'  


def create_map():
    items = []
    items.append(ap)
    for i in range(11):
        items.append(eg)
    
    shuffle(items)
    
    gmap = []
    for x in range(x_max):
        rows = []
        for y in range(y_max):
            rows.append(items[0])
            del items[0]
        gmap.append(rows)
    return gmap


def main():
    print gput('clear')
    x_cor = x_min 
    y_cor = y_min
 
    info()
    game_map = create_map()
    print game_map
 
    # game loop
    while True:
        direction = input (reset+'>>> input direction: ')
        
        if direction == 'w':
            if y_cor == y_max:
                print purle+'There is a wall forward'        
            else:
 	 	 	    y_cor += 1  
        elif direction == 's':
            if y_cor == y_min:
                print purple+'There is a wall backward'
            else:
 	 	 	    y_cor -= 1
        elif direction == 'd':
            if x_cor == x_max:
                print purple+'There is a wall on your rightside'
            else:
 	 	 	    x_cor += 1
        elif direction == 'a':
            if x_cor == x_min:
                print purle+'There is wall on your leftside'
            else:
 	  	 	    x_cor -= 1
        elif direction == 'q':
            sys.exit(1)
        else:
            print red+'ERROR: Please input the right key'+reset
        
        position = game_map[x_cor][y_cor]
        
        if position == 'apple':
            print reset+'GOAL!!!'
            print 'You found an', red+'apple'+reset
            sys.exit(1)
        else:
            print reset+'You found an', yellow+'egg'+reset
            print '\n'


if __name__ == '__main__':
    main()
