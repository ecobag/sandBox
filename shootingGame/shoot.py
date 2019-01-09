import pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640

rockImage=['src/rock01.png', 'src/rock02.png', 'src/rock03.png', 'src/rock04.png', 'src/rock05.png', \
           'src/rock06.png', 'src/rock07.png', 'src/rock08.png', 'src/rock09.png', 'src/rock10.png', \
           'src/rock11.png', 'src/rock12.png', 'src/rock13.png', 'src/rock14.png', 'src/rock15.png', \
           'src/rock16.png', 'src/rock17.png', 'src/rock18.png', 'src/rock19.png', 'src/rock20.png', \
           'src/rock21.png', 'src/rock22.png', 'src/rock23.png', 'src/rock24.png', 'src/rock25.png', \
           'src/rock26.png', 'src/rock27.png', 'src/rock28.png', 'src/rock29.png', 'src/rock30.png']


# draw image
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

# initialize variables 
def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Pyshooting')
    background = pygame.image.load('src/background.png')
    fighter = pygame.image.load('src/fighter.png')
    missile = pygame.image.load('src/missile.png')
    explosion = pygame.image.load('src/explosion.png')
    clock = pygame.time.Clock()


# Game logic
def runGame():
    global gamePad, clock, background, fighter, missile, explosion
    
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0
    rockPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5
                elif event.key == pygame.K_RIGHT:
                    fighterX += 5
                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth / 2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
                    

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
        
        drawObject(background, 0, 0)

        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
            
        drawObject(fighter,x, y)
        
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY += rockSpeed

        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
        
        if isShot:
            drawObject(explosion, rockX, rockY)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            isShot = False

        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


initGame()
runGame()