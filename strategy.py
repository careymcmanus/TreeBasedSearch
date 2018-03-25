import mazeDrawer as draw

""" The strategy class is the super class for the different 
strategies for solving the maze problem. The super class defines 
all the functions except for the getNextState function which is 
defined by the subclass """

class Strategy():

    def __init__(self, puzzle):
        self.Frontier = []
        self.Searched = []
        self.puzzle = puzzle
        self.score = 0

    def getNextState(self):
        return None

    def addToFrontier(self, puzzleState):
        if (puzzleState in self.Searched) | (puzzleState in self.Frontier):
            return False
        else:
            self.Frontier.append(puzzleState)
            self.puzzle.maze[puzzleState.location[1]][puzzleState.location[0]]=2
            return True
    
    def showPath(self, path):
            for member in path:
                self.puzzle.maze[member.location[1]][member.location[0]]=4
                self.drawMaze()
    
    def drawMaze(self):
        quit = self.drawObject.drawMaze(self.puzzle)
        return quit
    
    def solve(self, startState, endState):
        
        self.addToFrontier(startState)
        gotPath = False
        while (len(self.Frontier) > 0):
            thisState = self.getNextState()    
            if (thisState.location == endState.location):
                path = thisState.getPathToState()
                self.showPath(path)
                gotPath = True
                return path, gotPath
            else:
                thisState.findChildren(self.puzzle, endState.location)
                for state in thisState.neighbours:
                    self.addToFrontier(state)
                    self.drawMaze()
        
        #No Solution Found and we've run out of nodes to search
        return None, gotPath

    def addDrawObject(self, drawObject):
        self.drawObject = drawObject

class BFSStrategy(Strategy):

    def __init__(self, puzzle):
        super().__init__(puzzle)
        self.code = "BFS"
        self.longName = "Breadth-First-Strategy"
    
    def getNextState(self):
        thisState = self.Frontier.pop(0) #Removes the value at the start of the list
        self.Searched.append(thisState)
        self.puzzle.maze[thisState.location[1]][thisState.location[0]]=3
        self.score = self.score + 1
        return thisState

class DFSStrategy(Strategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)
        self.code = "DFS"
        self.longName = "Depth-First-Strategy"

    def getNextState(self):
        thisState = self.Frontier.pop() #Removes the value at the start of the list
        self.Searched.append(thisState)
        self.puzzle.maze[thisState.location[1]][thisState.location[0]]=3
        return thisState

class UCSStrategy(Strategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)
        self.code = "UCS"
        self.longName = "Uniform-Cost-Search"

    def getNextState(self):
        thisState = min(self.Frontier, key=lambda x: x.cost)
        self.Frontier.remove(thisState)
        self.Searched.append(thisState)
        self.puzzle.maze[thisState.location[1]][thisState.location[0]]=3
        self.score = self.score + 1
        return thisState

class GBFStrategy(Strategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)
        self.code = "GBF"
        self.longName = "Greedy-Best-First"

    def getNextState(self):
        thisState = min(self.Frontier, key=lambda x: x.heuristic)
        self.Frontier.remove(thisState)
        self.Searched.append(thisState)
        self.puzzle.maze[thisState.location[1]][thisState.location[0]]=3
        self.score = self.score + 1
        return thisState

class AStrategy(Strategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)
        self.code = "AST"
        self.longName ="A* Strategy"

    def getNextState(self):
        thisState = min(self.Frontier, key=lambda x: x.heuristic + x.cost)
        self.Frontier.remove(thisState)
        self.Searched.append(thisState)
        self.puzzle.maze[thisState.location[1]][thisState.location[0]]=3
        self.score = self.score + 1
        return thisState

    