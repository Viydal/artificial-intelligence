STUDENT_ID = 'a1885080'
DEGREE = 'UG'

from collections import deque
from sys import argv

# Defining inputs
mode = argv[1]
map = argv[2]
algorithm = argv[3]
heuristic = argv[4]

# Extracting map file
mapFile = open(map, "r")
boardSize = next(mapFile).strip().split()
startCoords = next(mapFile).strip().split()
endCoords = next(mapFile).strip().split()

grid = []

for line in mapFile:
    row = line.strip().split()
    grid.append(row)

for line in grid:
    print(line)
    
# Defining map information
boardX = int(boardSize[0])
boardY = int(boardSize[1])

startX = int(startCoords[0]) - 1
startY = int(startCoords[1]) - 1

endX = int(endCoords[0]) - 1
endY = int(endCoords[1]) - 1

visited = set()

if (algorithm == "bfs"):
    def BFSTraversal(currentX, currentY, cost):
        
        # ADD PATH
        queue = deque([(startX, startY, 0, [(startX, startY)])])
        
        visited.add((startX, startY))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            currentX, currentY, cost, path = queue.popleft()
            
            if currentX == endX and currentY == endY:
                return cost + int(grid[currentX][currentY]), path
            
            for dx, dy in directions:
                newX = currentX + dx
                newY = currentY + dy
                
                # print(newX, newY)
                
                if (newX >= 0 and newX < boardX) and (newY >= 0 and newY < boardY) and (newX, newY) not in visited:
                    
                    if grid[newX][newY] != 'X':
                        visited.add((newX, newY))
                        
                        newPath = path + [(newX, newY)]
                        
                        queue.append((newX, newY, cost + int(grid[currentX][currentY]), newPath))  
                        
        return 999999
    
    path = BFSTraversal(startX, startY, 0)  

       
if (path == 999999):
    print("null")
else: 
    print(path[1])
    
    for i, j in path[1]:
        grid[i][j] = "*"
    
    for i in range(boardX):
        for j in range(boardY):
            print(grid[i][j], end=" ")    
        print()


    


            