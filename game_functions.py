import sys
import pygame

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
			print(bird.steps_to_move_to_top)

def check_keyup_events(ai_settings, event, bird):
	"""Reakcja na zwolnienie klawisza."""
	if event.key == pygame.K_SPACE:
		ai_settings.pressed_space = False

def update_screen(ai_settings, screen, bird):
	"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
	# Odświeżenie ekranu w trakcie każdej iteracji pętli.
	screen.fill(ai_settings.bg_color)
	bird.blitme()

	# Wyświetlenie ostatio zmodyfikowanego ekranu.
	pygame.display.flip()