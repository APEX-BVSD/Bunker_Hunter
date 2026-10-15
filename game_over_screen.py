"""
Displays the game over screen screen for Bunker Hunters game.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""


import pygame
from pygame import font

def display_game_over_screen(screen: pygame.Surface, lives:list[bool]) -> str:
    """
    Displays the game over screen text and waits for the player to press the space key.
    Returns "START_SCREEN" as the next game state.

    Parameters:
        screen: The screen to render the game on
    
    Returns:
        The game state the game should use in the next frame

    """
    
    # draw the screen
    image: pygame.Surface = pygame.image.load("assets/main-screen.png")
    screen.blit(image, (0, 0))

    font: pygame.font.Font = pygame.font.Font(size=48)
    bigger_font: pygame.font.Font = pygame.font.Font(size=100)
    text_box: pygame.Surface = font.render("Press space to try again", True, "white")
    screen.blit(text_box, (screen.get_width() // 2 - text_box.get_width() // 2, screen.get_height() // 2))
    text_box2: pygame.Surface = bigger_font.render("GAME OVER", True, "white")
    screen.blit(text_box2, (screen.get_width() // 2 - text_box2.get_width() // 2, screen.get_height() // 3))

    #Reset everything
    lives[0]=True
    lives[1]=True
    lives[2]=True



    # process the events, if the space button was pressed, move to the next screen
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return "START_SCREEN"


    # stay on the current screen
    return "GAME_OVER"


