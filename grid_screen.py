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

def display_grid_screen(screen: pygame.Surface,background_image: pygame.surface, heart_sprite: list[pygame.Surface], heart_gone: list[pygame.Surface],  frame_counter: int,lives:list[bool]) -> str:
    screen.blit(background_image, (0, 0))
    #hearts
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)

    if lives[2]==True:
        screen.blit(heart_sprite[heart_frame],HEART1POS)
    else: 
        screen.blit(heart_gone[-1],HEART1POS)
    if lives[1]==True:
        screen.blit(heart_sprite[heart_frame],HEART2POS)
    else: 
        screen.blit(heart_gone[-1],HEART2POS)
    if lives[0]==True:
        screen.blit(heart_sprite[heart_frame],HEART3POS)
    else: 
        screen.blit(heart_gone[-1],HEART3POS)

    # stay on the current screen
    return "PLAYING"

def get_coordinates() -> tuple:
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if mouse_x <= 800 and mouse_y <= 800:
                coord: tuple = (mouse_x // (SCREEN_WIDTH//GRID_ROWS)) + 1,(mouse_y // (SCREEN_HEIGHT//GRID_COLUMNS)) + 1
                # get problems for x coordinate and shuffle
                return coord




    

