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

def game_main_loop():
  game_quit = False
  
  while not game_quit:
    #TODO collect input
    
    #TODO process input
    
    #TODO draw
    
  #TODO quit

def game_initialize():
  global SURFACE_MAIN
  
  pygame.init()

  SURFACE_MAIN = pygame.display.set_mode( (800, 600) )