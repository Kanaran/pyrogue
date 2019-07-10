import tcod as libtcod
import pygame
import math
import pickle
import gzip
import random
import sys
import datetime
import os

import constants

SURFACE_MAIN = None

#   /$$$$$$   /$$                                     /$$                                            
#  /$$__  $$ | $$                                    | $$                                            
# | $$  \__//$$$$$$    /$$$$$$  /$$   /$$  /$$$$$$$ /$$$$$$   /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$$
# |  $$$$$$|_  $$_/   /$$__  $$| $$  | $$ /$$_____/|_  $$_/  | $$  | $$ /$$__  $$ /$$__  $$ /$$_____/
#  \____  $$ | $$    | $$  \__/| $$  | $$| $$        | $$    | $$  | $$| $$  \__/| $$$$$$$$|  $$$$$$ 
#  /$$  \ $$ | $$ /$$| $$      | $$  | $$| $$        | $$ /$$| $$  | $$| $$      | $$_____/ \____  $$
# |  $$$$$$/ |  $$$$/| $$      |  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      |  $$$$$$$ /$$$$$$$/
#  \______/   \___/  |__/       \______/  \_______/   \___/   \______/ |__/       \_______/|_______/


class struc_Tile:
  def __init__(self, block_path):
    self.block_path = block_path

#   /$$$$$$              /$$                                  
#  /$$__  $$            | $$                                  
# | $$  \ $$  /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$$
# | $$$$$$$$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$ /$$_____/
# | $$__  $$| $$        | $$    | $$  \ $$| $$  \__/|  $$$$$$ 
# | $$  | $$| $$        | $$ /$$| $$  | $$| $$       \____  $$
# | $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$       /$$$$$$$/
# |__/  |__/ \_______/   \___/   \______/ |__/      |_______/  
                                                                       

class obj_Actor:
  def __init__(self, x, y, sprite):
    self.x = x
    self.y = y
    self.sprite = sprite
    
  def draw(self):
    SURFACE_MAIN.blit(self.sprite, ( self.x * constants.CELL_WIDTH, self.y * constants.CELL_HEIGHT ))
    
  def move(self, dx, dy):
    if self.x + dx >= 0 and self.x + dx < constants.MAP_WIDTH and self.y + dy >= 0 and self.y + dy < constants.MAP_HEIGHT and GAME_MAP[self.x + dx][self.y + dy].block_path == False:
      self.x += dx
      self.y += dy
 
#  /$$      /$$                    
# | $$$    /$$$                    
# | $$$$  /$$$$  /$$$$$$   /$$$$$$ 
# | $$ $$/$$ $$ |____  $$ /$$__  $$
# | $$  $$$| $$  /$$$$$$$| $$  \ $$
# | $$\  $ | $$ /$$__  $$| $$  | $$
# | $$ \/  | $$|  $$$$$$$| $$$$$$$/
# |__/     |__/ \_______/| $$____/ 
#                        | $$      
#                        | $$      
#                        |__/     

   
def map_create():
  new_map = [[ struc_Tile(False) for y in range(0, constants.MAP_HEIGHT) ] for x in range(0, constants.MAP_WIDTH)]
  
  new_map[10][10].block_path = True
  new_map[10][15].block_path = True
  
  return new_map

#  /$$$$$$$                                   /$$                    
# | $$__  $$                                 |__/                    
# | $$  \ $$  /$$$$$$  /$$$$$$  /$$  /$$  /$$ /$$ /$$$$$$$   /$$$$$$ 
# | $$  | $$ /$$__  $$|____  $$| $$ | $$ | $$| $$| $$__  $$ /$$__  $$
# | $$  | $$| $$  \__/ /$$$$$$$| $$ | $$ | $$| $$| $$  \ $$| $$  \ $$
# | $$  | $$| $$      /$$__  $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$
# | $$$$$$$/| $$     |  $$$$$$$|  $$$$$/$$$$/| $$| $$  | $$|  $$$$$$$
# |_______/ |__/      \_______/ \_____/\___/ |__/|__/  |__/ \____  $$
#                                                           /$$  \ $$
#                                                          |  $$$$$$/
#                                                           \______/  


def draw_game():
  global SURFACE_MAIN
  
  # clear the surface
  SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)
  
  # draw the map
  draw_map(GAME_MAP)
  
  # draw the character
  PLAYER.draw()
  
  # update the display
  pygame.display.flip()

def draw_map(map_to_draw):
  for x in range(0, constants.MAP_WIDTH):
    for y in range(0, constants.MAP_HEIGHT):
      if map_to_draw[x][y].block_path == True:
        # draw wall
        SURFACE_MAIN.blit(constants.S_WALL, ( x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT ))
      else:
        # draw floor
        SURFACE_MAIN.blit(constants.S_FLOOR, ( x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT ))

#   /$$$$$$                                   
#  /$$__  $$                                  
# | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
# | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
# | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
# | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
# |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
#  \______/  \_______/|__/ |__/ |__/ \_______/

 
def game_main_loop():
  game_quit = False
  
  while not game_quit:
    # collect input
    events_list = pygame.event.get()
    
    #TODO process input
    for event in events_list:
      if event.type == pygame.QUIT:
        game_quit = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          PLAYER.move(0, -1)
        if event.key == pygame.K_DOWN:
          PLAYER.move(0, 1)
        if event.key == pygame.K_LEFT:
          PLAYER.move(-1, 0)
        if event.key == pygame.K_RIGHT:
          PLAYER.move(1, 0)
    
    # draw
    draw_game()
    
  # quit
  pygame.quit()
  exit()

def game_initialize():
  global SURFACE_MAIN, GAME_MAP, PLAYER
  
  pygame.init()
  SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )
  
  GAME_MAP = map_create()
  
  PLAYER = obj_Actor(0, 0, constants.S_PLAYER)
 
 
#  /$$$$$$ /$$   /$$ /$$$$$$ /$$$$$$$$
# |_  $$_/| $$$ | $$|_  $$_/|__  $$__/
#   | $$  | $$$$| $$  | $$     | $$   
#   | $$  | $$ $$ $$  | $$     | $$   
#   | $$  | $$  $$$$  | $$     | $$   
#   | $$  | $$\  $$$  | $$     | $$   
#  /$$$$$$| $$ \  $$ /$$$$$$   | $$   
# |______/|__/  \__/|______/   |__/
  
if __name__ == '__main__':
  game_initialize()
  game_main_loop()