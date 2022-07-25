import os 
import sys
import pygame 

class Block(pygame.sprite.Sprite):
	def __init__(self,path,init_pos):
		super().__init__()
		self.image = pygame.image.load(path).convert_alpha()
		self.rect = self.image.get_rect(center=init_pos)


class Player(Block):
	def __init__(self,path,init_pos):
		super().__init__(path,init_pos)

class Opponent(Block):
	def __init_(sef,path,init_pos):
		super().__init(path,init_pos)

class Ball(Block):
	def __init__(self,path,init_pos,blocks_group):
		super().__init__(path,init_pos)

class Game:
	def __init__(self):
		# Init
		pygame.init()
		pygame.display.set_caption("Ping Pong")

		# Screen
		self._width = 600
		self._height = 350
		self.screen = pygame.display.set_mode((self._width, self._height))
		
		# Clock
		self.clock = pygame.time.Clock()

		# Groups 
		self.blocks_group = pygame.sprite.Group()
		self.ball_group = pygame.sprite.GroupSingle()

		# Objects
		self.player = Player(
			path = '../include/icons/paddle.png',
			init_pos = (0,self._height/2)
			)
		self.blocks_group.add(self.player)

		self.opponent = Opponent(
			path = '../include/icons/paddle.png',
			init_pos = (self._width-10,self._height/2)
			)
		self.blocks_group.add(self.opponent)

		self.ball = Ball(
			path = '../include/icons/ball.png',
			init_pos = (self._width/2,self._height/2),
			blocks_group = self.blocks_group
			)		
		self.ball_group.add(self.ball)

		# Score
		self.score_player	= 0
		self.score_opponent = 0

	def run(self):
		exit = False
		game_active = False

		while not exit:	
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					exit = True

			keys = pygame.key.get_pressed()		

			if keys[pygame.K_SPACE]:
				game_active = True
			
			if keys[pygame.K_ESCAPE]:
				game_active = False
			
			if keys[pygame.K_UP]:
				self.player.movement = -1

			if keys[pygame.K_DOWN]:
				self.player.movement = 1
						
			if keys[pygame.K_UP]==False and keys[pygame.K_DOWN]==False:
				self.player.movement = 0
			
			if game_active:
				self.display_score()

				self.blocks_group.draw(self.screen)
				self.ball_group.draw(self.screen)

				self.blocks_group.update(self.ball_group)
				self.ball_group.update()
			else:
				self.display_init()

			pygame.display.flip()
			self.clock.tick(60)

	def exit(self):
		pygame.quit()
		sys.exit()

	def display_init(self):
		self.screen.fill([20,20,20])

		mask = self.screen.convert_alpha()
		mask.fill([75,75,75,150])
		mask_rect = mask.get_rect(center=(self._width/2,self._height/2))

		self.screen.blit(mask,mask_rect)

		init = pygame.font.Font(None,36).render("Pulsa ENTER para comenzar", True, 'white')
		init_rect = init.get_rect(center=(self._width/2,self._height/2))

		self.screen.blit(init,init_rect)

	def display_score(self):
		self.screen.fill([20,20,20])


		pygame.draw.line(
			surface = self.screen,
			color = 'white',
			start_pos = (self._width/2,0),
			end_pos = (self._width/2,self._height),
			width = 3
			)

		score1 = pygame.font.Font(None,16).render(f'{self.score_player}', True, 'white')
		score2 = pygame.font.Font(None,16).render(f'{self.score_opponent}', True, 'white')

		score1_rect = score1.get_rect(center=(self._width/2-10,self._height/2))
		score2_rect = score2.get_rect(center=(self._width/2+10,self._height/2))

		self.screen.blit(score1,score1_rect)
		self.screen.blit(score2,score2_rect)

		mask = self.screen.convert_alpha()
		mask_rect = mask.get_rect(center=(self._width/2,self._height/2))
		mask.fill([75,75,75,150])
		
		self.screen.blit(mask,mask_rect)
	