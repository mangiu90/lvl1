import pygame

from pygame.locals import *
from data.scenes.SceneBase import *

class EndScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        bg_end = pygame.image.load("data/resources/img/game_over.png").convert()
        bg_end.set_colorkey((255, 255, 255), RLEACCEL)
        screen.blit(bg_end, [100, 0])