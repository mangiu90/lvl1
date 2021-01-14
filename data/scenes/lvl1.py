import pygame

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

        self.player = Player(600, 500)
    
    def ProcessInput(self, events, pressed_keys):
        self.player.update(pressed_keys)
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.background_image, [0, 0])
        screen.blit(self.player.surf, self.player.rect)