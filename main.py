"""
Bucket Hunters is a game where you solve math equations to eliminate all the buckets of aliens.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""

import asyncio
import pygame
import random
from settings import *
from start_screen import *
from grid_screen import *
from mode_screen import *
from equations import *
from problem_screen import *
from Intro_screen import *


async def main() -> None:
    """
    Run the main game loop, managing game states and rendering. Displays screens and problems.
    
    Returns:
        None
    """


    background_color: tuple = (100, 255, 100)
    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set title
    pygame.display.set_caption(GAME_TITLE)

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()
    frame_counter: int = 0


    # Load background image for playing screen
    original_image: pygame.Surface = pygame.image.load("assets/Desert.png")
    bigger_image: pygame.Surface = pygame.transform.scale(original_image, (800, 1000))


    # load hearts
    heart_sprite: list[pygame.Surface] = load_sprites("Heart_Idle", 4)

    # MAIN GAME LOOP
    running: bool = True
    game_state: str = "START_SCREEN"
    while running:
        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen)
        
        elif game_state == "INTRO_SCREEN":
            game_state = display_info_screen(screen)

        elif game_state == "MODE_SCREEN":
            game_state = display_mode_screen(screen)

        elif game_state == "PLAYING":
            game_state = display_grid_screen(screen, bigger_image, heart_sprite, frame_counter)
            coord: tuple = get_coordinates()
            if coord is not None:
                game_state = "QUESTION_SCREEN"
                equations: dict = get_equation_set(coord)

        elif game_state == "QUESTION_SCREEN":
            
            game_state = display_question_screen(screen, equations, coord)

        elif game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {game_state}")
            running = False
        
        # render the screen
        pygame.display.flip()
        # advance the clock
        clock.tick(FPS)
        frame_counter += 1
        pygame.event.pump()

        await asyncio.sleep(0)

    # when the loop breaks, shut down pygame gracefully
    pygame.quit()


def load_sprites(file_name: str, sprite_count: int) -> list[pygame.Surface]:
    """
    Load a series of sprite images from the assets folder.
    
    Parameters:
        file_name: The base name of the sprite files (without number suffix)
        sprite_count: The number of sprite images to load
        
    Returns:
        A list of pygame Surface objects containing the loaded sprites
    """
    
    sprite_list: list[pygame.Surface] = []

    for i in range(sprite_count):
        sprite: pygame.Surface = pygame.image.load(f"assets/{file_name}{i}.png")
        sprite_list.append(sprite)

    return sprite_list


asyncio.run(main())