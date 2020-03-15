import pygame
import numpy as np
from pygame.sprite import Sprite

class PipeDown(Sprite):

	def __init__(self, ai_settings, screen, random_int):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.left = ai_settings.screen_width + ai_settings.pipes_space
		self.top = random_int

		self.image = pygame.image.load('images/pipeDown.bmp')
		self.rect = self.image.get_rect()
		self.rect.left = self.left
		self.rect.top = self.top
		self.screen_rect = screen.get_rect()

		self.x = float(self.rect.x)
		self.color = ai_settings.pipe_color

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update(self, bird):
		self.x -= self.ai_settings.pipe_speed
		self.rect.x = self.x

		 