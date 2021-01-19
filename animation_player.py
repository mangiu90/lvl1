import pygame
from pygame.locals import *

SCREEN_SIZE = (600,600)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.vel = 5
        self.isRun = False
        self.isJump = False
        self.isShoot = False
        self.isMelee = False
        self.left = False
        self.jumpCount = 10

        self.pos = (x, y)

        self.jump_sound = pygame.mixer.Sound("data/resources/sound/mixkit-quick-jump-arcade-game-239.wav")

        self.count = 0

        self.idle_img = []
        self.jump_img = []
        self.run_img = []
        self.melee_img = []
        self.dead_img = []
        self.jump_melee_img = []
        self.jump_shoot_img = []
        self.run_shoot_img = []
        self.shoot_img = []
        self.slide_img = []
        for x in range(10):
            self.idle_img.append(pygame.image.load(f"data/resources/img/player/Idle ({x+1}).png"))
            self.jump_img.append(pygame.image.load(f"data/resources/img/player/Jump ({x+1}).png"))
            self.dead_img.append(pygame.image.load(f"data/resources/img/player/Dead ({x+1}).png"))
            self.slide_img.append(pygame.image.load(f"data/resources/img/player/Slide ({x+1}).png"))
        for x in range(8):
            self.run_img.append(pygame.image.load(f"data/resources/img/player/Run ({x+1}).png"))
            self.melee_img.append(pygame.image.load(f"data/resources/img/player/Melee ({x+1}).png"))
            self.jump_melee_img.append(pygame.image.load(f"data/resources/img/player/JumpMelee ({x+1}).png"))
            self.run_shoot_img.append(pygame.image.load(f"data/resources/img/player/RunShoot ({x+1}).png"))
        for x in range(5):
            self.jump_shoot_img.append(pygame.image.load(f"data/resources/img/player/JumpShoot ({x+1}).png"))
        for x in range(4):
            self.shoot_img.append(pygame.image.load(f"data/resources/img/player/Shoot ({x+1}).png"))

        self.surf = self.idle_img[0].convert_alpha()
        # self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=self.pos)

    def update(self, pressed_keys):
        if not(self.isRun):
            self.animation(self.idle_img)
        
    def animation(self, img_list):
        if self.count >= len(img_list)*5:
            self.count = 0
        self.surf = img_list[self.count//5].convert_alpha()
        # self.surf = pygame.transform.scale(self.surf, (100, 100)).
        self.count += 1
        if self.left:
            self.surf = pygame.transform.flip(self.surf, True, False)
        


def main():
    pygame.init()
    pygame.display.set_caption('Player')
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    while True:
                        event = pygame.event.wait()
                        if event.type == KEYDOWN and event.key == K_SPACE:
                            break 
            elif event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()

        # drawGrid(screen)

        player.update(pressed_keys)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        

        pygame.display.flip()

        dt = clock.tick(60)

def drawGrid(screen):
    blockSize = 50 #Set the size of the grid block
    for x in range(SCREEN_SIZE[0]):
        for y in range(SCREEN_SIZE[1]):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(screen, (255,255,255), rect, 1)

if __name__ == '__main__':
    main()