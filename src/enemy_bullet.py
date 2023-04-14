import pygame

WIDTH, HEIGHT = 800, 600
BULLET_SPEED = 5

# Add EnemyBullet class
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/images/enemy_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 30))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.rect.y += BULLET_SPEED

        if self.rect.top > HEIGHT or self.rect.bottom < 0 or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()