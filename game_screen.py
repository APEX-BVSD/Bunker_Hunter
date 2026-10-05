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

def display_game_screen(screen: pygame.Surface,background_image: pygame.surface, heart_sprite: list[pygame.Surface], frame_counter: int) -> str:
    screen.fill("Green")
    screen.blit(background_image, (0, 0))
    #hearts
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    screen.blit(heart_sprite[heart_frame],(0,0))
    screen.blit(heart_sprite[heart_frame],(35,0))
    screen.blit(heart_sprite[heart_frame],(67,0))

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


    

