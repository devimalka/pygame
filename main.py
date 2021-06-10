import pygame
from pygame import rect
from pygame.locals import *
import Ufunctions

pygame.init()


#screen set

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Project 1")

tile_size = 20

FPS = 60
fpsClock = pygame.time.Clock()

#colors
black =(0,0,0)
white = (255,255,255)


#load images
bg_img = pygame.image.load('img/bg2.jpg')
bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))






#functions

def draw():
    for line in range(0,40):
        pygame.draw.line(screen,white,(0,line * tile_size),(screen_width,line*tile_size))
        pygame.draw.line(screen,white,(line*tile_size,0),(line*tile_size,screen_height))


mapdata = Ufunctions.loadMap('map')


#classes

class Player():
    def __init__(self,x,y):
        self.player_img = pygame.image.load('img/player.png')
        self.player_img = pygame.transform.scale(self.player_img,(20,20))
        self.rect = self.player_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isjump = False
        self.vel_y = -15
        self.v = 5
        self.m = 1
        self.check = 0

    def update(self):
        px = 0
        py = 0
        key = pygame.key.get_pressed()

        if key[K_LEFT]:
            px -= 1
        if key[K_RIGHT]:
            px +=1
        if self.isjump == False:
            if key[K_SPACE]:
                self.isjump = True
               
        if self.isjump:
            py = self.vel_y
            self.vel_y += 1
            if self.rect.y >= screen_height - 40:
                self.rect.y = screen_height - 40
                self.isjump = False
                self.vel_y = -15
        
    
        
        
       
        self.rect.x += px
        self.rect.y += py
        screen.blit(self.player_img,(self.rect.x,self.rect.y))



class World():
    def __init__(self,data):
        self.tile_list = []
       
        grass_img = pygame.image.load('img\grass.png')

        row_count=0
        for row in data:
            col_count = 0
            for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(grass_img,(tile_size,tile_size ))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count *tile_size 
                        tile = (img,img_rect)
                        self.tile_list.append(tile)
                        col_count +=1
                        
            row_count += 1
                
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])







# initializing
player = Player(0,screen_height-40)

world = World(mapdata)








#loop
run = True
while run:
    

    screen.fill(white)
    screen.blit(bg_img,(0,0))
    
    draw()
    world.draw()
    player.update()
    




    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
           

    #always use this to update screen
    pygame.display.update()
    fpsClock.tick(FPS)



pygame.quit()
