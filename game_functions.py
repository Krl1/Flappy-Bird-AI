import sys
import pygame
from pipe import Pipe

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

def update_screen(ai_settings, screen, bird, pipes):
	"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
	# Odświeżenie ekranu w trakcie każdej iteracji pętli.
	# screen.fill(ai_settings.bg_color)
	screen.blit(ai_settings.background_image, [0, 0])
	bird.blitme()
	for pipe in pipes.sprites():
		pipe.blitme()

	# Wyświetlenie ostatio zmodyfikowanego ekranu.
	pygame.display.flip()

def check_pipes(ai_settings, screen, pipes):
	check_new_pipe = True
	for pipe in pipes.copy():
		if pipe.rectTop.right <= 0:
			pipes.remove(pipe)
		elif pipe.rectTop.right > ai_settings.screen_width:
			check_new_pipe = False

	if check_new_pipe:
		new_pipe = Pipe(ai_settings, screen)
		pipes.add(new_pipe)
