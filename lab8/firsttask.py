import sys
import pygame as pg
from pygame.locals import *
import random

pg.init()

FPS = 60
clock = pg.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPPED = 5
SCORE = 0
font = pg.font.SysFont("Verdana",60)
font_small = pg.font.SysFont("Verdana",20)
game_over = font.render("Game Over", True, BLACK)
background = pg.image.load("AnimatedStreet.png")

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("GAME")

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("/Users/ernarberenbaj/python/lab8/image copy 2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPPED)
        if (self.rect.bottom > 600):
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("/Users/ernarberenbaj/python/lab8/images-1.jpeg")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

enemies = pg.sprite.Group()
enemies.add(E1)
all_sprites = pg.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pg.event.get():
        if event.type == INC_SPEED:
              SPPED += 0.5
           
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    screen.blit(background,(0,0))
    scores = font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))

 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(P1, enemies):
          pg.mixer.Sound('crash.wav').play()
          pg.time.sleep(0.5)
          screen.fill(RED)
          screen.blit(game_over,(30,250))
          pg.display.update()
          for entity in all_sprites:
                entity.kill() 
          pg.time.sleep(2)
          pg.quit()
          sys.exit()        
         
    pg.display.update()
    clock.tick(FPS)
    
