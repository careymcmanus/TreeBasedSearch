import numpy as np

class maze:

	def __init__(self, dimensions, obstacles):

		self.obstacles = obstacles
		self.dimensions = np.array(dimensions)
		self.maze = np.zeros(dimensions)

	def populateMaze(self):
		for value in self.obstacles:
			for i in range(value[2]):
				for j in range(value[3]):
					if ((value[1] + j < self.dimensions[0]) & (value[2] + i < self.dimensions[1])):
						self.maze[value[1] + j][value[0] + i] = 1
					else:
						print('Warning: Some obstacles out of Maze Boundaries, not included.')
    	