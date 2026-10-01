"""
Contains functions that implement the start screen.
Month Year
First Last
First Last 
First Last 
"""


from start_screen import *
import pygame
from pygame import font
from settings import *

def display_game_screen(screen: pygame.Surface) -> str:
    screen.fill("Green")
    image: pygame.Surface = pygame.image.load("assets/grid_image.jpg")
    screen.blit(image, (0, 0))

    # stay on the current screen
    return "PLAYING"


