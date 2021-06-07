import pygame
from pygame.locals import *

pygame.init()


# screen
screen_height = 720
screen_width = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Project 1")






#images to load
bg_img = pygame.image.load('img/bg.png')
scaled_img = pygame.transform.scale(bg_img,(screen_width,screen_height))


# world variables
tile_size = 20


def draw_grid():
    for line in range(0,95):
        pygame.draw.line(screen, (255,255,255),(0, line * tile_size),(screen_width, line * tile_size))
        pygame.draw.line(screen,(255,255,255),(line * tile_size, 0), (line * tile_size, screen_height))



def loadmap(path):
    map_array = []
    splited = []
    file = open(path+'.txt','r')
    data = file.read()
    data = data.split('\n')
    for line in data:
        for i in line:
            splited.append(int(i))
        map_array.append(splited)
        splited = []
            

    return map_array



game_map = loadmap('map')


#classed
class Player():
    def __init__(self,x,y):
        self.player_img = pygame.image.load('img/player.png')
        self.player_img = pygame.transform.scale(self.player_img,(30,50))
        self.rect = self.player_img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        py = 0
        px = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            px -= 1
        if key[pygame.K_RIGHT]:
            px += 1
        

        self.rect.x += px
      #  self.rect.y += px

        screen.blit(self.player_img,(self.rect.x,self.rect.y))


class World():
    def __init__(self,data):
        self.tile_list = []
        grass_img = pygame.image.load('img/grass.png')

        row_counter = 0
        for row in data:
            col_counter = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(grass_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * tile_size
                    img_rect.y = row_counter * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
            col_counter+=1
        row_counter+=1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])


#initializing
player = Player(0,screen_height-50)

maped = loadmap('map')
world = World(maped)

#run
run = True
while run:
        
        screen.blit(scaled_img,(0,0)) 
     
        player.update()   
        world.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False 

        pygame.display.update()

pygame.quit()
