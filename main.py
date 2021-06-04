import pygame
from pygame.locals import *

pygame.init()

screen_height = 720
screen_width = 1280

screen = pygame.display.set_mode((screen_width,screen_height))


#images to load
bg_img = pygame.image.load('img/bg.png')



run = True
while run:
        
        screen.blit(bg_img,(0,0))        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False 

        pygame.display.update()

pygame.quit()