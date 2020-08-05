import pygame
import os

os.chdir('C:/Users/natha/Desktop/ITP Group Project/Monkey Motion')

pygame.init()

display_width = 1200
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (200,0,0)
green = (0,255,0)
bright_green = (0,220,0)
blue = (0,0,255)
light_blue  = (0,100,220)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Monkey Motion')
clock = pygame.time.Clock()

pygame.mixer.music.load('Menu Music.mp3')
pygame.mixer.music.play(-1)

monImg = pygame.image.load('image/monkey.png')

crashed = False

def mon(x,y):
    gameDisplay.blit(monImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(light_blue)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Monkey Motion", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        button("Start",300,450,100,50,green,bright_green,game_loop)
        button("Quit",800,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause

game_intro()
pygame.quit()
quit()
