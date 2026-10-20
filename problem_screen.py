"""
Contains functions that display the question screen and handle user answers.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""

import pygame
from pygame import font
from equations import *
from settings import *

def display_question_screen(screen: pygame.Surface, equations: dict, heart_sprite: list[pygame.Surface], heart_gone: list[pygame.Surface], frame_counter: int, lives: list[bool],owchie_sound:pygame.mixer.Sound, explosion_sound:pygame.mixer.Sound, background_music: pygame.mixer.Sound) -> bool:
    """
    Displays the question screen with three equation choices and handles user selection.

    Parameters:
        screen: The screen to render the question on
        equations: Dictionary containing the correct answer and equation choices
        heart_sprite: List of heart animation frames
        heart_gone: List of empty heart sprites
        frame_counter: Current frame count for animation
        lives: List of booleans representing remaining lives

    Returns:
        True if correct answer selected, False if incorrect, None if no selection
    """
    # Load and display background
    image: pygame.Surface = pygame.image.load("assets/main-screen.png")

    screen.blit(image, (0, 0))

    # Set up fonts
    font: pygame.font.Font = pygame.font.Font(size=48)

    bigger_font: pygame.font.Font = pygame.font.Font(size=90)

    # Render question and equation text
    correct: str = equations["correct"]

    problems: list[str] = equations["equations"]

    asking_text_box: pygame.Surface = bigger_font.render(f"Which equation equals {equations["coord"]}?", True, "white","Black")
    asking_text_box.set_alpha(180)
    equation1: pygame.Surface = font.render(problems[0], True, "white","Black")
    equation1.set_alpha(180)
    equation2: pygame.Surface = font.render(problems[1], True, "white","Black")
    equation2.set_alpha(180)
    equation3: pygame.Surface = font.render(problems[2], True, "white","Black")
    equation3.set_alpha(180)

    # Create clickable rectangles for each equation
    screen.blit(asking_text_box, (screen.get_width() // 2 - asking_text_box.get_width() // 2, screen.get_height() // 10))

    screen.blit(equation1, (screen.get_width() // 2 - equation1.get_width() // 2, screen.get_height() // 4))

    screen.blit(equation2, (screen.get_width() // 2 - equation2.get_width() // 2, screen.get_height() // 3 + 40))

    screen.blit(equation3, (screen.get_width() // 2 - equation3.get_width() // 2, screen.get_height() // 2))
    

    equation_1_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation1.get_width() // 2, screen.get_height() // 4, EQUATION_RECT_DIMENSIONS[0], EQUATION_RECT_DIMENSIONS[1])

    equation_2_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation2.get_width() // 2, screen.get_height() // 3 + 40, EQUATION_RECT_DIMENSIONS[0], EQUATION_RECT_DIMENSIONS[1])

    equation_3_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation3.get_width() // 2, screen.get_height() // 2, EQUATION_RECT_DIMENSIONS[0], EQUATION_RECT_DIMENSIONS[1])
    
    
    
    # Display hearts based on remaining lives
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    heart_death: int = (frame_counter // FPS) % len(heart_gone)
    if lives[2] == True:
        screen.blit(heart_sprite[heart_frame], HEART1POS)
    else: 
        screen.blit(heart_gone[-1], HEART1POS)
    if lives[1] == True:
        screen.blit(heart_sprite[heart_frame], HEART2POS)
    else: 
        screen.blit(heart_gone[-1], HEART2POS)
    if lives[0] == True:
        screen.blit(heart_sprite[heart_frame], HEART3POS)
    else: 
        screen.blit(heart_gone[-1], HEART3POS)

    # Handle mouse clicks on equations
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if equation_1_box.collidepoint(event.pos):
                if problems[0] == correct:
                    explosion_sound.play()                  
                    return True
                else:
                    owchie_sound.play()              
                    if lives[0]:
                        lives[0] = False
                    elif lives[1]:
                        lives[1] = False
                    elif lives[2]:
                        lives[2] = False
                    return False
            elif equation_2_box.collidepoint(event.pos):
                if problems[1] == correct:
                    explosion_sound.play()    
                    return True
                else:  
                    owchie_sound.play()    
                    if lives[0]:
                        lives[0] = False
                    elif lives[1]:
                        lives[1] = False
                    elif lives[2]:
                        lives[2] = False                
                    return False
            elif equation_3_box.collidepoint(event.pos):
                if problems[2] == correct: 
                    explosion_sound.play()    
                    return True
                else:         
                    owchie_sound.play()     
                    if lives[0]:
                        lives[0] = False
                    elif lives[1]:
                        lives[1] = False
                    elif lives[2]:
                        lives[2] = False                       
                    return False
            else:
                print("Not clicking an equation!")
            return None