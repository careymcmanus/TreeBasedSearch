import maze 
import mazestate 
import strategy 
import mazeDrawer as draw


def readProblem():
    with open('maze.txt', 'r') as file:
        lines = file.readlines()

        rows, cols = (int(val) for val in lines[0].split(','))
        xi, yi = (int(val) for val in lines[1].split(','))
        xg, yg = (int(val) for val in lines[2].split(','))
        
        gridSize = [rows, cols]
        initialState = [xi, yi]
        goalState = [xg,yg]
    
        obstacles = []
        for i in range(3, len(lines)):
            obst = [0,0,0,0]
            obst[0], obst[1], obst[2], obst[3] = (int(val) for val in lines[i].split(','))
            obstacles.append(obst)
    return gridSize, initialState, goalState, obstacles


#Read the puzzle information from the text file.
gridSize, initialState, goalState, obstacles = readProblem()

#Create a problem object
problem = maze.maze(gridSize, obstacles)

#populate the maze array with the obstacles
problem.populateMaze()


#Create the start and end state giving them directions of start and end
startState = mazestate.PuzzleState(initialState, direction=3)
endState = mazestate.PuzzleState(goalState, direction=4)




display = draw.guiDisplay(problem)


#Create the Puzzle Solver Object
Solver = strategy.DFSStrategy(problem)

Solver.addDrawObject(display)
print(problem.maze)
done = False
gotPath = False
printedPath = False
while not done:
	
	while not gotPath:
		path, gotPath = Solver.solve(startState, endState)
	done = Solver.drawMaze()
	if not printedPath:
             dlist = []
             for member in path:
                 dlist.append(member.direction.name)
             
             print(dlist)
             print("Length of Path: " + str(path[-1].cost))
             print("Number of Nodes Explored: " + str(Solver.score))
              
             printedPath = True


display.closeMaze()
