import pygame
import random

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(x=random.randint(0, screen_width - 30),
                                         y=random.randint(0, screen_height - 30))


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemies = pygame.sprite.Group(Enemy() for _ in range(7))
all_sprites.add(enemies)

score = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    collisions = pygame.sprite.spritecollide(player, enemies, True)
    score += len(collisions)

    keys = pygame.key.get_pressed()
    player.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    player.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score:", score, True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
