import pygame
pygame.init()



#win param
windowWidth = 1280
windowHeight = 720
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Wizzy's Quest")
bg = pygame.image.load('homeworld.jpg')

#fps
clock = pygame.time.Clock()
#hit score
score = 0
#sfx
bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')
dmgReceived = pygame.mixer.Sound('water_hit.wav')
#ost
music = pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)                #music play loop
#player param
death = False
#----------------------------------------------------------------------------------------
#main character
class player(object):
	walkRight = [pygame.image.load('Wizzy_R1.png'), pygame.image.load('Wizzy_R2.png'), pygame.image.load('Wizzy_R3.png'), pygame.image.load('Wizzy_R4.png'), pygame.image.load('Wizzy_R5.png'), pygame.image.load('Wizzy_R6.png'), pygame.image.load('Wizzy_R7.png'), pygame.image.load('Wizzy_R8.png')]
	walkLeft = [pygame.image.load('Wizzy_L1.png'), pygame.image.load('Wizzy_L2.png'), pygame.image.load('Wizzy_L3.png'), pygame.image.load('Wizzy_L4.png'), pygame.image.load('Wizzy_L5.png'), pygame.image.load('Wizzy_L6.png'), pygame.image.load('Wizzy_L7.png'), pygame.image.load('Wizzy_L8.png')]
	idle = pygame.image.load('Wizzy_R.png')
	direction = [pygame.image.load('Wizzy_R.png'), pygame.image.load('Wizzy_L.png')]
	life = [pygame.image.load('Life.png'), pygame.image.load('Life.png'), pygame.image.load('Life.png')]
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 10
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0
		self.standing = True
		self.hitbox = (self.x + 10, self.y + 15, 45, 50) #hitbox position
		self.hp = 2 #hp = 3
		self.visible = True
		self.heart = True
		self.life_amount = 3

	def draw(self, win):
		if self.visible:
			if self.walkCount + 1 >= 24:
				self.walkCount = 0

			if not(self.standing):
				if self.left:
					win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
					self.walkCount = self.walkCount + 1
				elif self.right:
					win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
					self.walkCount = self.walkCount + 1	

			else:
				if self.right:
					win.blit(self.direction[0], (self.x, self.y))
				else:
					win.blit(self.direction[1], (self.x, self.y))
			#hitbox drawing
			self.hitbox = (self.x + 10, self.y + 15, 45, 50)
			#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
			#pygame.draw.rect(win, (255,0,0), (self.hitbox[0] + 8, self.hitbox[1] - 2, 30, 5))   #hp bar parameters
			#pygame.draw.rect(win, (0,255,0), (self.hitbox[0] + 8, self.hitbox[1] - 2, 30 - ((30/3) * (2 - self.hp)), 5)) #hp loss display
			if self.life_amount == 3 and self.heart == True:
				win.blit(self.life[0], (10,10))
				win.blit(self.life[1], (50,10))
				win.blit(self.life[2], (90,10))
			elif self.life_amount == 2 and self.heart == True:
				win.blit(self.life[0], (10,10))
				win.blit(self.life[1], (50,10))
			elif self.life_amount == 1 and self.heart == True:
				win.blit(self.life[0], (10,10))
			elif self.life_amount > 3 and self.heart == True:
				win.blit(self.life[0], (10,10))
				win.blit(self.life[1], (50,10))
				win.blit(self.life[2], (90,10))
			else:
				self.heart == False

		else:
			death = True
			self.visible = False
			hitFont = pygame.font.SysFont('verdana', 30, True)
			hitText = hitFont.render('You Died', 1, (255,0,0))
			win.blit(hitText, ((windowWidth/2) - (hitText.get_width()/2), 330)) #screen text position
			pygame.display.update()
			delay = 0
			while delay < 10:
				pygame.time.delay(10)
				delay = delay + 1
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						delay = 11
						pygame.quit()

	#collision with the enemy
	def hit(self):
		self.isJump = False
		self.jumpCount = 10
		if self.hp > 0:
			self.x = 60
			self.y = 620
			self.walkCount = 0
			self.hp = self.hp - 1
			self.life_amount = self.life_amount - 1
			delay = 0
			while delay < 20:
				pygame.time.delay(20)
				delay = delay + 1
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						delay = 21
						pygame.quit()
		else:
			self.visible = False

			"""
			hitFont = pygame.font.SysFont('verdana', 30, True)
			hitText = hitFont.render('Score -1', 1, (255,0,0))
			win.blit(hitText, ((windowWidth/2) - (hitText.get_width()/2), 330)) #screen text position
			pygame.display.update()
			"""
