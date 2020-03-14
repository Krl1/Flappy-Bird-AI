import pygame
import numpy as np
from pygame.sprite import Sprite

class Pipe(Sprite):

	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.left = ai_settings.screen_width + ai_settings.pipes_space
		self.top = np.random.randint(ai_settings.screen_height/3, 2*ai_settings.screen_height/3)

		self.imageDown = pygame.image.load('images/pipeDown.bmp')
		self.imageTop = pygame.image.load('images/pipeTop.bmp')
		self.rectDown = self.imageDown.get_rect()
		self.rectTop = self.imageTop.get_rect()

		self.rectDown.left = self.left
		self.rectTop.left = self.left

		self.rectDown.top = self.top
		self.rectTop.bottom = self.top - ai_settings.pipe_hole

		# self.rectDown = pygame.Rect(self.left, self.top, ai_settings.pipe_width, ai_settings.screen_height)
		# self.rectTop = pygame.Rect(self.left, self.top - ai_settings.pipe_hole, ai_settings.pipe_width, -ai_settings.screen_height )
		self.screen_rect = screen.get_rect()

		self.x = float(self.rectDown.x)
		self.color = ai_settings.pipe_color

	def blitme(self):
		"""Wyświetlenie ptaka w jego początkowym położeniu."""
		self.screen.blit(self.imageDown, self.rectDown)
		self.screen.blit(self.imageTop, self.rectTop)

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rectDown)
		pygame.draw.rect(self.screen, self.color, self.rectTop)

	def update(self):
		self.x -= self.ai_settings.pipe_speed
		self.rectDown.x = self.x
		self.rectTop.x = self.x
		 