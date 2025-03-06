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


def traverse(currentX, currentY, cost):

    # Check bounds

    if currentX < 0 or currentX >= len(grid):
        return 99999999
    elif currentY < 0 or currentY >= len(grid[0]):
        return 99999999

    if grid[currentX][currentY] == "X":
        return 99999999

    # No duplicate pathing

    if (currentX, currentY) in visited:
        return 99999999


    if currentX == endX and currentY == endY:
        return cost + grid[currentX][currentY]

    visited.add((currentX, currentY))

    # Split the location into four new directions, keeping track of locations that have already been visited

    print("decision tree")
    
    # Up
    upCost = traverse(currentX, currentY + 1, cost + grid[currentX][currentY])

    # Down
    downCost = traverse(currentX, currentY - 1, cost + grid[currentX][currentY])

    # Left
    leftCost = traverse(currentX - 1, currentY, cost + grid[currentX][currentY])

    # Right
    rightCost = traverse(currentX + 1, currentY, cost + grid[currentX][currentY])
    
    visited.remove((currentX, currentY))
    
    return min(upCost, downCost, leftCost, rightCost)

cost = traverse(startX, startY, 0)

print(cost)