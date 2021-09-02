import pygame
import random
import time


class Player():  
    def __init__(self):
        self.image = pygame.image.load(r'Fish.io\images\fish.png').convert_alpha()
        self.mass = 32
        self.image = pygame.transform.smoothscale(self.image, (int(self.mass), int(self.mass)))
        self.flipped = False
        self.x = 400
        self.y = 300
        self.speed = 0.25
        self.hitbox = pygame.Rect(self.x, self.y , self.mass, self.mass -5)

    #Key Movement, Boundaries on window and FlipIMG when moving to left
    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_s]: 
            self.y += self.speed 
        elif key[pygame.K_w]: 
            self.y -= self.speed 
        if key[pygame.K_d]: 
            self.x += self.speed 
            self.flipped = False
        elif key[pygame.K_a]:
            self.x -= self.speed
            self.flipped = True
        if self.x <= 0:
            self.x = 0
        elif self.x >=800-self.mass:
            self.x = 800-self.mass
        if self.y <= 0:
            self.y = 0
        elif self.y >= 600 - self.mass:
            self.y = 600 - self.mass
    #Update player on window
    def draw(self, window):
        
        self.imageflip = pygame.transform.flip(self.image, True, False)  
        if self.flipped:
            image = self.imageflip
        else:
            image = self.image
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)
        window.blit(image, (self.x, self.y))

class Fishfood():  
    def __init__(self):  
        
        self.randomfishsize = random.uniform(0.80, 1.35)
        self.flipped = False
        self.speed = 0
        self.x = 0
        self.count = 0
        
        self.recycle()
    def recycle(self):
        #re-start an fishfood position, image, speed and syze after leaving borders or being eaten
        self.count += 1
        self.mass = int(self.randomfishsize*player.mass)
        if self.count%2 == 0:
            self.image = pygame.image.load(r'Fish.io\images\fishfood1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.mass, self.mass))
        elif self.count%3 == 0:
            self.image = pygame.image.load(r'Fish.io\images\fishfood2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.mass, self.mass))
        else:
            self.image = pygame.image.load(r'Fish.io\images\fishfood3.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.mass, self.mass))
        self.imageflip = pygame.transform.flip(self.image, True, False)
        if self.x < 0:
            self.x = 800
        else:
            self.x = -self.mass
        self.y = random.randint(0, 600 - self.mass)
        if self.speed < 0:
            self.speed = random.uniform(-0.10, -0.18)
        else: 
            self.speed = random.uniform(0.10, 0.18)
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)

    def createfood(self):
        #Create fishfood, append to fishfood list and decides if img should be flipped
        global fishfoodlist
        new_food = Fishfood()
        if len(fishfoodlist)%2 == 0:
            new_food.speed = -new_food.speed
            new_food.x = 800
            new_food.flipped = True
        fishfoodlist.append(new_food)
    
    def draw(self, window):
        #draw and move fishfood on window
        if self.flipped:
            image = self.imageflip
        else:
            image = self.image
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)
        window.blit(image, (self.x, self.y))
        
        self.x += self.speed

class Skeleton():  
    def __init__(self):  
        
        self.randomfishsize = random.uniform(0.40, 0.60)
        self.flipped = True
        self.speed = 0
        self.x = 0
        self.recycle()

    def recycle(self):
        #re-start a skeleton position, image, speed and syze after leaving borders or being eaten
        self.mass = int(self.randomfishsize*player.mass)
        self.image = pygame.image.load(r'Fish.io\images\skeleton.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.mass, self.mass))
        self.imageflip = pygame.transform.flip(self.image, True, False)
        if self.x < 0:
            self.x = 800
        else:
            self.x = -self.mass
        self.y = random.randint(0, 600 - self.mass)
        if self.speed < 0:
            self.speed = random.uniform(-0.10, -0.18)
        else: 
            self.speed = random.uniform(0.10, 0.18)
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)

    def createfood(self):
        #Create fishfood, append to fishfood list and decides if img should be flipped
        global skeletonlist
        new_skeleton = Skeleton()
        if len(skeletonlist)%2 == 0:
            new_skeleton.speed = -new_skeleton.speed
            new_skeleton.x = 800
            new_skeleton.flipped = False
        skeletonlist.append(new_skeleton)
    
    def draw(self, window):
        #draw and move fishfood on window
        if self.flipped:
            image = self.imageflip
        else:
            image = self.image
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)
        window.blit(image, (self.x, self.y))
        
        self.x += self.speed

