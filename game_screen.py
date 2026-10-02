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
    original_image: pygame.Surface = pygame.image.load("assets/grid_image.jpg")
    bigger_image: pygame.Surface = pygame.transform.scale(original_image, (800,800))
    screen.blit(bigger_image, (0, 0))
    
    # stay on the current screen
    return "PLAYING"

def mouse_grid_interactions() -> None:
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            print(f"{mouse_x} {mouse_y}")
            print(event.pos)
        
            coord: tuple = (event.pos[0] // 80) + 1,(event.pos[1] // 80) + 1
            print(coord)

    

