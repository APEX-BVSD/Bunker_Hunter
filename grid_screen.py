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
from problem_screen import *
from equations import *

def display_grid_screen(screen: pygame.Surface,background_image: pygame.surface, heart_sprite: list[pygame.Surface], frame_counter: int) -> str:
    screen.blit(background_image, (0, 0))
    #hearts
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    screen.blit(heart_sprite[heart_frame],(0,0))
    screen.blit(heart_sprite[heart_frame],(35,0))
    screen.blit(heart_sprite[heart_frame],(67,0))

    # stay on the current screen
    return "PLAYING"

def get_coordinates() -> tuple:
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
        
            coord: tuple = (event.pos[0] // (SCREEN_WIDTH//GRID_ROWS)) + 1,(event.pos[1] // (SCREEN_HEIGHT//GRID_COLUMNS)) + 1
            # get problems for x coordinate and shuffle
            return coord




    

