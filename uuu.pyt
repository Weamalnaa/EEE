python
import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height=600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Duck and Pole Game")

# Set up the colors
yellow = (255, 255, 0)
green = (0, 255, 0)

# Set up the duck
duck_width = 50
duck_height = 50
duck_x = window_width // 2 - duck_width // 2
duck_y = window_height - duck_height
duck_speed = 5

# Set up the pole
pole_width = 100
pole_height = random.randint(100, 400)
pole_x = window_width
pole_y = window_height - pole_height
pole_speed = 3

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the duck
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and duck_y > 0:
        duck_y -= duck_speed
    if keys[pygame.K_DOWN] and duck_y < window_height - duck_height:
        duck_y += duck_speed

    # Move the pole
    pole_x -= pole_speed
    if pole_x + pole_width < 0:
        pole_x = window_width
        pole_height = random.randint(100, 400)
        pole_y = window_height - pole_height

    # Check for collision
    if duck_x + duck_width > pole_x and duck_x < pole_x + pole_width:
        if duck_y < pole_y + pole_height:
            running = False

    # Draw the game objects
    window.fill((0, 0, 0))
    pygame.draw.rect(window, yellow, (duck_x, duck_y, duck_width, duck_height))
    pygame.draw.rect(window, green, (pole_x, pole_y, pole_width, pole_height))
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)