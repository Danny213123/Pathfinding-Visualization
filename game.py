# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:20:20 2022

@author: danny
"""

if __name__ == "__main__":
    import make_grid as gm
import pygame

rows = 30
width = 600

Game = pygame.display.set_mode((1200, width))
pygame.display.set_caption("Game Test")

gm.main(Game, rows, width, True, "U_DFS")
