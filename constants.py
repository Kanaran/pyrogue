import pygame

pygame.init()

# game sizes
GAME_WIDTH = 800
GAME_HEIGHT = 800

# map vars
MAP_WIDTH = 25
MAP_HEIGHT = 25
CELL_WIDTH = 32
CELL_HEIGHT = 32

# color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

# game colors
COLOR_DEFAULT_BG = COLOR_GREY

# sprites
S_PLAYER = pygame.image.load("img/snake.png")
S_WALL = pygame.image.load("img/wall.png")
S_FLOOR = pygame.image.load("img/floor.png")