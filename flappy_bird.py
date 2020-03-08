import pygame
import sys

from settings import Settings
from bird import Bird
import game_functions as gf

def run_game():
	#Inicjalizacja Pygame, ustawień i obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Flappy bird")

	# Utworzenie ptaka
	bird = Bird(screen)

	# Zdefiniowania koloru tła.
	bg_color = (152, 218, 255)

	#Rozpoczęcie pętli głównej gry
	while True:
		gf.check_events()		
		gf.update_screen(ai_settings, screen, bird)
		

run_game()