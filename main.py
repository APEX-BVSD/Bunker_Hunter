"""
Describe your game.
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

random.randint(1,9)
async def main() -> None:

    Background_color: tuple = (100,255,100)
    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    # set title
    pygame.display.set_caption(GAME_TITLE)

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()
    frame_counter: int = 0

    #Load background image for playing screen
    original_image: pygame.Surface = pygame.image.load("assets/grid_image.jpg")
    bigger_image: pygame.Surface = pygame.transform.scale(original_image, (800,800))

    # load hearts
    heart_sprite: list[pygame.Surface] = load_sprites("Heart_Idle", 4)

    # MAIN GAME LOOP
    running: bool = True
    game_state: str = "START_SCREEN"
    while running:
        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen)

        elif game_state == "MODE_SCREEN":
            game_state = display_mode_screen(screen)

        elif game_state == "PLAYING":
            game_state = display_grid_screen(screen,bigger_image, heart_sprite, frame_counter)
            coord: tuple = get_coordinates()
            if coord is not None:
                game_state = "LOAD_QUESTION_SCREEN"

        elif game_state == "LOAD_QUESTION_SCREEN": 
            game_state = display_question_screen(screen, coord)

        elif game_state == "QUESTION_SCREEN":
            pass

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
    sprite_list: list[pygame.Surface] = []

    for i in range(sprite_count):
        sprite: pygame.Surface = pygame.image.load(f"assets/{file_name}{i}.png")
        sprite_list.append(sprite)

    return sprite_list


asyncio.run(main())