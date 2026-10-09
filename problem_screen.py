import pygame
from pygame import font
from equations import*

def display_question_screen(screen: pygame.Surface, equations: dict, coord: tuple) -> str:
    image: pygame.Surface = pygame.image.load("assets/Space-Background-Image.jpg")
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
            elif equation_2_x_box.collidepoint(event.pos):
                if equations_x[1] == correct_x:
                    print("Correct!")
                else:
                    print("Wrong!")
            elif equation_3_x_box.collidepoint(event.pos):
                if equations_x[2] == correct_x:
                    print("Correct!")
                else:
                    print("Wrong!")
            else:
                print("Not clicking an equation!")


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
    