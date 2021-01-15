import pygame
import random

from pygame.locals import *
from data.config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.idleCount = 0
        self.jumpCount = 10
        self.jumpCountAni = 0
        self.melee = False
        self.meleeCount = 0

        self.jump_sound = pygame.mixer.Sound("data/resources/sound/mixkit-quick-jump-arcade-game-239.wav")

        self.idle_img = [pygame.image.load("data/resources/img/player/Idle (1).png"), pygame.image.load("data/resources/img/player/Idle (2).png"), pygame.image.load("data/resources/img/player/Idle (3).png"), pygame.image.load("data/resources/img/player/Idle (4).png"), pygame.image.load("data/resources/img/player/Idle (5).png"), pygame.image.load("data/resources/img/player/Idle (6).png"), pygame.image.load("data/resources/img/player/Idle (7).png"), pygame.image.load("data/resources/img/player/Idle (8).png"), pygame.image.load("data/resources/img/player/Idle (9).png"), pygame.image.load("data/resources/img/player/Idle (10).png")]
        self.jump_img = [pygame.image.load("data/resources/img/player/Jump (1).png"), pygame.image.load("data/resources/img/player/Jump (2).png"), pygame.image.load("data/resources/img/player/Jump (3).png"), pygame.image.load("data/resources/img/player/Jump (4).png"), pygame.image.load("data/resources/img/player/Jump (5).png"), pygame.image.load("data/resources/img/player/Jump (6).png"), pygame.image.load("data/resources/img/player/Jump (7).png"), pygame.image.load("data/resources/img/player/Jump (8).png"), pygame.image.load("data/resources/img/player/Jump (9).png"), pygame.image.load("data/resources/img/player/Jump (10).png")]
        self.run_img = [pygame.image.load("data/resources/img/player/Run (1).png"), pygame.image.load("data/resources/img/player/Run (2).png"), pygame.image.load("data/resources/img/player/Run (3).png"), pygame.image.load("data/resources/img/player/Run (4).png"), pygame.image.load("data/resources/img/player/Run (5).png"), pygame.image.load("data/resources/img/player/Run (6).png"), pygame.image.load("data/resources/img/player/Run (7).png"), pygame.image.load("data/resources/img/player/Run (8).png")]
        self.melee_img = [pygame.image.load("data/resources/img/player/Melee (1).png"), pygame.image.load("data/resources/img/player/Melee (2).png"), pygame.image.load("data/resources/img/player/Melee (3).png"), pygame.image.load("data/resources/img/player/Melee (4).png"), pygame.image.load("data/resources/img/player/Melee (5).png"), pygame.image.load("data/resources/img/player/Melee (6).png"), pygame.image.load("data/resources/img/player/Melee (7).png"), pygame.image.load("data/resources/img/player/Melee (8).png")]

        self.surf = self.idle_img[0].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)

    def update(self, pressed_keys):
        self.animacionIdle(self.idle_img)

        if not(self.isJump):
            if pressed_keys[K_UP]:
                self.animacionWalk(self.run_img)
                self.rect.move_ip(0, -self.vel)
            if pressed_keys[K_DOWN]:
                self.animacionWalk(self.run_img)
                self.rect.move_ip(0, self.vel)
            if pressed_keys[K_LEFT]:
                self.right = False
                self.left = True
                self.animacionWalk(self.run_img)
                self.rect.move_ip(-self.vel, 0)
            if pressed_keys[K_RIGHT]:
                self.left = False
                self.right = True
                self.animacionWalk(self.run_img)
                self.rect.move_ip(self.vel, 0)
            if pressed_keys[K_SPACE]:
                self.jump_sound.play()
                self.isJump = True
            if pressed_keys[K_LCTRL]:
                self.animavionMelee(self.melee_img)
        else:
            self.animacionJump(self.jump_img)
            if pressed_keys[K_LEFT]:
                self.right = False
                self.left = True
                self.rect.move_ip(-self.vel, 0)
            if pressed_keys[K_RIGHT]:
                self.left = False
                self.right = True
                self.rect.move_ip(self.vel, 0)
            if self.jumpCount >= -10:
                self.rect.move_ip(0, (self.jumpCount * abs(self.jumpCount)) * -0.5)
                self.jumpCount -= 1
                self.jumpCountAni += 1
            else: 
                self.jumpCount = 10
                self.isJump = False


                
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 200 and not(self.isJump):
            self.rect.top = 200
        if self.rect.bottom >= 635:
            self.rect.bottom = 635

    def animacionIdle(self, img_list):
        if self.idleCount >= len(img_list):
            self.idleCount = 0
        self.surf = img_list[int(self.idleCount)].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        if self.left:
            self.surf = pygame.transform.flip(self.surf, True, False)
        self.idleCount += 0.1

    def animacionWalk(self, img_list):
        if self.walkCount >= len(img_list):
            self.walkCount = 0
        self.surf = img_list[int(self.walkCount)].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        if self.left:
            self.surf = pygame.transform.flip(self.surf, True, False)
        self.walkCount += 0.1

    def animacionJump(self, img_list):
        if self.jumpCountAni > 19:
            self.jumpCountAni = 0
        self.surf = img_list[self.jumpCountAni//2].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        if self.left:
            self.surf = pygame.transform.flip(self.surf, True, False) 

    def  animavionMelee(self, img_list):
        if self.meleeCount > 21:
            self.meleeCount = 0
        self.surf = img_list[self.meleeCount//3].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        if self.left:
            self.surf = pygame.transform.flip(self.surf, True, False) 
        self.meleeCount += 1

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        
        self.x = random.randint(100, 1000)
        self.y = random.randint(100, 600)
        self.coin_img = []
        self.coinCount = 0
        self.coin_img = [pygame.image.load("data/resources/img/coins/Gold_1.png"), pygame.image.load("data/resources/img/coins/Gold_2.png"), pygame.image.load("data/resources/img/coins/Gold_3.png"), pygame.image.load("data/resources/img/coins/Gold_4.png"), pygame.image.load("data/resources/img/coins/Gold_5.png"), pygame.image.load("data/resources/img/coins/Gold_6.png"), pygame.image.load("data/resources/img/coins/Gold_7.png"), pygame.image.load("data/resources/img/coins/Gold_8.png"), pygame.image.load("data/resources/img/coins/Gold_9.png"), pygame.image.load("data/resources/img/coins/Gold_10.png")]
        self.surf = self.coin_img[0].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, [self.surf.get_size()[0]//10, self.surf.get_size()[1]//10])
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, dt):
        if self.coinCount >= 30:
            self.coinCount = 0
        self.surf = self.coin_img[self.coinCount//3].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, [self.surf.get_size()[0]//10, self.surf.get_size()[1]//10])
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        self.coinCount += 1
        
