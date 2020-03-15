import sys
import pygame
import numpy as np
from pipeTop import PipeTop
from pipeDown import PipeDown

def check_events(ai_settings, screen, bird):
	"""Reakcja na zdarzenia generowane przez klawiaturę"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(ai_settings, event, bird)
			elif event.type == pygame.KEYUP:
				check_keyup_events(ai_settings, event, bird)


def check_keydown_events(ai_settings, event, bird):
	"""Reakcja na naciśnięcie klawisza."""
	if event.key == pygame.K_SPACE:
		if not ai_settings.pressed_space:
			bird.steps_to_move_to_top += ai_settings.bird_jump
			ai_settings.pressed_space = True

def check_keyup_events(ai_settings, event, bird):
	"""Reakcja na zwolnienie klawisza."""
	if event.key == pygame.K_SPACE:
		ai_settings.pressed_space = False

def update_screen(ai_settings, screen, bird, pipesTop, pipesDown):
	"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
	# Odświeżenie ekranu w trakcie każdej iteracji pętli.
	# screen.fill(ai_settings.bg_color)
	screen.blit(ai_settings.background_image, [0, 0])
	bird.blitme()
	for pipe in pipesTop.sprites():
		pipe.blitme()

	for pipe in pipesDown.sprites():
		pipe.blitme()

	# Wyświetlenie ostatio zmodyfikowanego ekranu.
	pygame.display.flip()

def check_pipes(ai_settings, screen, pipesTop, pipesDown):
	check_new_pipe = True
	for pipe in pipesTop.copy():
		if pipe.rect.right <= 0:
			pipesTop.remove(pipe)
		elif pipe.rect.right > ai_settings.screen_width:
			check_new_pipe = False


	for pipe in pipesDown.copy():
		if pipe.rect.right <= 0:
			pipesDown.remove(pipe)

	if check_new_pipe:
		random_int =  np.random.randint(ai_settings.screen_height/3, 2*ai_settings.screen_height/3)
		new_pipe_top = PipeTop(ai_settings, screen, random_int)
		new_pipe_down = PipeDown(ai_settings, screen, random_int)
		pipesTop.add(new_pipe_top)
		pipesDown.add(new_pipe_down)


def check_collide(pipesDown,pipesTop,bird):
	for pipe in pipesTop:
		is_collided = pygame.sprite.collide_rect(pipe, bird)
		if is_collided>0:
			return False
			
	for pipe in pipesDown:
		is_collided = pygame.sprite.collide_rect(pipe, bird)
		if is_collided>0:
			return False

	return True
		 