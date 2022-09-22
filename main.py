import pygame
import setup as s

from pygame.locals import *

run = True

#display
display = pygame.display.set_mode(s.SCREEN)
pygame.display.set_caption('RPG TEST')



while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			run = False