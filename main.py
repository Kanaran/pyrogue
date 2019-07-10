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

def draw_game():
  global SURFACE_MAIN
  
  # clear the surface
  SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)
  
  #TODO draw the map
  
  #TODO draw the character
  SURFACE_MAIN.blit(constants.S_PLAYER, ( 100, 100 ))
  
  # update the display
  pygame.display.flip()
  

def game_main_loop():
  game_quit = False
  
  while not game_quit:
    # collect input
    events_list = pygame.event.get()
    
    # process input
    for event in events_list:
      if event.type == pygame.QUIT:
        game_quit = True
    
    #TODO draw
    draw_game()
    
  # quit
  pygame.quit()
  exit()

def game_initialize():
  global SURFACE_MAIN
  
  pygame.init()

  SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )
  
if __name__ == '__main__':
  game_initialize()
  game_main_loop()