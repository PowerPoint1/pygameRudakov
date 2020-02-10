import pygame
import random
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder)
player_img = pygame.image.load(os.path.join('img', 'delor.png'))

pygame.mixer.init(44100, -16,2,2048)
pygame.mixer.music.load('call.mp3')
pygame.mixer.music.play()


WIDTH = 750
HEIGHT = 442
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1.3)
            
            
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
background_image = pygame.image.load(os.path.join('img', "retrowave.jpg"))
back_rect = background_image.get_rect(bottomright=(750, 430))
screen.blit(background_image, back_rect)
player_img = pygame.Surface([640,480], pygame.SRCALPHA, 32)
player_img = player_img.convert_alpha()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    

pygame.quit()