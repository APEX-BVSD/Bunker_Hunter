"""
Contains settings for the game.
Month Year
First Last
First Last 
First Last 
"""


SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 900
GRID_HEIGHT: int = 800
GRID_WIDTH: int = 800
GRID_ROWS: int = 10
GRID_COLUMNS: int = 10
ROW_SIZE: int = GRID_WIDTH // GRID_COLUMNS
COLUMN_SIZE: int = GRID_HEIGHT // GRID_ROWS
EQUATION_RECT_DIMENSIONS: tuple = (200,40)
LOW: int = -20
HIGH: int = 20
ALIEN_COUNT: int = 30
FPS: int = 60
MISSILE_OFFSET: int = 185

GAME_TITLE: str = "Your Game Title"

HEART1POS: tuple = (0,0)
HEART2POS: tuple = (35,0)
HEART3POS: tuple = (67,0)

HEART1POS2: tuple = (0,815)
HEART2POS2: tuple = (35,815)
HEART3POS2: tuple = (67,815)
