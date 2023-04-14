import pygame

WIDTH = 800
WHITE = (255, 255, 255)

class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.high_score = 0
        self.load_high_score()

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (WIDTH - 200, 10))

    def update(self, value):
        self.score += value

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
