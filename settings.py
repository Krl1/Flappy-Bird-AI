import pygame

class Settings():
	"""Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

	def __init__(self):
		"""Inicjalizacja ustawień gry."""
		# Ustawienia ekranu.
		self.screen_width = 300
		self.screen_height = 500
		self.bg_color = (152, 218, 255)
		self.bird_speed_fall = .35
		self.bird_speed_fly = .4
		self.bird_jump = 100
		self.pipe_speed = .2
		self.pipe_color = (0,255,0)
		self.pipes_space = 120
		self.pipe_width = 80
		self.pipe_hole = 100


		self.pressed_space = False

		self.background_image = pygame.image.load("images/background.bmp")