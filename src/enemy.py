import pygame
import random

WIDTH, HEIGHT = 800, 600
ENEMY_SPEED = 2

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-HEIGHT, -self.rect.height)

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-HEIGHT, -self.rect.height)
            self.rect.x = random.randint(0, WIDTH - self.rect.width)