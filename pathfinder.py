from collections import deque

STUDENT_ID = 'a1885080'
DEGREE = 'UG'

grid = [
    [1, 1, 1, 1, 1, 1, 4, 7, 8, "X"],
    [1, 1, 1, 1, 1, 1, 1, 5, 8, 8],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
    [1, 1, 1, 1, 1, "X", 1, 1, 1, 6],
    [1, 1, 1, 1, 1, "X", 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [6, 1, 1, 1, 1, "X", 1, 1, 1, 1],
    [7, 7, 1, "X", "X", "X", 1, 1, 1, 1],
    [8, 8, 1, 1, 1, 1, 1, 1, 1, 1],
    ["X", 8, 7, 1, 1, 1, 1, 1, 1, 1]
]

startX = 0
startY = 0

endX = 9
endY = 9

visited = set()

def BFSTraversal(currentX, currentY, cost):
    
    # ADD PATH
    queue = deque([(startX, startY, 0 [startX, startY])])
    
    visited.add((startX, startY))
    
    directions = [(-1, 0), (1, 0),(0, -1), (0, 1)]
    
    while queue:
        currentX, currentY, cost = queue.popleft()
        
        print(cost)
        
        if currentX == endX and currentY == endY:
            return cost + grid[currentX][currentY]
        
        for dx, dy in directions:
            newX = currentX + dx
            newY = currentY + dy
            
            # print(newX, newY)
            
            if (newX >= 0 and newX < len(grid)) and (newY >= 0 and newY < len(grid[0])) and (newX, newY) not in visited:
                
                if grid[newX][newY] != "X":
                    visited.add((newX, newY))
                    queue.append((newX, newY, cost + grid[currentX][currentY]))  
                    
    return 999999

cost = BFSTraversal(startX, startY, 0)         

print(cost)  