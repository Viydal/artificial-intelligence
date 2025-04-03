STUDENT_ID = 'a1885080'
DEGREE = 'UG'

from collections import deque
import heapq
from sys import argv
import numpy as np

if __name__ == "__main__":

    # Defining inputs
    mode = argv[1]
    mapPath = argv[2]
    algorithm = argv[3]
    if (algorithm == "astar"):
        heuristic = argv[4]

    # Extracting map file
    mapFile = open(mapPath, "r")
    boardSize = next(mapFile).strip().split()
    startCoords = next(mapFile).strip().split()
    endCoords = next(mapFile).strip().split()

    grid = []

    for line in mapFile:
        row = line.strip().split()
        grid.append(row)
        
    # Defining map information
    boardX = int(boardSize[0])
    boardY = int(boardSize[1])

    startX = int(startCoords[0]) - 1
    startY = int(startCoords[1]) - 1

    endX = int(endCoords[0]) - 1
    endY = int(endCoords[1]) - 1
    
    gridVisit = np.zeros([boardX, boardY], dtype=int)

    if (algorithm == "bfs"):
        visited = set()
        
        def BFSTraversal(currentX, currentY):
            queue = deque([(startX, startY, [(startX, startY)])])
            visited.add((startX, startY))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                currentX, currentY, path = queue.popleft()
                
                gridVisit[currentX, currentY] += 1
                
                if currentX == endX and currentY == endY:
                    return path
                
                for dx, dy in directions:
                    newX = currentX + dx
                    newY = currentY + dy
                    
                    if (newX >= 0 and newX < boardX) and (newY >= 0 and newY < boardY) and (newX, newY) not in visited:
                        
                        if grid[newX][newY] != 'X':
                            
                            newPath = path + [(newX, newY)]
                            queue.append((newX, newY, newPath))  
                     
                visited.add((currentX, currentY))        
            return None
        
        path = BFSTraversal(startX, startY)  
        
    if (algorithm == "ucs"):    
        visited = set()
            
        def UCSTraversal(currentX, currentY):
            queue = []
            
            heapq.heappush(queue, (0, startX, startY, [(startX, startY)]))
            
            print(queue[0])
            
            visited.add((startX, startY))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                cost, currentX, currentY, path = heapq.heappop(queue)
                print(path)
                
                gridVisit[currentX, currentY] += 1
                
                if currentX == endX and currentY == endY:
                    return path
                
                for dx, dy in directions:
                    newX = currentX + dx
                    newY = currentY + dy
                    
                    if (newX >= 0 and newX < boardX) and (newY >= 0 and newY < boardY) and (newX, newY) not in visited:
                        
                        if grid[newX][newY] != 'X':
                            
                            newPath = path + [(newX, newY)]
                            heapq.heappush(queue, (cost + int(grid[newX][newY]), newX, newY, newPath))  
                     
                visited.add((currentX, currentY))        
            return None
        
        path = UCSTraversal(startX, startY)

    if (algorithm == "astar"):
        b = 3
        
    if (mode == "release"):
        if (path == None):
            print('null')
        else:
            for i, j in path:
                grid[i][j] = "*"
            
            for i in range(boardX):
                for j in range(boardY):
                    print(grid[i][j], end=" ")    
                print()
            
    elif (mode == "debug"):
        print(gridVisit)