#----------------------------------------------------------------------------------------
#enemy
class enemy(object):
	walkRight = [pygame.image.load('Bat_R1.png'), pygame.image.load('Bat_R2.png'), pygame.image.load('Bat_R3.png'), pygame.image.load('Bat_R4.png'), pygame.image.load('Bat_R5.png')]
	walkLeft = [pygame.image.load('Bat_L1.png'), pygame.image.load('Bat_L2.png'), pygame.image.load('Bat_L3.png'), pygame.image.load('Bat_L4.png'), pygame.image.load('Bat_L5.png')]
	corpse = pygame.image.load('Bat_C.png')

	def __init__(self, x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.walkCount = 0
		self.vel = 5
		self.hitbox = (self.x + 11, self.y + 15, 40, 40)
		#hp + enemy existence
		self.hp = 5 #hp = 5
		self.visible = True

	def draw(self, win):
		self.move()
		if self.visible:
			if self.walkCount + 1 >= 15:
				self.walkCount = 0

			if self.vel > 0:
				win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
				self.walkCount = self.walkCount + 1
			else:
				win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
				self.walkCount = self.walkCount + 1
			#enemy hitbox drawing
			self.hitbox = (self.x + 11, self.y + 15, 40, 40)
			#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
			#hp bar drawing
			pygame.draw.rect(win, (255,0,0), (self.hitbox[0] + 8, self.hitbox[1] - 2, 25, 5))   #hp bar parameters
			pygame.draw.rect(win, (0,255,0), (self.hitbox[0] + 8, self.hitbox[1] - 2, 25 - ((25/5) * (5 - self.hp)), 5)) #hp loss display
		else:
			death == True
			visible = False
			win.blit(self.corpse, (self.x, self.y))

	def move(self):
		if self.visible:
			if self.vel > 0:
				if self.x + self.vel < self.path[1]:
					self.x = self.x + self.vel
				else:
					self.vel = self.vel * -1
					self.walkCount = 0
			else:
				if self.x - self.vel > self.path[0]:
					self.x = self.x + self.vel
				else:
					self.vel = self.vel * -1
					self.walkCount = 0

	def hit(self):
		if self.hp > 0:
			self.hp = self.hp - 1
		else:
			self.visible = False
		print('bat_bullet_hit')

#----------------------------------------------------------------------------------------
#cherry(heal)
class fruit(object):
	cherry = pygame.image.load('Cherry.png')
	life = [pygame.image.load('Life.png'), pygame.image.load('Life.png'), pygame.image.load('Life.png')]
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = (self.x, self.y, 30, 33)
		self.hp = 1
		self.visible = True

	def draw(self, win):
		if self.visible:
			win.blit(self.cherry, (self.x, self.y))
			#cherry hitbox
			self.hitbox = (self.x, self.y, 30, 33)
			#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
		else:
			self.visible == False

	def pick(self):
		if self.hp > 0:
			self.hp = self.hp - 2  #-1 (pygame bug)
		else:
			self.visible = False
			wizzy.hp = wizzy.hp + 1
			wizzy.life_amount = wizzy.life_amount + 1
			global score
			score = score + 1
			if self.visible == False:
				win.blit(self.life[0], (130, 10))
			print('cherry_picked')
#----------------------------------------------------------------------------------------
#bullets
class projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 20 * facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, 1)

#----------------------------------------------------------------------------------------
"""
#platforms
class platform(object):
	file = pygame.image.load('sky_platform.png')
	def __init__(self, x, y, width, heigh):
		self.x = x #100
		self.y = y #500

	def draw(self, win):
		win.blit(self.file, (self.x, self.y))
"""
#----------------------------------------------------------------------------------------
#game window
def redrawGameWindow():
	win.blit(bg, (0,0))	
	text = font.render('Score: ' + str(score), 1, (0,0,0))
	win.blit(text, (1170, 10))
	wizzy.draw(win)
	bat.draw(win)
	cherry.draw(win)
	#platform.draw(win)
	for bullet in bullets:
		bullet.draw(win)

	pygame.display.update()
