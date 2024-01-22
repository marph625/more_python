# Imports
import pygame
import sys
import time
import random
from pygame.locals import *

# Some Variables
MULTIPLIER = 20

# Colors
ORANGE = (255, 140, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Use MULTIPLIER to set window size
window = pygame.display.set_mode((MULTIPLIER * 20, MULTIPLIER * 30))


# Title for header
pygame.display.set_caption("Breakout's 1984th copy of a copy")
game_active = True

# Set screen refresh rate
clock = pygame.time.Clock()


def draw_element(column, row):
    pygame.draw.rect(window, ORANGE, (column * MULTIPLIER, row * MULTIPLIER, MULTIPLIER, MULTIPLIER))


# Main loop
while game_active:
    # Check if user made an input
    for event in pygame.event.get():
        if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_active = False
            print("Program was shut down successfully.")

        # Test Output for draw_element in window
        draw_element(0, 0)
        draw_element(1, 1)
        draw_element(2, 2)

        # Refresh display
        pygame.display.update()

        # Refresh-Rate
        clock.tick(10)

pygame.quit()