import pygame
from pygame import font
from equations import *
from settings import *


def display_question_screen(screen: pygame.Surface, equations: dict, coord: tuple, heart_sprite: list[pygame.Surface],heart_gone: list[pygame.Surface], frame_counter: int,lives:list[bool]) -> str:
    image: pygame.Surface = pygame.image.load("assets/main-screen.png")
    screen.blit(image, (0, 0))
    font: pygame.font.Font = pygame.font.Font(size=48)
    bigger_font: pygame.font.Font = pygame.font.Font(size=90)
    correct_x: str = equations["correct_x"]
    equations_x: list[str] = equations["equations_x"]
    correct_y: str = equations["correct_y"]
    equations_y: list[str] = equations["equations_y"]
    

    asking_text_box_x: pygame.Surface = bigger_font.render(f"Which equation equals {coord[0]} ?", True, "white")

    equation1_x: pygame.Surface = font.render(equations_x[0], True, "white")

    equation2_x: pygame.Surface = font.render(equations_x[1], True, "white")

    equation3_x: pygame.Surface = font.render(equations_x[2], True, "white")
# need to fix wrong or right feedback.
    screen.blit(asking_text_box_x, (screen.get_width() // 2 - asking_text_box_x.get_width() // 2, screen.get_height() // 10))

    screen.blit(equation1_x, (screen.get_width() // 2 - equation1_x.get_width() // 2, screen.get_height() // 4))

    screen.blit(equation2_x, (screen.get_width() // 2 - equation2_x.get_width() // 2, screen.get_height() // 3+40))

    screen.blit(equation3_x, (screen.get_width() // 2 - equation3_x.get_width() // 2, screen.get_height() // 2))
    
    EQUATION_1_X_RECT_DIMENSIONS: tuple = (200,40)
    equation_1_x_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation1_x.get_width() // 2, screen.get_height() // 4,EQUATION_1_X_RECT_DIMENSIONS[0], EQUATION_1_X_RECT_DIMENSIONS[1])

    EQUATION_2_X_RECT_DIMENSIONS: tuple = (200,40)
    equation_2_x_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation2_x.get_width() // 2, screen.get_height() // 3+40,EQUATION_2_X_RECT_DIMENSIONS[0], EQUATION_2_X_RECT_DIMENSIONS[1])

    EQUATION_3_X_RECT_DIMENSIONS: tuple = (200,40)
    equation_3_x_box: pygame.Rect = pygame.Rect(screen.get_width() // 2 - equation3_x.get_width() // 2, screen.get_height() // 2,EQUATION_3_X_RECT_DIMENSIONS[0], EQUATION_3_X_RECT_DIMENSIONS[1])

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if equation_1_x_box.collidepoint(event.pos):
                if equations_x[0] == correct_x:
                    print("Correct!")
                else:
                    print("Wrong!")
                    if lives[0]:
                        lives[0]=False
                    elif lives[1]:
                        lives[1]=False
                    elif lives[2]:
                        lives[2]=False
                    
            elif equation_2_x_box.collidepoint(event.pos):
                if equations_x[1] == correct_x:
                    print("Correct!")
                else:
                    print("Wrong!")
                    if lives[0]:
                        lives[0]=False
                    elif lives[1]:
                        lives[1]=False
                    elif lives[2]:
                        lives[2]=False
            elif equation_3_x_box.collidepoint(event.pos):
                if equations_x[2] == correct_x:
                    print("Correct!")
                else:
                    print("Wrong!")
                    if lives[0]:
                        lives[0]=False
                    elif lives[1]:
                        lives[1]=False
                    elif lives[2]:
                        lives[2]=False
            else:
                print("Not clicking an equation!")
    heart_frame: int = (frame_counter // FPS) % len(heart_sprite)
    heart_death: int = (frame_counter // FPS) % len(heart_gone)
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





    """
    asking_text_box_y: pygame.Surface = bigger_font.render(f"Which equation equals {coord[1]}", True, "white")
    equation1_y: pygame.Surface = font.render(equations_y[0], True, "white")
    equation2_y: pygame.Surface = font.render(equations_y[1], True, "white")
    equation3_y: pygame.Surface = font.render(equations_y[2], True, "white")

    screen.blit(asking_text_box_y, (screen.get_width() // 2 - asking_text_box_y.get_width() // 2, screen.get_height() // 10))
    screen.blit(equation1_y, (screen.get_width() // 2 - equation1_y.get_width() // 2, screen.get_height() // 4))
    screen.blit(equation2_y, (screen.get_width() // 2 - equation2_y.get_width() // 2, screen.get_height() // 3+40))
    screen.blit(equation3_y, (screen.get_width() // 2 - equation3_y.get_width() // 2, screen.get_height() // 2))  
    """

    return "QUESTION_SCREEN"
    