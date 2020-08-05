# Importing the module(s)
import pygame, os, random

# Centering the Window when it appears onscreen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initializing Pygame
pygame.init()

# Creating the Window
displayHeight = 650
displayWidth = 1400
screen = pygame.display.set_mode((displayWidth, displayHeight))

# Title of the Game
pygame.display.set_caption("Monkey Motion")

# Sprites
cloudImg = pygame.image.load('bigcloud.png')	# Cloud
cloud_y = random.randint(-288, -211)
cloud_y2 = random.randint(-288, -211)
cloud_x = random.randint(-20, displayWidth-800)
cloud_x2 = random.randint(750, displayWidth-450)

# Cloud Scrolling
def cloud():
		global cloud_y
		global cloud_x
		global cloud_x2
		global cloud_y2
		screen.blit(cloudImg, (cloud_x, cloud_y))
		screen.blit(cloudImg, (cloud_x2, cloud_y2))
		cloud_y += 4
		cloud_y2 += 4
		if cloud_y > displayHeight and cloud_y2 > displayHeight:
			for x in range(2):				# Re-assigns random numbers for the x co-ordinates
				cloud_x = random.randint(-20, displayWidth-800)
				cloud_x2 = random.randint(750, displayWidth-450)
				cloud_y = random.randint(-288, -211)
				cloud_y2 = random.randint(-288, -211)

# Running the game as it continuously
running = True
while running:
	screen.fill((64,102,209)) # Background colour

	# Event Handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False					# Closes game when window is closed

	# Calling sprite functions
	cloud()

	pygame.display.update()

	clock = pygame.time.Clock()
	FPS = 60
	clock.tick(FPS)
pygame.quit()
