"""
Bucket Hunters is a game where you solve math equations to eliminate all the buckets of aliens.
October 2026
Yoav Bierkatz
Jude Averitt
Kaplan Tonelli
Main background image from (https://easy-peasy.ai/ai-image-generator/images/genera-un-pixel-art-9b8a92a9-eb53-4ce5-8ae0-d74c8f95d824)
Green alien image on main background from (https://www.vecteezy.com/vector-art/66675512-pixel-alien-emerging-from-ground-green-extraterrestrial-character-retro-game-art)
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
from winner_screen import *
pygame.mixer.init()


async def main() -> None:
    """
    Run the main game loop, managing game states and rendering. Displays screens and problems.
    
    Returns:
        None
    """
    pygame.init()
    # Sounds
    owchie_sound: pygame.mixer.Sound = pygame.mixer.Sound("assets/owchie.ogg")
    explosion_sound: pygame.mixer.Sound = pygame.mixer.Sound("assets/explosion.ogg")
    background_music: pygame.mixer.Sound = pygame.mixer.Sound("assets/background_music.ogg")
    background_music.set_volume(0.10)
    ding_sound: pygame.mixer.Sound = pygame.mixer.Sound("assets/Ding.ogg")
    win_sound: pygame.mixer.Sound = pygame.mixer.Sound("assets/You_Win.ogg")
    
    background_color: tuple = (100, 255, 100)
    
    # Set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set title
    pygame.display.set_caption(GAME_TITLE)

    # Create clock
    clock: pygame.time.Clock = pygame.time.Clock()
    frame_counter: int = 0


    # Load background image for playing screen
    original_image: pygame.Surface = pygame.image.load("assets/Desert.png")
    bigger_image: pygame.Surface = pygame.transform.scale(original_image, (800, 1000))
    main_image: pygame.Surface = pygame.image.load("assets/main-screen.png")


    # Load hearts
    heart_gone: list[pygame.Surface] = load_sprites("Heart_gone", 12)
    heart_sprite: list[pygame.Surface] = load_sprites("Heart_Idle", 4)
    lives: list[bool] = [True, True, True]

    # Load more sprites
    dead_bunker_sprite: pygame.Surface = pygame.image.load("assets/dead_bunker_sprite.png")
    idle_missile_sprite: pygame.Surface = pygame.image.load("assets/Missile_Idle0.png")
    flying_missile_sprite: pygame.Surface = pygame.image.load("assets/missile_flying_sprite.png")

    # Load dead desert sprite
    dead_desert_sprite: pygame.Surface = pygame.image.load("assets/dead_desert_sprite.png")

    # bunkers

    ROW_COUNT = 0
    bunker_aliens: list[list[bool]] = []
    bunker_states: list[list[bool]] = []

    # If missile is flying
    missile_flying: bool = False
    missile_flying_location: int = 815
    missile_flying_speed: int = (SCREEN_HEIGHT - MISSILE_OFFSET) // FPS
    

    # MAIN GAME LOOP
    running: bool = True
    last_clicked_coord: tuple = (-1, -1)
    game_state: str = "SET_GAME"
    background_music.play(-1)
    while running:
        if game_state == "SET_GAME":
            bunker_aliens = []
            for  _ in range(GRID_ROWS):
                bunker_aliens.append( [False] * GRID_COLUMNS )
            bunker_number: str = ALIEN_COUNT
            # Randomly Generates the location of the bunkers 
            aliens_placed: int = 0
            while aliens_placed < ALIEN_COUNT:
                col: int = random.randint(0,GRID_ROWS - 1)
                row: int = random.randint(0,GRID_COLUMNS - 1)
                if not bunker_aliens[row][col]:
                    bunker_aliens[row][col] = True
                    aliens_placed += 1
            print(bunker_aliens)

            bunker_states = []
            for  _ in range(GRID_ROWS):
                bunker_states.append( [False] * GRID_COLUMNS )
            game_state = "START_SCREEN"

        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen, main_image)
        
        elif game_state == "INTRO_SCREEN":
            game_state = display_info_screen(screen, main_image)

        elif game_state == "MODE_SCREEN":
            game_state = display_mode_screen(screen, main_image)

        elif game_state == "PLAYING":
            coord: tuple = get_coordinates()
            

            game_state = display_grid_screen(screen, bigger_image, heart_sprite, frame_counter,
                                            lives, heart_gone, bunker_aliens, bunker_states, dead_bunker_sprite, 
                                            bunker_number, dead_desert_sprite, idle_missile_sprite, flying_missile_sprite,
                                            missile_flying, missile_flying_location, missile_flying_speed, last_clicked_coord,
                                            game_state)
            if coord is not None:
                last_clicked_coord = coord
                game_state = "X_QUESTION_SCREEN"
                equations_x: dict = get_equation_set(coord[0])
                equations_y: dict = get_equation_set(coord[1])   

            if missile_flying:
                missile_flying_location -= missile_flying_speed

            if missile_flying_location <= 0:
                last_clicked_coord = (-1, -1)
                missile_flying = False
                missile_flying_location = 815

        elif game_state == "X_QUESTION_SCREEN":
            result: bool = display_question_screen(screen, equations_x, heart_sprite, heart_gone, frame_counter, lives, owchie_sound, explosion_sound, background_music, main_image)
            if result:
                ding_sound.play()
                game_state = "Y_QUESTION_SCREEN"
            elif result == False:
                game_state = "PLAYING"
            else: 
                game_state = "X_QUESTION_SCREEN"

        elif game_state == "Y_QUESTION_SCREEN":
            result: bool = display_question_screen(screen, equations_y, heart_sprite, heart_gone, frame_counter, lives, owchie_sound, explosion_sound, background_music, main_image)
            if result:
                # Finish implementing the bunkers
                explosion_sound.play()
                bunker_states[row][col] == True
                col, row = coord
                row -= 1
                col -= 1

                if bunker_states[row][col] == False:
                    bunker_states[row][col] = True
                    if bunker_aliens[row][col]:
                        bunker_number -= 1
                missile_flying = True
                print(lives)
                if bunker_number == 0:
                    game_state = "WIN_SCREEN"
                else:
                    game_state = "PLAYING"

            elif result == False:
                game_state = "PLAYING"
            else: 
                game_state = "Y_QUESTION_SCREEN"
                
        elif game_state == "GAME_OVER":
            game_state = display_game_over_screen(screen, lives, main_image)
       
        elif game_state == "WIN_SCREEN":
             game_state = display_win_screen(screen,main_image)
        else:
            print(f"Invalid game state: {game_state}")
            running = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Render the screen
        pygame.display.flip()
        # Advance the clock
        clock.tick(FPS)
        frame_counter += 1
        pygame.event.pump()

        await asyncio.sleep(0)

    # When the loop breaks, shut down pygame gracefully
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

