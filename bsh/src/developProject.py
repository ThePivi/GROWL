import pygame
import random
import time
import os


#   Ablak init
WIDTH = 1366
HEIGHT = 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#   Ablak neve
pygame.display.set_caption("Ablak neve")

DIVIDER = 40
MULTIPLER = 0.5
ONE_UNIT = int(WIDTH/(WIDTH/DIVIDER)*MULTIPLER)

#load image
VARR = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "pictures", "ui", "heart.png")), (ONE_UNIT, ONE_UNIT))
VAR = pygame.image.load(os.path.join("..", "assets", "pictures", "ui", "grassland_bg.png"))
#kép nyújtása
#pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "pictures", "ui", "grassland_bg.PNG")), (HEIGHT,WIDTH)), 90)



pygame.font.init()

class MainCharacter ():

    def __init__ (self):
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.angle = 0
        self.speed = 1
        self.mainCharacterGraphics = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "pictures", "ui", "heart.png")), (ONE_UNIT, ONE_UNIT))
        # Gravity érintett variables
        self.mass = 0.1
        self.velocity = 0
        self.gravityX = 0
        self.gravityY = 0
        self.gravityZ = 0

    def update (self):
        # Gravity Calculation method call
        self.setGravity (0, 0, 1)
        self.calculateGravity()
        self.mainCharacterGraphics = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "pictures", "ui", "heart.png")), (ONE_UNIT, ONE_UNIT)), self.angle)

    def draw (self, window):
        self.update()
        # TODO ide kell egy gravity hívás, ami 3 paraméter (x,y,z) segítségével eldőnti a gravitáció irányát
        window.blit(self.mainCharacterGraphics, (self.posX, self.posY))

    def calculateGravity (self):
        # Collision Check method call
        if self.collision ():
            self.velocity = 0
        else:
            self.velocity += 0.1
        self.posX += self.gravityX * self.mass * self.velocity
        self.posY += self.gravityY * self.mass * self.velocity
        #self.posZ += self.gravityZ * self.mass * self.velocity

    def collision (self):
        return False

    def setGravity(self, gravityX, gravityY, gravityZ):
        self.gravityX = gravityX
        self.gravityY = gravityY
        #self.gravityZ = gravityZ

    def direction (self, angle):
        self.angle = angle
        #Következő megoldandó problem:
        if self.notCollide():
            self.moove (angle)

    def notCollide (self):
        #if self.angle:
        return True

    def moove (self, angle):
# Normál 4 irány
        if angle == 180:
            self.velocity -= 1 * self.speed
        if angle == 90:
            self.posX -= 1 * self.speed
        if angle == 0:
            self.posY += 1 * self.speed
        if angle == -90:
            self.posX += 1 * self.speed
# Átlós 4 irány
        if angle == 225:
            self.posY -= 1 * self.speed/1.75
            self.posX -= 1 * self.speed/1.75
        if angle == 135:
            self.posY -= 1 * self.speed/1.75
            self.posX += 1 * self.speed/1.75
        if angle == 45:
            self.posY += 1 * self.speed/1.75
            self.posX += 1 * self.speed/1.75
        if angle == -45:
            self.posY += 1 * self.speed/1.75
            self.posX -= 1 * self.speed/1.75




#   Szükséges egy olyan grafikai megjelenítő engine aminek van egy methodja, amibe be lehet dobálni a megjelenítendő képeket, szövegeket.
def main ():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    #Betűkhöz
    #font_neve = pygame.font.SysFont("font neve", mérete)

    mainCharacter = MainCharacter()

    def redraw_window ():
        WIN.blit(VAR, (-10, -10))
        #   kép
        mainCharacter.draw (WIN)
        #   font

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pushedKeys = pygame.key.get_pressed()
        if pushedKeys[pygame.K_UP]:
            if pushedKeys[pygame.K_LEFT]:
                mainCharacter.direction (225)
            elif pushedKeys[pygame.K_RIGHT]:
                mainCharacter.direction (135)
            else:
                mainCharacter.direction (180)
            # TODO Ki kell kísérletezni azt, hogy hogyan lehet az object-hez implementálni a viselkedését.
        elif pushedKeys[pygame.K_DOWN]:
            if pushedKeys[pygame.K_LEFT]:
                mainCharacter.direction (-45)
            elif pushedKeys[pygame.K_RIGHT]:
                mainCharacter.direction (45)
            else:
                mainCharacter.direction (0)
        elif pushedKeys[pygame.K_LEFT]:
            mainCharacter.angle = -90
            mainCharacter.posX -= 1
        elif pushedKeys[pygame.K_RIGHT]:
            mainCharacter.angle = 90
            mainCharacter.posX += 1
        if pushedKeys[pygame.K_ESCAPE]:
            run = False

main()
