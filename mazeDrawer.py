import pygame
import numpy as np
import maze
from enum import Enum
import button

BLACK = (  0,   0,   0)
GREY = (65, 65, 65)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
GREEN2 = (100, 255, 100)
RED =   (255,   0,   0)
PURPLE = (200, 100, 0)


class guiDisplay:

	def __init__(self, maze, windowHeight=400, windowWidth=800):
		self.size = np.array([windowWidth, windowHeight])
		self.tile_height = self.size[1]/maze.dimensions[0]
		self.tile_width = self.size[0]/maze.dimensions[1]


		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption('Robot Navigation')
		self.clock = pygame.time.Clock()
	
	def drawMainMenu(self):
		self.clock.tick(10)
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				return True
		self.screen.fill(WHITE)
		bfsButton = button.Button([self.size[0]/2 - 75, 20], [150,50], "BFS")
		dfsButton = button.Button([self.size[0]/2 - 75, 120], [150,50], "DFS")
		bfsButton.drawButton(self.screen)
		dfsButton.drawButton(self.screen)
		
		pygame.display.flip()

	def drawMaze(self, maze):
		self.clock.tick(10)
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				return True

		self.screen.fill(WHITE)

		for i in range(maze.dimensions[0]):
			for j in range(maze.dimensions[1]):
				if (maze.maze[i][j] == 1.0):
					pygame.draw.rect(self.screen, BLACK, [j*self.tile_width, i*self.tile_height, self.tile_width, self.tile_height])
				elif (maze.maze[i][j] == 2.0):
					pygame.draw.rect(self.screen, GREEN, [j*self.tile_width, i*self.tile_height, self.tile_width, self.tile_height])
				elif (maze.maze[i][j] == 3.0):
					pygame.draw.rect(self.screen, PURPLE, [j*self.tile_width, i*self.tile_height, self.tile_width, self.tile_height])
				elif (maze.maze[i][j] == 4.0):
					pygame.draw.rect(self.screen, RED, [j*self.tile_width, i*self.tile_height, self.tile_width, self.tile_height])

		for i in range(maze.dimensions[1]):
			pygame.draw.line(self.screen, GREY, [i*self.tile_width, 0], [i*self.tile_width, self.size[1]], 3)

		for i in range(maze.dimensions[0]):
			pygame.draw.line(self.screen, GREY, [0,i*self.tile_height], [self.size[0],i*self.tile_height], 3)


		pygame.display.flip()

		return False

	def closeMaze(self):
		pygame.quit()