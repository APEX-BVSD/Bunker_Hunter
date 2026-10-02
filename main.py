"""
Describe your game.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
"""

import asyncio
import pygame
from settings import *
from start_screen import *
from game_screen import *

async def main() -> None:

    Background_color: tuple = (100,255,100)
    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    # set title
    pygame.display.set_caption(GAME_TITLE)

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()


    # MAIN GAME LOOP
    running: bool = True
    game_state: str = "START_SCREEN"
    while running:
        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen)

        elif game_state == "PLAYING":
            game_state = display_game_screen(screen)
            mouse_grid_interactions()
            
        elif game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {game_state}")
            running = False
        
        # render the screen
        pygame.display.flip()
        # advance the clock
        clock.tick(FPS)
        pygame.event.pump()

        await asyncio.sleep(0)

    # when the loop breaks, shut down pygame gracefully
    pygame.quit()


asyncio.run(main())