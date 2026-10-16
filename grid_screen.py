"""
Contains functions that implement the grid screen.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""


from start_screen import *
import pygame
from pygame import font
from settings import *
from problem_screen import *
from equations import *

def display_grid_screen(screen: pygame.Surface,background_image: pygame.surface, heart_sprite: list[pygame.Surface], frame_counter: int,lives:list[bool], bunkers: list[list[bool]], bunker_states: list[list[bool]], dead_bunker_sprite: pygame.Surface) -> str:
    """
    Displays the game grid screen with hearts showing remaining lives.
    
    Parameters:
        screen: The screen to render the game on
        background_image: The background image for the grid
        heart_sprite: List of heart animation frames
        heart_gone: List of empty heart sprites
        frame_counter: Current frame count for animation
        lives: List of booleans representing remaining lives
    
    Returns:
        The game state for the next frame
    """
    screen.blit(background_image, (0, 0))

    # Display hearts based on remaining lives
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    bunkers="30"

    if lives[2] == True:
        screen.blit(heart_sprite[heart_frame], HEART1POS)
    else:
        screen.blit(heart_gone[-1], HEART1POS)
        return "GAME_OVER"
    if lives[1] == True:
        screen.blit(heart_sprite[heart_frame], HEART2POS)
    else:
        screen.blit(heart_gone[-1], HEART2POS)
    if lives[0] == True:
        screen.blit(heart_sprite[heart_frame], HEART3POS)
    else:
        screen.blit(heart_gone[-1], HEART3POS)

    for row in range(len(bunker_states)):
        for col in range(len(bunker_states[row])):
            if bunker_states[row][col]:
                screen.blit(dead_bunker_sprite,(COLUMN_SIZE * col, ROW_SIZE * row))
                
    # stay on the current screen
    return "PLAYING"

def get_coordinates() -> tuple:
    """
    Captures mouse click coordinates and converts them to grid positions.
    
    Returns:
        A tuple containing the grid row and column coordinates
    """

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if mouse_x <= GRID_WIDTH and mouse_y <= GRID_HEIGHT:
                coord: tuple = (mouse_x // (SCREEN_WIDTH//GRID_ROWS)) + 1,(mouse_y // (SCREEN_HEIGHT//GRID_COLUMNS)) + 1
                # get problems for x coordinate and shuffle
                return coord

    

