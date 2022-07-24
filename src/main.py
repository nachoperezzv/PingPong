import os 
import sys
import pygame 

from player import Player
from ball   import Ball 


class Game:
	def __init__(self):
		pygame.init()
		
		self.screen = pygame.display.set_mode((600,600))
		self.game = True

		self.player1 = Player(self.screen,left=0,top=195,width=10,height=30)
		self.player2 = Player(self.screen,left=390,top=195,width=10,height=30)

		self.ball = Ball(self.screen,(300,300))

	def run(self):

		self.screen.fill([20,20,20])

		while self.game:	

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game = False
					

			self.player1.update()
			self.player1.draw()

			self.player2.update()
			self.player2.draw()

			self.ball.update((300,300))
			self.ball.draw()

			pygame.display.flip()

		self.close()

	def close(self):
		pygame.quit()
		sys.exit()


if __name__ == '__main__':
	game = Game()
	game.run()


	