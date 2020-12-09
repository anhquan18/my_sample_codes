import pygame, time
from pygame.locals import *

pygame.init()

def music():
    # Loading and playing background music:
    pygame.mixer.music.load('we_were_born_to_make_history.mp3')
 
    pygame.mixer.music.play(1 , 0.0)
    time.sleep(92)
 
    print 'Start quiting'
    # ...some more of your code goes here...
    pygame.mixer.music.stop()
    pygame.quit()

def main():
    music()

if __name__ == '__main__':
    main()
