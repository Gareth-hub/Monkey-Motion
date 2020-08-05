# Importing the module(s)
import pygame, os, random, sys, math

# Centering the Window when it appears onscreen
os.environ['SDL_VIDEO_CENTERED'] = '1'
os.chdir("D:\Programming\Monkey Motion\Sorin Blitz")

# Initializing Pygame
pygame.init()

# Creating the Window
displayHeight = 650
displayWidth = 1400
screen = pygame.display.set_mode((displayWidth, displayHeight))

# Title of the Game
pygame.display.set_caption("Monkey Motion")

# Sprites
cloudImg = pygame.image.load('images/bigcloud.png')	# Cloud
bananaImg = pygame.image.load('images/banana.png')

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
		if cloud_y > displayHeight and cloud_y2 > displayHeight:				# Re-assigns random numbers for the x co-ordinates
				cloud_x = random.randint(-20, displayWidth-800)
				cloud_x2 = random.randint(750, displayWidth-450)
				cloud_y = random.randint(-288, -211)
				cloud_y2 = random.randint(-288, -211)

# Gary's code
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()
        self.images = []
        img = pygame.image.load(os.path.join('images','unhero2.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()

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
        img = pygame.image.load(os.path.join('images','hero.png'))
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

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)
score = 100

player = Player()
player.rect.x = 20 # these control where
player.rect.y = 100 # the player appears on screen
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10      # how fast to move

block_list = pygame.sprite.Group()

#List of every sprite
all_sprites_list = pygame.sprite.Group()

for i in range(random.randint(2,4),(random.randint(5,9))):
    # This represents a block
    block = Block(WHITE, 20, 30)

    # Set a random center location for the block to orbit
    block.center_x = random.randrange(displayWidth)
    block.center_y = random.randrange(displayHeight)
    # Random radius
    block.radius = random.randrange(10, 200)

    block.angle = random.random() * 2 * math.pi

    block.speed = 0.008

    # Add the block to object list
    block_list.add(block)
    all_sprites_list.add(block)
    all_sprites_list.add(Player())


# Running the game as it continuously
running = True
while running:
	screen.fill((64,102,209)) # Background colour
	# Event Handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False					# Closes game when window is closed

		# Gary's Code
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

	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

	for block in blocks_hit_list:
		score -= 5
		print(score)

	# Calling sprite functions
	cloud()
	block_list.draw(screen)
	player_list.draw(screen)
	block_list.draw(screen)
	player.update()
	block_list.update()
	pygame.display.update()

	clock = pygame.time.Clock()
	FPS = 60
	clock.tick(FPS)
pygame.quit()
