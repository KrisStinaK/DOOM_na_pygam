from menu import *
import pygame
import os

print(os.getcwd())
a = Menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    a.run()
