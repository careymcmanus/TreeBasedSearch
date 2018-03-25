from enum import Enum
import numpy as np
import math 

class directions(Enum):
    LEFT = -1
    RIGHT = 1
    UP = 0
    DOWN = 2
    START = 3
    FINISH = 4

class PuzzleState:
    
    def __init__(self, location, parentState=None, direction=3, cost=0):
        
        self.location = location
        self.parentState = parentState
        self.direction = directions(direction)
        self.neighbours = []
        self.cost = cost
        self.heuristic = 0
    
    def populateNeighbours(self, maze, state):
        neighbours = []
        directionsFrom = []
        ylim, xlim = maze.maze.shape
        for i in range(-1,2,2):
            xIndex = state[0] + i
            yIndex = state[1]
        
            if (xIndex < xlim) & (xIndex >= 0)  & (yIndex < ylim) & (yIndex >= 0):
                if (maze.maze[yIndex][xIndex] == 0):        
                    neighbours.append([xIndex, yIndex])
                    directionsFrom.append(directions(i))
                
            xIndex = state[0]
            yIndex = state[1] + i
        
            if (xIndex < xlim) & (xIndex >= 0)  & (yIndex < ylim) & (yIndex >= 0):
                if (maze.maze[yIndex][xIndex] == 0):
                    neighbours.append([xIndex, yIndex])
                    directionsFrom.append(directions(i+1))
                
        return neighbours, directionsFrom
        
    def findChildren(self, puzzle, goalState=None):
        
        nlist, dlist = self.populateNeighbours(puzzle,  self.location)
        for i in range(len(nlist)):
            if (dlist[i] == directions(0)):
                self.neighbours.append(PuzzleState(nlist[i], parentState=self , direction=dlist[i], cost=(self.cost+1)))
            else:
                self.neighbours.append(PuzzleState(nlist[i], parentState=self , direction=dlist[i], cost=(self.cost+1)))

        if not goalState == None:
            for member in self.neighbours:
                member.setHeuristic(goalState)
        

    def setHeuristic(self, goalState, startState=None):
        xDist = math.fabs(self.location[0] - goalState[0])
        yDist = math.fabs(self.location[1] - goalState[1])
        
        self.heuristic = xDist + yDist
      


    def getPathToState(self):
        result = []
       
        if (self.parentState == None):
            result.append(self)
            
        else:
            pathToParent = self.parentState.getPathToState()
            for i in range(len(pathToParent)):
                result.append(pathToParent[i])
                
            result.append(self)
        return result    