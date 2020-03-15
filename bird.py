import pygame

class Bird():

	def __init__(self, ai_settings, screen):
		"""Inicjalizacja skaczącego ptaka i jego położenie początkowe."""
		self.screen = screen
		self.ai_settings = ai_settings

		# Wczytanie obrazu statu kosmicznego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/bird.bmp')

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect_angle = 0.0

		#Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		self.rect.centerx = self.screen_rect.centerx/2
		self.rect.centery = self.screen_rect.centery

		# Położenie ptaka jest zdefiniowane za pomocą wartości zmiennoprzecinkowej
		self.y = float(self.rect.y)

		self.speed_factor = ai_settings.bird_speed_fall

		# # Punkt środkowy ptaka jest przechowywany w postaci liczby zmiennoprzecinkowej
		# self.centery = float(self.rect.centery)

		# Opcja wskazująca na skok ptaka
		#self.moving_top = False
		self.steps_to_move_to_top = 0

	def blitme(self):
		"""Wyświetlenie ptaka w jego początkowym położeniu."""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Poruszanie ptakiem po ekranie."""
		# Uaktualnienie położenia ptaka
		#if self.moving_top or self.steps_to_move_to_top>0:
		if self.steps_to_move_to_top>0:
			if self.y > 0:
				self.y -= self.ai_settings.bird_speed_fly
			self.steps_to_move_to_top -= 1

		else:
			if self.rect.bottom < self.ai_settings.screen_height:
				self.y += self.ai_settings.bird_speed_fall

		# Uaktualnienie położenia obiektu ptak.
		self.rect.y = self.y
		

	def die(self):
		if self.rect.bottom < self.ai_settings.screen_height:
			self.y += self.ai_settings.bird_speed_fall_die
			self.rect.y = self.y
			return True
		else:
			return False
