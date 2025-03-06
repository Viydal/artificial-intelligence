from collections import deque

STUDENT_ID = 'a1885080'
DEGREE = 'UG'

# grid = [
#     [1, 1, 1, 1, 1, 1, 4, 7, 8, "X"],
#     [1, 1, 1, 1, 1, 1, 1, 5, 8, 8],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
#     [1, 1, 1, 1, 1, "X", 1, 1, 1, 6],
#     [1, 1, 1, 1, 1, "X", 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [6, 1, 1, 1, 1, "X", 1, 1, 1, 1],
#     [7, 7, 1, "X", "X", "X", 1, 1, 1, 1],
#     [8, 8, 1, 1, 1, 1, 1, 1, 1, 1],
#     ["X", 8, 7, 1, 1, 1, 1, 1, 1, 1]
# ]

mapFile = open("map.txt", "r")
print(mapFile.read())

startX = 0
startY = 0

endX = 9
endY = 9

visited = set()

def BFSTraversal(currentX, currentY, cost):
    
    # ADD PATH
    queue = deque([(startX, startY, 0, [(startX, startY)])])
    
    visited.add((startX, startY))
    
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    while queue:
        currentX, currentY, cost, path = queue.popleft()
        
        if currentX == endX and currentY == endY:
            return cost + grid[currentX][currentY], path
        
        for dx, dy in directions:
            newX = currentX + dx
            newY = currentY + dy
            
            # print(newX, newY)
            
            if (newX >= 0 and newX < len(grid)) and (newY >= 0 and newY < len(grid[0])) and (newX, newY) not in visited:
                
                if grid[newX][newY] != "X":
                    visited.add((newX, newY))
                    
                    newPath = path + [(newX, newY)]
                    
                    queue.append((newX, newY, cost + grid[currentX][currentY], newPath))  
                    
    return 999999

path = BFSTraversal(startX, startY, 0)         

print(path[1])  

for i, j in path[1]:
    grid[i][j] = "*"
    
for i in range(len(grid)):
    print(grid[i])    