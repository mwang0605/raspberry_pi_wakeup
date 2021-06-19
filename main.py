import pygame
import time
pygame.init()
x=1
soundObj = pygame.mixer.Sound('test.wav')
while x<6:
    soundObj.play()
    time.sleep(2)
    x+=1
    soundObj.stop()
