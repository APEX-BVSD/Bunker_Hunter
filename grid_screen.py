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

def display_grid_screen(screen: pygame.Surface,background_image: pygame.surface, heart_sprite: list[pygame.Surface], 
                        frame_counter: int, lives:list[bool], heart_gone: list[pygame.Surface], bunker_aliens: list[list[bool]], 
                        bunker_states: list[list[bool]], dead_bunker_sprite: pygame.Surface, bunker_number:str, 
                        dead_desert_sprite: pygame.Surface, idle_missile_sprite: pygame.Surface, flying_missile_sprite: pygame.Surface,
                        missile_flying: bool, missile_flying_location: int, missile_flying_speed: int, last_clicked_coord: tuple, game_state: str) -> str:
    """
    Displays the game grid screen with hearts showing remaining lives.
    
    Parameters:
        screen (pygame.Surface): The screen to render the game on
        background_image (pygame.Surface): The background image for the grid
        heart_sprite (list[pygame.Surface]): List of heart animation frames
        frame_counter (int): Current frame count for animation
        lives (list[bool]): List of booleans representing remaining lives
        heart_gone (list[pygame.Surface]): List of empty heart sprites
        bunker_aliens (list[list[bool]]): 2D list tracking which bunkers contain aliens
        bunker_states (list[list[bool]]): 2D list tracking which bunkers have been destroyed
        dead_bunker_sprite (pygame.Surface): Sprite for destroyed bunkers
        bunker_number (str): String showing the number of remaining bunkers
        dead_desert_sprite (pygame.Surface): Sprite for empty destroyed locations
    
    Returns:
        str: The game state for the next frame
    """
    screen.blit(background_image, (0, 0))
    #sound

    # Display hearts based on remaining lives
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    
    font: pygame.font.Font = pygame.font.Font(size=48)
    text_box: pygame.Surface = font.render(f"Bunkers left: {bunker_number}", True, "black")
    screen.blit(text_box, (540, 825))
        
    #display flying missile
    if missile_flying and missile_flying_location >= 0:
        screen.blit(flying_missile_sprite, (350, missile_flying_location))
    else:
        screen.blit(idle_missile_sprite, (350, 815))
    for row in range(len(bunker_states)):
        for col in range(len(bunker_states[row])):
            if bunker_states[row][col] and (last_clicked_coord[0] -1 != col or last_clicked_coord[1] -1 != row):
                if bunker_aliens[row][col]:
                    screen.blit(dead_bunker_sprite,(COLUMN_SIZE * col, ROW_SIZE * row))
                else:
                    screen.blit(dead_desert_sprite,(COLUMN_SIZE * col, ROW_SIZE * row))  

    if lives[2]:
        screen.blit(heart_sprite[heart_frame], HEART1POS2)
    else:
        screen.blit(heart_gone[-1], HEART1POS2)
        return "GAME_OVER"
    if lives[1]:
        screen.blit(heart_sprite[heart_frame], HEART2POS2)
    else:
        screen.blit(heart_gone[-1], HEART2POS2)
    if lives[0]:
        screen.blit(heart_sprite[heart_frame], HEART3POS2)
    else:
        screen.blit(heart_gone[-1], HEART3POS2)


                
    # return current game state
    return game_state

def get_coordinates() -> tuple:
    """
    Captures mouse click coordinates and converts them to grid positions.
    
    Returns:
        tuple: A tuple containing the grid row and column coordinates

    """

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if mouse_x <= GRID_WIDTH and mouse_y <= GRID_HEIGHT:
                coord: tuple = (mouse_x // (GRID_WIDTH//GRID_ROWS)) + 1,(mouse_y // (GRID_HEIGHT//GRID_COLUMNS)) + 1
                # get problems for x coordinate and shuffle
                return coord
