import pygame

WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
            self.image = pygame.image.load("assets/images/player_l.png").convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED
            self.image = pygame.image.load("assets/images/player_r.png").convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.image = pygame.image.load("assets/images/player.png").convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)