import pygame
from pygame import font
from equations import*

def display_question_screen(screen: pygame.Surface, coord: tuple) -> str:
    image: pygame.Surface = pygame.image.load("assets/Space-Background-Image.jpg")
    screen.blit(image, (0, 0))
    font: pygame.font.Font = pygame.font.Font(size=48)
    bigger_font: pygame.font.Font = pygame.font.Font(size=90)
    equations_x, equations_y = get_equation_set(coord)

    asking_text_box_x: pygame.Surface = bigger_font.render(f"Which equation equals {coord[0]}", True, "white")
    equation1_x: pygame.Surface = font.render(equations_x[0], True, "white")
    equation2_x: pygame.Surface = font.render(equations_x[1], True, "white")
    equation3_x: pygame.Surface = font.render(equations_x[2], True, "white")
    screen.blit(asking_text_box_x, (screen.get_width() // 2 - asking_text_box_x.get_width() // 2, screen.get_height() // 10))
    screen.blit(equation1_x, (screen.get_width() // 2 - equation1_x.get_width() // 2, screen.get_height() // 4))
    screen.blit(equation2_x, (screen.get_width() // 2 - equation2_x.get_width() // 2, screen.get_height() // 3+40))
    screen.blit(equation3_x, (screen.get_width() // 2 - equation3_x.get_width() // 2, screen.get_height() // 2))

    """asking_text_box_y: pygame.Surface = bigger_font.render(f"Which equation equals {coord[1]}", True, "white")
    equation1_y: pygame.Surface = font.render(equations_y[0], True, "white")
    equation2_y: pygame.Surface = font.render(equations_y[1], True, "white")
    equation3_y: pygame.Surface = font.render(equations_y[2], True, "white")"""

    return "QUESTION_SCREEN"
    