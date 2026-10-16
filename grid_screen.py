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

def display_grid_screen(screen: pygame.Surface,background_image: pygame.surface, heart_sprite: list[pygame.Surface], frame_counter: int,lives:list[bool], bunkers: list[list[bool]], bunker_states: list[list[bool]], dead_bunker_sprite: pygame.Surface) -> str:
    screen.blit(background_image, (0, 0))
    #hearts
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    screen.blit(heart_sprite[heart_frame],(0,0))
    screen.blit(heart_sprite[heart_frame],(35,0))
    screen.blit(heart_sprite[heart_frame],(67,0))

    for row in range(len(bunker_states)):
        for col in range(len(bunker_states[row])):
            if bunker_states[row][col]:
                screen.blit(dead_bunker_sprite,(COLUMN_SIZE * col, ROW_SIZE * row))
                
    # stay on the current screen
    return "PLAYING"

def get_coordinates() -> tuple:
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if mouse_x <= GRID_WIDTH and mouse_y <= GRID_HEIGHT:
                coord: tuple = (mouse_x // (SCREEN_WIDTH//GRID_ROWS)) + 1,(mouse_y // (SCREEN_HEIGHT//GRID_COLUMNS)) + 1
                # get problems for x coordinate and shuffle
                return coord
    #screen.blit(insert_sprite_here)

    

