"""
Contains functions that implement the start screen.
Month Year
First Last
First Last 
First Last 
"""


import pygame
from pygame import font

def display_mode_screen(screen: pygame.Surface) -> str:
    """
    Displays the start screen text and waits for the player to press the space key.
    Returns "PLAYING" as the next game state.

    Parameters:
    screen(pygame.Surface): The screen to render the game on
    
    Returns:
    str: The game state the game should use in the next frame
    
    """
    
    # draw the screen
    image: pygame.Surface = pygame.image.load("assets/Space-Background-Image.jpg")
    font: pygame.font.Font = pygame.font.Font(size=48)
    bigger_font: pygame.font.Font = pygame.font.Font(size=100)
    text_box1: pygame.Surface = bigger_font.render("MODES", True, "white")
    text_box2: pygame.Surface = font.render("MODE 1 (+,-)", True, "white")
    text_box3: pygame.Surface = font.render("MODE 2 (*,/)", True, "white")
    text_box4: pygame.Surface = font.render("MODE 3 (Algebra)", True, "white")

    screen.blit(image, (0, 0))
    screen.blit(text_box1, (screen.get_width() // 2 - text_box1.get_width() // 2, screen.get_height() // 10))
    screen.blit(text_box2, (screen.get_width() // 2 - text_box2.get_width() // 2, screen.get_height() // 4))
    screen.blit(text_box3, (screen.get_width() // 2 - text_box3.get_width() // 2, screen.get_height() // 3+40))
    screen.blit(text_box4, (screen.get_width() // 2 - text_box4.get_width() // 2, screen.get_height() // 2))


    # process the events, if the space button was pressed, move to the next screen
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "PLAYING"

    # stay on the current screen
    return "MODE_SCREEN"


