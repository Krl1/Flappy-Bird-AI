import pygame

class Bird():

	def __init__(self, screen):
		"""Inicjalizacja skaczącego ptaka i jego położenie początkowe."""
		self.screen = screen

		# Wczytanie obrazu statu kosmicznego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/bird.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		self.rect.centerx = self.screen_rect.centerx/3
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		"""Wyświetlenie ptaka w jego początkowym położeniu."""
		self.screen.blit(self.image, self.rect)

		 