class Settings():
	"""Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

	def __init__(self):
		"""Inicjalizacja ustawień gry."""
		# Ustawienia ekranu.
		self.screen_width = 450
		self.screen_height = 700
		self.bg_color = (152, 218, 255)
		self.bird_speed_fall = .2
		self.bird_speed_fly = .5
		self.bird_jump = 500


		self.pressed_space = False