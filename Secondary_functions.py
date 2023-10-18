# This file is meant to contain necessary variables and classes
import pygame

pygame.init()

"""class Character():

    def __init__(self):
        super().__init__()
        self.x = 45
        self.y = 45
"""
class Canvas():

    def __init__(self):
        super().__init__()
        self.canvas1 = pygame.image.load('WhiteWolfLogo.png')
        self.canvas2 = pygame.image.load('BackgroundMenu.png')
        self.canvas3 = pygame.image.load('Beginning.png')