class Shark():  
    def __init__(self):  
        
        self.randomfishsize = random.uniform(1.20,1.40)
        self.flipped = False
        self.recycle()

    def recycle(self):
        #re-start an shark position
        self.mass = int(self.randomfishsize*player.mass)
        self.image = pygame.image.load(r'Fish.io\images\shark.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.mass, self.mass))
        self.imageflip = pygame.transform.flip(self.image, True, False)
        self.side = random.randint(0,1)
        if self.side == 0:
            self.x = -self.mass
            self.speed = 0.4
            self.image = self.imageflip
        else:
            self.x = 800
            self.speed = -0.4
            
        self.y = random.randint(0, 600 - self.mass)
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)

    def draw(self, window):
        #draw and move shark, and shark hitbox on window
        if self.flipped:
            image = self.imageflip
        else:
            image = self.image
        self.hitbox = pygame.Rect(self.x, self.y, self.mass, self.mass)
        window.blit(image, (self.x, self.y))
        self.x += self.speed

pygame.init()

#Texts for Win, GameOver and Mass
font = pygame.font.Font('freesansbold.ttf', 28)
wontext = pygame.font.Font('freesansbold.ttf', 64)
gameover = pygame.font.Font('freesansbold.ttf', 64)

#Functions to Win, GameOver and Mass windows
def GameWonText(x,y):
    gamewon = font.render("You won the game!! You ate the World!", True, (255, 255, 255))
    window.blit(gamewon, (x,y))

def GameOverText(x,y): 
    gameover = font.render("You lost the game!! You got bit by a shark!", True, (255, 255, 255))
    window.blit(gameover, (x,y))

def ShowScore(x,y):
    score = font.render("Mass: " + str(player.mass) + "Kg", True, (255, 255, 255))
    window.blit(score, (x,y))


#Create the screen
window = pygame.display.set_mode((800,600))
background = pygame.image.load(r'Fish.io\images\background.png').convert()
background = pygame.transform.scale(background, (800, 600))


#Title and Icon
pygame.display.set_caption("Fish.io")
icon = pygame.image.load(r'Fish.io\images\fish.png').convert_alpha()
pygame.display.set_icon(icon)

#Player declaration
player = Player()

#Fish declaration
fishfoodlist = []
fishfood = Fishfood()
fishfoodlist.append(fishfood)

#Skeleton declaration
skeletonlist = []
skeleton = Skeleton()
skeletonlist.append(skeleton)

#Shark declaration
shark = Shark()


#Game loop
running = True
start = pygame.time.get_ticks()

while running == True:
    window.fill((0,200,255))
    window.blit(background,(0,0))
    now = pygame.time.get_ticks()
    #When 8000 ms have passed we bring a Shark to Window
    if now - start > 8000:
        start = now
        shark = Shark()    
    #Create 10 fishfood
    if len(fishfoodlist) <=9:
        fishfood.createfood()
    #Create 4 skeletons
    if len(skeletonlist) <=3:
        skeleton.createfood()

    #Handle Player Keys
    player.handle_keys()
    #Show Mass
    ShowScore(10,10)
    
    #Press ESCAPE or click X to stop running the game
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
            running = False
    #Loop for drawing fishfood, verifying if fishfood leaves the border or is eat, in the last case verify if player has enough mass to eat
    for fishfood in fishfoodlist:
        fishfood.draw(window)
        if (fishfood.x < -fishfood.mass - 20) or (fishfood.x > 800 + 20):        
            fishfood.recycle() 
        if player.hitbox.colliderect(fishfood.hitbox):
            if fishfood.mass >= 1.05*player.mass:
                pass
            else:
                fishfood.recycle()
                time.sleep(0.002)
                player.mass += 2
                #Verify win condition (300mass or more)
                if player.mass >= 300:
                    running = "Win"
                #Change player image according to new mass
                player.image = pygame.image.load(r'Fish.io\images\fish.png').convert_alpha()
                player.image = pygame.transform.scale(player.image, (int(player.mass), int(player.mass)))
     #Loop for drawing fishfood, verifying if fishfood leaves the border or is eat and change player Mass
    for skeleton in skeletonlist:
        skeleton.draw(window)
        if (skeleton.x < -skeleton.mass - 20) or (skeleton.x > 800 + 20):        
            skeleton.recycle() 
        if player.hitbox.colliderect(skeleton.hitbox):
            skeleton.recycle()
            time.sleep(0.002)
            if player.mass >= 30:
                player.mass -= 10
            #Change player image according to new mass
            player.image = pygame.image.load(r'Fish.io\images\fish.png').convert_alpha()
            player.image = pygame.transform.scale(player.image, (int(player.mass), int(player.mass)))
    if player.hitbox.colliderect(shark.hitbox):
        running = "Game Over"
    shark.draw(window)    
    player.draw(window)
    pygame.display.update()
while running == "Win":
    window.fill((0,200,255))
    window.blit(background,(0,0))
    ShowScore(10,10)
    GameWonText(150,300)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
            running = False
    pygame.display.update()
while running == "Game Over":
    window.fill((0,200,255))
    window.blit(background,(0,0))
    ShowScore(10,10)
    GameOverText(150,300)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
            running = False
    pygame.display.update()
                
