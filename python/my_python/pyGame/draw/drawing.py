import pygame, sys
from pygame.locals import *
from math import radians

pygame.init()

# set up the window 
DISPLAYSURF = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255,255,0)

DISPLAYSURF.fill((125,125,125))

# draw on the surface object
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 50, 10, 100))
pygame.draw.arc(DISPLAYSURF, BLUE, (500.0, 500.0, 100, 100), radians(120), radians(420), 50)
pygame.draw.aaline(DISPLAYSURF, RED, (200, 200), (200, 300))

def draw_pacman():
    angle_list = [(radians(45), radians(315)), (radians(30), radians(330)), (radians(15), radians(345)), (radians(0), radians(360))]
    i = 0
    
    for start_angle, end_angle in angle_list:
        print start_angle, end_angle
        pygame.draw.arc(DISPLAYSURF, YELLOW,(500,500, 200,200), start_angle, end_angle, 100)
        pygame.display.update()
        pygame.time.wait(100)
        i+=1

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
    #DISPLAYSURF.fill(BLACK)
    #draw_pacman()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.time.wait(10)
