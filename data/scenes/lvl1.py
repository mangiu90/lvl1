import pygame
import random

from pygame.locals import *
from data.scenes.SceneBase import *
from data.scenes.EndScene import *
from data.sprites.Sprites import *

class Level1Scene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.background_image = pygame.image.load("data/resources/img/game_background_2.png").convert()
        self.background_image.set_colorkey((255, 255, 255), RLEACCEL)
        pygame.mixer.music.load("data/resources/sound/LOWER-VERSION-2020-08-10_-_Go_Beyond_-_David_Fesliyan.mp3")
        pygame.mixer.music.play(loops=-1)
        self.coin_sound = pygame.mixer.Sound("data/resources/sound/mixkit-unlock-new-item-game-notification-254.wav")

        self.player = Player(600, 500)
        self.coin = Player(600, 500)

        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 1000)
        self.coins = pygame.sprite.Group()

        self.bullet = 0
        self.yellow = (255, 255, 0)
        self.myfont = pygame.font.SysFont("Comic Sans MS", 50, True)

    def ProcessInput(self, events, pressed_keys):
        self.player.update(pressed_keys)
        for event in events:
            if event.type == self.ADDENEMY and len(self.coins.sprites()) < 10:
                coin = Coin()
                self.coins.add(coin)
    
    def Update(self, dt):
        self.label = self.myfont.render(str(self.bullet), 1, self.yellow)
    
    def Render(self, screen, dt):
        screen.fill((0, 0, 0))
        screen.blit(self.background_image, [0, 0])
        screen.blit(self.player.surf, self.player.rect)
        screen.blit(self.label, (1050, 650))
        collide = pygame.sprite.spritecollide(self.player, self.coins, True)
        for coin in collide:
            self.coin_sound.play()
            self.bullet += 1
        for coin in self.coins:
            coin.update(dt)
            screen.blit(coin.surf, coin.rect)