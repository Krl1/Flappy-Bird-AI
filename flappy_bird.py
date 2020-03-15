import pygame
from pygame.sprite import Group
import sys

from settings import Settings
from bird import Bird
from pipeTop import PipeTop
from pipeDown import PipeDown
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Flappy bird")
	
	
	bird = Bird(ai_settings, screen)
	pipesTop = Group()
	pipesDown = Group()

	running = True

	while running:
		gf.check_events(ai_settings, screen, bird)		
		gf.check_pipes(ai_settings, screen, pipesTop, pipesDown)
		bird.update()
		pipesTop.update(bird)
		pipesDown.update(bird)
		
		running = gf.check_collide(pipesDown,pipesTop,bird)

		gf.update_screen(ai_settings, screen, bird, pipesTop, pipesDown)

		
	bird_fall = True
	while bird_fall:
		bird_fall = bird.die()
		gf.update_screen(ai_settings, screen, bird, pipesTop, pipesDown)


run_game()