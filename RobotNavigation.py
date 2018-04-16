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

def getInput():
    print("Select a Strategy for solving problem: ")
    print("1: Breadth-First Search")
    print("2: Depth-First Search")
    print("3: Uniform Cost Search")
    print("4: Greedy Best First Search")
    print("5: A* Search")
    value = input("Select a Number: ")
    if (value == '1'):
        Solver = strategy.BFSStrategy(problem)
    elif (value == '2'):
        Solver = strategy.DFSStrategy(problem)
    elif (value == '3'):
        Solver = strategy.UCSStrategy(problem)
    elif (value == '4'):
        Solver = strategy.GBFStrategy(problem)
    elif (value == '5'):
        Solver = strategy.AStrategy(problem)
    else:
        print("Please choose a number between 1 and 5!")
        return None
    

    print("Do you want uniform Cost")
    value = input("y/n: ")
    if (value == 'y'):
        cost = [1,1,1,1]
    else:
        cost = [2,1,4,3]

    return Solver, cost


#Read the puzzle information from the text file.
gridSize, initialState, goalState, obstacles = readProblem()

#Create a problem object
problem = maze.maze(gridSize, obstacles)

#populate the maze array with the obstacles
problem.populateMaze()

Solver, cost = getInput()
while (Solver == None):
    Solver, cost = getInput()


#Create the start and end state giving them directions of start and end
startState = mazestate.PuzzleState(initialState, direction=3, dirCost=cost)
endState = mazestate.PuzzleState(goalState, direction=4)

display = draw.guiDisplay(problem)


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
             if (path == None):
                 print("There is no path to goal")
             else:
                 dlist = []
                 for member in path:
                     dlist.append(member.direction.name)
             
                 print(dlist)
                 print("Length of Path: " + str(path[-1].cost))
                 print("Number of Nodes Explored: " + str(Solver.score))
                               
             printedPath = True


display.closeMaze()
