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

        self.idle_img = [pygame.image.load("data/resources/img/player/Idle (1).png"), pygame.image.load("data/resources/img/player/Idle (2).png"), pygame.image.load("data/resources/img/player/Idle (3).png"), pygame.image.load("data/resources/img/player/Idle (4).png"), pygame.image.load("data/resources/img/player/Idle (5).png"), pygame.image.load("data/resources/img/player/Idle (6).png"), pygame.image.load("data/resources/img/player/Idle (7).png"), pygame.image.load("data/resources/img/player/Idle (8).png"), pygame.image.load("data/resources/img/player/Idle (9).png"), pygame.image.load("data/resources/img/player/Idle (10).png")]
        self.run_img = [pygame.image.load("data/resources/img/player/Run (1).png"), pygame.image.load("data/resources/img/player/Run (2).png"), pygame.image.load("data/resources/img/player/Run (3).png"), pygame.image.load("data/resources/img/player/Run (4).png"), pygame.image.load("data/resources/img/player/Run (5).png"), pygame.image.load("data/resources/img/player/Run (6).png"), pygame.image.load("data/resources/img/player/Run (7).png"), pygame.image.load("data/resources/img/player/Run (8).png")]

        self.surf = self.idle_img[0].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)

    def update(self, pressed_keys):
        if self.idleCount == 10:
            self.idleCount = 0
        self.surf = self.idle_img[self.idleCount].convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        if self.left:
            self.surf = pygame.transform.flip(self.surf, True, False)
        self.idleCount += 1

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.vel)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.vel)
        if pressed_keys[K_LEFT]:
            self.right = False
            self.left = True
            if self.walkCount == 8:
                self.walkCount = 0
            self.surf = self.run_img[self.walkCount].convert_alpha()
            self.surf = pygame.transform.scale(self.surf, (100, 100))
            self.surf = pygame.transform.flip(self.surf, True, False)
            self.walkCount += 1
            self.rect.move_ip(-self.vel, 0)
        if pressed_keys[K_RIGHT]:
            self.left = False
            self.right = True
            if self.walkCount == 8:
                self.walkCount = 0
            self.surf = self.run_img[self.walkCount].convert_alpha()
            self.surf = pygame.transform.scale(self.surf, (100, 100))
            self.walkCount += 1
            self.rect.move_ip(self.vel, 0)
                
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 200:
            self.rect.top = 200
        if self.rect.bottom >= 600:
            self.rect.bottom = 600