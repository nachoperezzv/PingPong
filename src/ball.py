import pygame

class Ball():
	def __init__(self, screen, pos=(0,0), radius=10, width=0, color='white'):

		self.screen = screen
		self.color  = color
		self.center = pos
		self.radius = radius
		self.width  = width

	def update(self,pos):
		self.center = pos

	def draw(self):
		pygame.draw.circle(
			self.screen,
			self.color,
			self.center,
			self.radius,
			self.width
			)
