import pygame

class Player():
	def __init__(self,screen, left=0,top=0,width=10,height=30):

		self.screen = screen
		self.rect = pygame.Rect(left,top,width,height)


	def update(self):
		pass

	def draw(self):
		pass