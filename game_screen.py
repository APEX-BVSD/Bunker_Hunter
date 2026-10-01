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

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()
    BG_color: tuple = (100,255,100)
    Top_border: pygame.Rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.fill(BG_color)

        # render the screen
    pygame.display.flip()
        # advance the clock
    clock.tick(FPS)
    pygame.event.pump()

    # stay on the current screen
    return "PLAYING"


