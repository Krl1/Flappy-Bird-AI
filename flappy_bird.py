import pygame
from pygame.sprite import Group
import sys

from settings import Settings
from bird import Bird
from pipe import Pipe
import game_functions as gf

def run_game():
	#Inicjalizacja Pygame, ustawień i obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Flappy bird")
	
	

	# Utworzenie ptaka
	bird = Bird(ai_settings, screen)
	pipes = Group()
	#pipe = Pipe(ai_settings, screen)

	# Zdefiniowania koloru tła.
	bg_color = (152, 218, 255)

	#Rozpoczęcie pętli głównej gry
	while True:
		gf.check_events(ai_settings, screen, bird)		
		gf.check_pipes(ai_settings, screen, pipes)
		bird.update()
		pipes.update()
		gf.update_screen(ai_settings, screen, bird, pipes)

		

run_game()