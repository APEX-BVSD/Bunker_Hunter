"""
Implements the start screen for the Bunker Hunters game.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""




import pygame
from pygame import font
from settings import *


def display_info_screen(screen: pygame.Surface,main_image:pygame.Surface) -> str:
    """
    Displays the start screen text and waits for the player to press the space key.
    Returns "PLAYING" as the next game state.


    Parameters:
    screen(pygame.Surface): The screen to render the game on
   
    Returns:
    str: The game state the game should use in the next frame
   
    """
   
    # draw the screen
    font: pygame.font.Font = pygame.font.Font(size=35)
    bigger_font: pygame.font.Font = pygame.font.Font(size=100)
    middle_font: pygame.font.Font = pygame.font.Font(size=80)
    text_box1: pygame.Surface = bigger_font.render("Bunker Hunters", True, "white")
    text_box2: pygame.Surface = font.render("""
    You are a high raking military officer 
    and you're the only person the higher-ups
    trust with this mission. You have been sent
    out to the desert where they have confirmed
    that there are 30 alien bunkers. Your task
    will be to find all of the aliens and 
    eliminate them. To find the bunkers you will
    select a Box and two sets of 3 equations
    will show up, you will select the equation
    that is correct. If you select the correct 
    equation two times in a row you will launch
    your rocket to the selected Box. If you 
    select a wrong equation you will lose a
    life. you have three lives to eliminate the
    all the alien bunkers. 
    Good luck on your mission soldier""", True, "white",(0, 0, 0))
    text_box2.set_alpha(200)
   
    text_box3: pygame.Surface = middle_font.render("""
   
   


   
    Press space to continue""", True, "white")




    screen.blit(main_image, (0, 0))
    screen.blit(text_box1, (screen.get_width() // 2 - text_box1.get_width() // 2, screen.get_height() // 10))
    screen.blit(text_box2, (screen.get_width() // 2 - text_box2.get_width() // 2, screen.get_height() // 4))
    screen.blit(text_box3, (screen.get_width() // 2 - text_box3.get_width() // 2, screen.get_height() // 2))
   
    # process the events, if the space button was pressed, move to the next screen
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "MODE_SCREEN"


    # stay on the current screen
    return "INTRO_SCREEN"
