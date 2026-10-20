"""
Bucket Hunters is a game where you solve math equations to eliminate all the buckets of aliens.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
Background music from pixabay(https://pixabay.com/music/electronic-game-game-music-508018/)
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
from game_over_screen import *
pygame.mixer.init()


async def main() -> None:
    """
    Run the main game loop, managing game states and rendering. Displays screens and problems.
    
    Returns:
        None
    """
    #sounds
    owchie_sound: pygame.mixer.Sound = pygame.mixer.Sound("assets/owchie.ogg")
    explosion_sound: pygame.mixer.Sound = pygame.mixer.Sound("assets/explosion.ogg")
    background_music: pygame.mixer.Sound = pygame.mixer.Sound("assets/Background_Music.ogg")
    background_music.set_volume(0.10)
    
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
    heart_gone: list[pygame.Surface] = load_sprites("Heart_gone", 12)
    heart_sprite: list[pygame.Surface] = load_sprites("Heart_Idle", 4)
    lives: list[bool] = [True, True, True]

    # load dead bunkers
    dead_bunker_sprite: pygame.Surface = pygame.image.load("assets/dead_bunker_sprite.png")

    # bunkers
    bunker_number:str =30
    ROW_COUNT = 0
    bunker_aliens: list[list[bool]] = []
    for  _ in range(GRID_ROWS):
        bunker_aliens.append( [False] * GRID_COLUMNS )
    # Randomly Generates the location of the bunkers 
    aliens_placed: int = 0
    while aliens_placed < ALIEN_COUNT:
        col: int = random.randint(0,GRID_ROWS - 1)
        row: int = random.randint(0,GRID_COLUMNS - 1)
        if not bunker_aliens[row][col]:
            bunker_aliens[row][col] = True
            aliens_placed += 1
    print(bunker_aliens)

    bunker_states: list[list[bool]] = []
    for  _ in range(GRID_ROWS):
        bunker_states.append( [False] * GRID_COLUMNS )

    # MAIN GAME LOOP
    running: bool = True
    game_state: str = "START_SCREEN"
    background_music.play(-1)
    while running:

        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen)
        
        elif game_state == "INTRO_SCREEN":
            game_state = display_info_screen(screen)

        elif game_state == "MODE_SCREEN":
            game_state = display_mode_screen(screen)

        elif game_state == "PLAYING":
            game_state = display_grid_screen(screen, bigger_image, heart_sprite, frame_counter, lives, heart_gone, bunker_aliens, bunker_states, dead_bunker_sprite,bunker_number)
            coord: tuple = get_coordinates()
            if coord is not None:
                game_state = "X_QUESTION_SCREEN"
                equations_x: dict = get_equation_set(coord[0])
                equations_y: dict = get_equation_set(coord[1])
        elif game_state == "X_QUESTION_SCREEN":
            result: bool = display_question_screen(screen, equations_x, heart_sprite, heart_gone, frame_counter, lives, owchie_sound, explosion_sound,background_music)
            if result:
                game_state = "Y_QUESTION_SCREEN"
            elif result == False:
                game_state = "PLAYING"
            else: 
                game_state = "X_QUESTION_SCREEN"

        elif game_state == "Y_QUESTION_SCREEN":
            result: bool = display_question_screen(screen, equations_y, heart_sprite, heart_gone, frame_counter, lives, owchie_sound, explosion_sound,background_music)
            if result:
                #Finish implementing the bunkers     
                bunker_states[row][col] == True
                col, row = coord
                row -= 1
                col -= 1

                if bunker_aliens[row][col] and bunker_states[row][col] == False:
                    bunker_states[row][col] = True
                    bunker_number-=1
                game_state = "PLAYING"                
            elif result == False:
                game_state = "PLAYING"
            else: 
                game_state = "Y_QUESTION_SCREEN"
                
        elif game_state == "GAME_OVER":
            game_state = display_game_over_screen(screen,lives)

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
