# x18382503



import pygame
import os
import sys
import random

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)
RED   = (255,   0,   0)


class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1,8):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

'''
Setup
'''
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
fps = 60       # frame rate
clock = pygame.time.Clock()
pygame.init()
main = True

block_list = pygame.sprite.Group()

# list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(Player())


# Used to manage how fast the screen updates
clock = pygame.time.Clock()



world = pygame.display.set_mode([screen_width,screen_height])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropbox = world.get_rect()
player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)


'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False



    # Get the current mouse position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
    # Same way you can fetch letters out of a string
    # Set the player object to follow mouse positioning\\
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    world.fill(BLUE)
    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world) #refresh player position
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
