#!/usr/bin/env python3

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame WASD Movement")

# Set up the player object
player_size = 50
player_x, player_y = width // 2 - player_size // 2, height // 2 - player_size // 2
player_speed = 5

# Set up colors
white = (255, 255, 255)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move the player based on WASD inputs
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < height - player_size:
        player_y += player_speed
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < width - player_size:
        player_x += player_speed

    # Draw the player
    pygame.draw.rect(
        screen, (0, 128, 255), (player_x, player_y, player_size, player_size)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
