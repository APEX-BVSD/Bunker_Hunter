import pygame
from pygame import font
from equations import*
from settings import *

def display_question_screen(screen: pygame.Surface, equations: dict) -> bool:

    image: pygame.Surface = pygame.image.load("assets/main-screen.png")

    screen.blit(image, (0, 0))

    font: pygame.font.Font = pygame.font.Font(size=48)

    bigger_font: pygame.font.Font = pygame.font.Font(size=90)

    correct: str = equations["correct"]

    problems: list[str] = equations["equations"]

    asking_text_box: pygame.Surface = bigger_font.render(f"Which equation equals {equations["coord"]} ?", True, "white")

    equation1: pygame.Surface = font.render(problems[0], True, "white")

    equation2: pygame.Surface = font.render(problems[1], True, "white")

    equation3: pygame.Surface = font.render(problems[2], True, "white")

    screen.blit(asking_text_box, (screen.get_width() // 2 - asking_text_box.get_width() // 2, screen.get_height() // 10))

    screen.blit(equation1, (screen.get_width() // 2 - equation1.get_width() // 2, screen.get_height() // 4))

    screen.blit(equation2, (screen.get_width() // 2 - equation2.get_width() // 2, screen.get_height() // 3+40))

    screen.blit(equation3, (screen.get_width() // 2 - equation3.get_width() // 2, screen.get_height() // 2))
    

    equation_1_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation1.get_width() // 2, screen.get_height() // 4,EQUATION_RECT_DIMENSIONS[0], EQUATION_RECT_DIMENSIONS[1])

    equation_2_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation2.get_width() // 2, screen.get_height() // 3+40,EQUATION_RECT_DIMENSIONS[0], EQUATION_RECT_DIMENSIONS[1])

    equation_3_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation3.get_width() // 2, screen.get_height() // 2,EQUATION_RECT_DIMENSIONS[0], EQUATION_RECT_DIMENSIONS[1])

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if equation_1_box.collidepoint(event.pos):
                if problems[0] == correct:            
                    return True
                
                else:                 
                    return False
                
            elif equation_2_box.collidepoint(event.pos):
                if problems[1] == correct:
                    return True
                
                else:                  
                    return False
                
            elif equation_3_box.collidepoint(event.pos):
                if problems[2] == correct: 
                    return True
                else:                                 
                    return False
                
            else:
                print("Not clicking an equation!")
                return None

    return None

