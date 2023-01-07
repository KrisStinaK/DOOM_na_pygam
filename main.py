from Menu import *
import pygame

a = Menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    a.run()