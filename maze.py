import numpy as np

class maze:

	def __init__(self, dimensions, obstacles):

		self.obstacles = obstacles
		self.dimensions = np.array(dimensions)
		self.maze = np.zeros(self.dimensions)

	def populateMaze(self):
		for value in self.obstacles:
			for i in range(value[2]):
				for j in range(value[3]):
					try:
                                            self.maze[value[1] + j][value[0] + i] = 1
					except:
						print('Warning: Some obstacles out of Maze Boundaries, not included.')
    	