#----------------------------------------------------------------------------------------
#main game loop
wizzy = player(25, 615, 64, 64)
bat = enemy(600, 617, 64, 64, 1200)
cherry = fruit(400, 645, 32, 32)

#platform
#platform = platform(100, 500, 320/3, 225/3)

#making bullets shot 1x at a time
shootingLoop = 0
bullets = []
#hitting test
font = pygame.font.SysFont('verdana', 20)
run = True
while run:
	clock.tick(24)
	
	#game win
	if score >= 6:
		hitFont = pygame.font.SysFont('verdana', 30, True)
		hitText = hitFont.render('Victory Achieved', 1, (218,165,32))
		win.blit(hitText, ((windowWidth/2) - (hitText.get_width()/2), 330)) #screen text position
		pygame.display.update()
		delay = 0
		while delay < 10:
			pygame.time.delay(10)
			delay = delay + 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					delay = 11
					pygame.quit()
					
	#game quitting
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	#enemy collision
	if bat.visible == True:
		if wizzy.hitbox[1] < bat.hitbox[1] + bat.hitbox[3] and wizzy.hitbox[1] + wizzy.hitbox[3] > bat.hitbox[1]:	
			if wizzy.hitbox[0] + wizzy.hitbox[2] > bat.hitbox[0] and wizzy.hitbox[0] < bat.hitbox[0] + bat.hitbox[2]:
				dmgReceived.play()
				wizzy.hit()
				score = score - 1

	#fruit picking
	if cherry.visible == True:
		if wizzy.hitbox[1] < cherry.hitbox[1] + cherry.hitbox[3] and wizzy.hitbox[1] + wizzy.hitbox[3] > cherry.hitbox[1]:	
			if wizzy.hitbox[0] + wizzy.hitbox[2] > cherry.hitbox[0] and wizzy.hitbox[0] < cherry.hitbox[0] + cherry.hitbox[2]:
				cherry.pick()

	#projectiles		
	for bullet in bullets:
		#checking for projectile collision(top, bottom)
		if bullet.y - bullet.radius < bat.hitbox[1] + bat.hitbox[3] and bullet.y + bullet.radius > bat.hitbox[1]:
			#left, right
			if bullet.x + bullet.radius > bat.hitbox[0] and bullet.x - bullet.radius < bat.hitbox[0] + bat.hitbox[2] and bat.visible == True:
				hitSound.play()
				bat.hit()
				score = score + 1
				bullets.pop(bullets.index(bullet))


		if bullet.x < windowWidth and bullet.x > 0:
			bullet.x = bullet.x + bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()
	#bullet cooldown
	if shootingLoop > 0:
		shootingLoop = shootingLoop + 1
	if shootingLoop > 3:
		shootingLoop = 0
	
	#shooting
	if keys[pygame.K_UP] and shootingLoop == 0:
		bulletSound.play()
		if wizzy.left:
			facing = -1
		else:
			facing = 1

		if len(bullets) < 1:
			bullets.append(projectile(round(wizzy.x + wizzy.width //2), round(wizzy.y + wizzy.height //2), 6, (0, 0, 255), facing))

		shootingLoop = 1

	#left movement
	if keys[pygame.K_LEFT] and wizzy.x > wizzy.vel:
		wizzy.x = wizzy.x - wizzy.vel
		wizzy.left = True
		wizzy.right = False
		wizzy.standing = False
	#right movement
	elif keys[pygame.K_RIGHT] and wizzy.x < windowWidth - wizzy.width - wizzy.vel:
		wizzy.x = wizzy.x + wizzy.vel
		wizzy.right = True
		wizzy.left = False
		wizzy.standing = False
	else:
		wizzy.standing = True
		wizzy.walkCount = 0
	#jumping
	if not(wizzy.isJump):
		if keys[pygame.K_SPACE]:
			wizzy.isJump = True
			wizzy.right = False
			wizzy.left = False
			wizzy.walkCount = 0
	else:
		if wizzy.jumpCount >= -10:
			neg = 1
			if wizzy.jumpCount < 0:
				neg = -1
			wizzy.y = wizzy.y - (wizzy.jumpCount**2) /2 * neg
			wizzy.jumpCount = wizzy.jumpCount - 1
		else:
			wizzy.isJump = False
			wizzy.jumpCount = 10

	redrawGameWindow()

pygame.quit()