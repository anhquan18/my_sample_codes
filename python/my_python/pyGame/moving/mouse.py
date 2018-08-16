import pygame
from pygame.locals import *

dis_surf = pygame.display.set_mode((1300, 1000))
pygame.display.set_caption('Moving')
FPS = 45
ge_fps = pygame.time.Clock()

white = (255,255,255)
img = pygame.image.load('Lucio.png')

def main():
    pygame.init()
    
    # mouse
    mox = 0
    moy = 0
    
    while True:
        dis_surf.fill(white)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(1)
            elif event.type == MOUSEMOTION:
                mox, moy = event.pos
        
        dis_surf.blit(img, (mox, moy))
        
        pygame.display.update()
        ge_fps.tick(FPS)

if __name__ == '__main__':
    main()
