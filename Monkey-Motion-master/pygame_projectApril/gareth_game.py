
#x18382503



import pygame
import sys
import os
import random
import math


'''
Objects
'''

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # The "center" the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        # Current angle in radians
        self.angle = 0

        # How far away from the center to orbit, in pixels
        self.radius = 0

        # How fast to orbit, in radians per frame
        self.speed = 0.05

    def update(self):

        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y

        self.angle += self.speed

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('images','hero2.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()


    def control(self,x,y):

        self.movex += x
        self.movey += y

    def update(self):
        #pos = pygame.mouse.get_pos()
        #self.rect.x = pos[0]
        #self.rect.y = pos[1]
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

'''
Setup
'''
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

fps = 60       # frame rate
clock = pygame.time.Clock()
pygame.init()
main = True

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
#backdropbox = screen.get_rect()
player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10      # how fast to move

block_list = pygame.sprite.Group()

#List of every sprite
all_sprites_list = pygame.sprite.Group()

for i in range(20):
    # This represents a block
    block = Block(WHITE, 20, 30)

    # Set a random center location for the block to orbit
    block.center_x = random.randrange(SCREEN_WIDTH)
    block.center_y = random.randrange(SCREEN_HEIGHT)
    # Random radius
    block.radius = random.randrange(10, 200)

    block.angle = random.random() * 2 * math.pi

    block.speed = 0.008

    # Add the block to object list
    block_list.add(block)
    all_sprites_list.add(block)
    all_sprites_list.add(Player())



# Loop until closed
main = True

# Manages how fast the screen updates
clock = pygame.time.Clock()

score = 100

'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

        all_sprites_list.update()

        # Set player block collisions
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # Check the list of collisions.
        for block in blocks_hit_list:
            score -= 5
            print( score )






    screen.blit(backdrop, (0,0))

    block_list.update()
    block_list.draw(screen)
    player_list.draw(screen) #refresh player position
    player.update()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
