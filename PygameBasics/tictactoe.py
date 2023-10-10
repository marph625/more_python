import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Courier New", 40)

window_size = (450, 500)
cell_size = 150

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")
