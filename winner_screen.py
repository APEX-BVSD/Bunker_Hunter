"""
Contains functions that implement the start screen.
Month Year
First Last
First Last 
First Last 
"""


import pygame
from pygame import font

def display_win_screen(screen: pygame.Surface, main_image:pygame.Surface) -> str:
    """
    Displays the win screen text and waits for the player to press the space key.
    Returns "PLAYING" as the next game state.

    Parameters:
    screen(pygame.Surface): The screen to render the game on
    
    Returns:
    str: The game state the game should use in the next frame
    
    """
    
    # draw the screen
    font: pygame.font.Font = pygame.font.Font(size=48)
    bigger_font: pygame.font.Font = pygame.font.Font(size=80)
    middle_font:pygame.font.Font = pygame.font.Font(size=100)
    text_box1: pygame.Surface = bigger_font.render("""   You Defeated The Aliens!""", True, "white")
    text_box3: pygame.Surface = bigger_font.render("""             You Win""", True, "white")
    text_box2: pygame.Surface = font.render("""
    Press The Space Bar To Play Again""", True, "white")
    Mode_Button:pygame.Rect= pygame.Rect(screen.get_width() // 2 - text_box2.get_width() // 2, screen.get_height() // 4, 200, 30)
    screen.blit(main_image, (0, 0))
    screen.blit(text_box1, (screen.get_width() // 2 - text_box1.get_width() // 2, screen.get_height() // 9))
    screen.blit(text_box3, (screen.get_width() // 2 - text_box2.get_width() // 2, screen.get_height() // 5))
    screen.blit(text_box2, (screen.get_width() // 2 - text_box2.get_width() // 2, screen.get_height() // 3))
    


    # process the events, if the space button was pressed, move to the next screen
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "START_SCREEN"

    # stay on the current screen
    return "WIN_SCREEN"


