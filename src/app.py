import pygame
import sys
import random

from player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score
from enemy_bullet import EnemyBullet

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Add enemy bullet firing logic in the game loop
ENEMY_FIRE_RATE = 500  # In milliseconds
last_enemy_fire = pygame.time.get_ticks()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Battle")
clock = pygame.time.Clock()

# Instantiate the Score class
scoreboard = Score()

player = Player()
all_sprites = pygame.sprite.Group(player)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


# Add a reset_game function
def reset_game():
    global player, all_sprites, enemies, bullets, scoreboard

    scoreboard.reset()

    player = Player()
    all_sprites = pygame.sprite.Group(player)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    for _ in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

# Add game over screen
def game_over_screen(screen, scoreboard):
    font = pygame.font.Font(None, 60)
    font_small = pygame.font.Font(None, 20)
    text = font.render("Game Over", True, (200, 0, 0))
    text_small = font_small.render("Press Enter to restart the game", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    small_rect = text.get_rect(center=(WIDTH // 2 + 15, HEIGHT // 2))

    while True:
        screen.fill(BLACK)
        screen.blit(text, text_rect)
        screen.blit(text_small, small_rect)
        scoreboard.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                reset_game()
                main()

# Add a collide_mask function
def collide_mask(sprite1, sprite2):
    return pygame.sprite.collide_mask(sprite1, sprite2) is not None

# Create a main function for the game loop
def main():
    global player, all_sprites, enemies, bullets, scoreboard, last_enemy_fire

    running = True
    while running:
        clock.tick(FPS)
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

        all_sprites.update()

        # Check for collisions
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True, collide_mask)
        for hit in hits:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)
            scoreboard.update(10)  # Add 10 points for each enemy killed

        # Enemy bullet firing logic
        if now - last_enemy_fire > ENEMY_FIRE_RATE:
            last_enemy_fire = now
            firing_enemy = random.choice(enemies.sprites())
            enemy_bullet = EnemyBullet(firing_enemy.rect.centerx, firing_enemy.rect.centery)
            all_sprites.add(enemy_bullet)

        # Check for player death
        player_death = pygame.sprite.spritecollide(player, enemies, False, collide_mask)
        player_hit_by_enemy_bullet = pygame.sprite.spritecollide(player, [b for b in all_sprites if isinstance(b, EnemyBullet)], False, collide_mask)
        if player_death or player_hit_by_enemy_bullet:
            game_over_screen(screen, scoreboard)
            break

        screen.fill(BLACK)
        all_sprites.draw(screen)
        scoreboard.draw(screen)  # Draw the scoreboard
        pygame.display.flip()


if __name__ == "__main__":
    main()