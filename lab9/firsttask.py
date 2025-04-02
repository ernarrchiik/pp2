import pygame 
import sys
import random 
import time
from pygame.locals import *
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font.render("Game Over",True,BLACK)

background = pygame.image.load("/Users/ernarberenbaj/python/lab8/AnimatedStreet.png")

screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")
#add random weights like [1,3,5]
COIN_TYPES = [
    {"image":"/Users/ernarberenbaj/python/lab8/coin-svgrepo-com.png", "weight":1},
    {"image":"/Users/ernarberenbaj/python/lab8/coin-svgrepo-com.png", "weight":3},
    {"image":"/Users/ernarberenbaj/python/lab8/coin-svgrepo-com.png", "weight":5}
]

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ernarberenbaj/python/lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH - 40),0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH - 40),0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ernarberenbaj/python/lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
    def collect_coins(self,coins):
        global COIN_SCORE
        collisions = pygame.sprite.spritecollide(self,coins,True)
        for coin in collisions:
            COIN_SCORE += coin.weight
        return bool(collisions)
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin_type = random.choice(COIN_TYPES)
        self.image = pygame.image.load(coin_type["image"])
        self.weight = coin_type["weight"]
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH - 40),0)
    def move(self):
        self.rect.move_ip(0,SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH - 40),0)
P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED,1000)
N = 10 #Change this to set how often speed increases
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            SPEED += 0.5
    #Increase speed when COIN_SCORE reaches multiples of N
    if COIN_SCORE > 0 and COIN_SCORE % N == 0:
        SPEED += 0.2
        COIN_SCORE += 1
    screen.blit(background,(0,0))
    scores = font_small.render(str(SCORE),True,BLACK)
    coin_scores = font_small.render(str(COIN_SCORE),True,BLACK)
    screen.blit(scores,(10,20))
    screen.blit(coin_scores,(375,10))
    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    if P1.collect_coins(coins):
        new_coin = Coins()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound('/Users/ernarberenbaj/python/lab8/lab8_crash.wav').play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over,(30,50))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)



        
