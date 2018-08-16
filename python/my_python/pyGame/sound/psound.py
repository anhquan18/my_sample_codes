import time, pygame
from pygame.locals import *

pygame.init()
soundObj = pygame.mixer.Sound('beep1.ogg')

for x in range(10):
    soundObj.play()
    time.sleep(1)

soundObj.stop()
pygame.quit()
