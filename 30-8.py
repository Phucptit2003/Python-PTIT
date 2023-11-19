import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 3

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooting Game")

# Load player and enemy images
player_img = pygame.image.load("player.png.jpg")
player_rect = player_img.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.centery = SCREEN_HEIGHT - 50

bullet_img = pygame.image.load("player1.jpg")
bullet_rect = bullet_img.get_rect()

enemy_img = pygame.image.load("player2.jpg")
enemy_rect = enemy_img.get_rect()
enemy_rect.centerx = SCREEN_WIDTH // 2
enemy_rect.centery = 50

# Create lists to store bullets and enemies
bullets = []
enemies = []

# Game state
START_SCREEN = 0
PLAYING = 1
GAME_OVER = 2
current_state = START_SCREEN

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if current_state == START_SCREEN:
        if keys[pygame.K_SPACE]:
            current_state = PLAYING
    elif current_state == PLAYING:
        if keys[pygame.K_LEFT]:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            bullet = bullet_rect.copy()
            bullet.centerx = player_rect.centerx
            bullet.centery = player_rect.centery
            bullets.append(bullet)

        # Move bullets
        for bullet in bullets:
            bullet.y -= BULLET_SPEED

        # Remove bullets that are off-screen
        bullets = [bullet for bullet in bullets if bullet.y > 0]

        # Move enemy
        enemy_rect.y += ENEMY_SPEED

        # Check for collisions between bullets and enemy
        for bullet in bullets:
            if bullet.colliderect(enemy_rect):
                enemies.remove(enemy_rect)
                bullets.remove(bullet)

        # Check for collisions between player and enemy
        if player_rect.colliderect(enemy_rect):
            current_state = GAME_OVER

        # Draw everything
        screen.fill(WHITE)
        screen.blit(player_img, player_rect)
        screen.blit(enemy_img, enemy_rect)
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
    
    elif current_state == GAME_OVER:
        game_over_text = font.render("Game Over. Press Space to Restart", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50))

        if keys[pygame.K_SPACE]:
            current_state = START_SCREEN
            player_rect.centerx = SCREEN_WIDTH // 2
            player_rect.centery = SCREEN_HEIGHT - 50
            bullets = []
            enemies = []

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
