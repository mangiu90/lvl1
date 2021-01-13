import pygame

from pygame.locals import *
from data.scenes.SceneBase import *
from data.scenes.EndScene import *

class StartScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
                self.SwitchToScene(EndScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        bg_start = pygame.image.load("data/resources/img/start.png").convert()
        bg_start.set_colorkey((255, 255, 255), RLEACCEL)
        screen.blit(bg_start, [150, 250])