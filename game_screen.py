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
from equations import *

def display_game_screen(screen: pygame.Surface) -> str:
    screen.fill("Green")
    original_image: pygame.Surface = pygame.image.load("assets/grid_image.jpg")
    bigger_image: pygame.Surface = pygame.transform.scale(original_image, (800,800))
    screen.blit(bigger_image, (0, 0))
    
    # stay on the current screen
    return "PLAYING"

def mouse_grid_interactions() :
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            print(f"{mouse_x} {mouse_y}")
            print(event.pos)
        
            coord: tuple = (event.pos[0] // (SCREEN_WIDTH//GRID_ROWS)) + 1,(event.pos[1] // (SCREEN_HEIGHT//GRID_COLUMNS)) + 1
            # get problems for x coordinate and shuffle
            correct_x: str = problem(coord[0], make_correct = True)
            wrong_x1: str = problem(coord[0], make_correct = False)
            wrong_x2: str = problem(coord[0], make_correct = False)

            problems_x: list[str] = [correct_x, wrong_x1, wrong_x2]
            
            random.shuffle(problems_x)
            print(problems_x)
            
            correct_y: str = problem(coord[1], make_correct = True)
            wrong_y1: str = problem(coord[1], make_correct = False)
            wrong_y2: str = problem(coord[1], make_correct = False)

            problems_y: list[str] = [correct_y, wrong_y1, wrong_y2]
            
            random.shuffle(problems_y)
            print(problems_y)
            
            #problem(coord)
            print(coord)

    

