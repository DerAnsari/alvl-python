# grid = [[ 1 for i in range(5)] for index in range(5)]
# start = (0,0)
# end = (4,4)

# class Node:
#     def __init__ (self,position,parent = None):
#         self.position = position
#         self.g = 0
#         self.h = 0
#         self.f = 0
#         self.parent = parent

# def manhattanDistance(x,y):
#     return abs(x[0] - y[0]) + abs(x[1] - y[1])

# def aStar(grid, start, end):

#     openList = []
#     closedList = []
#     startNode = Node(start)
#     goalNode = Node(end)
#     openList.append(startNode)

#     while openList:

#         currentNode = min(openList, key=lambda Node: Node.f)
#         openList.remove(currentNode)
#         closedList.append(currentNode)

# #*  Check if successfully reached destination 
#         if currentNode.position == goalNode.position:
#             path = []
#             while currentNode:
#                 path.append(currentNode.position)
#                 currentNode = currentNode.parent

#             return path[:: -1]

# #*find the neighbors of the current node 
#     neighbors = []

#     for index, i in [ (0,-1), (0,1), (-1,0), (1,0)]:
#         nodePosition = (currentNode.position[0] + index , currentNode.position[1] + i)

#         if 0 <= nodePosition[0] < len(grid) and 0 <= nodePosition[1] < len(grid[0]) and grid[nodePosition[0]][nodePosition[1]] == 0:
#             neighbors.append(Node(nodePosition, currentNode))
    
#     for neighbor in neighbors:
#         if any(node.position == neighbor.position for node in closedList):
#             continue
        
#         tentative_g = currentNode.g + 1
#         neighbor.h = manhattanDistance(neighbor.position, goalNode.position)
#         neighbor.f = tentative_g + neighbor.h

#         existingNode = next((node for node in openList if node.position == neighbor.position), None)
#         if existingNode:
#             if tentative_g < existingNode.g:
#                 existingNode.g = tentative_g
#                 existingNode.f = tentative_g + existingNode.h
#                 existingNode.parent = currentNode
#         else:
#             neighbor.g = tentative_g
#             openList.append(neighbor)
    
#     return None

# def printGrid(grid):
#     for row in grid:
#         print(" ".join(str(cell) for cell in row))

# Passage = aStar(grid,start,end)
# print("your maze grid")
# printGrid(grid)
# print("the path: " , Passage)



grid = [[0 for i in range(5)] for index in range(5)]
start = (0,0)
end = (4,4)

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent

def manhattanDistance(x,y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def aStar(grid, start, end):
    openList = []
    closedList = []
    startNode = Node(start)
    goalNode = Node(end)
    openList.append(startNode)

    while openList:
        currentNode = min(openList, key=lambda Node: Node.f)
        openList.remove(currentNode)
        closedList.append(currentNode)

        if currentNode.position == goalNode.position:
            path = []
            while currentNode:
                path.append(currentNode.position)
                currentNode = currentNode.parent
            return path[::-1]

        neighbors = []
        for index, i in [(0,-1), (0,1), (-1,0), (1,0)]:
            nodePosition = (currentNode.position[0] + index, currentNode.position[1] + i)
            if 0 <= nodePosition[0] < len(grid) and 0 <= nodePosition[1] < len(grid[0]) and grid[nodePosition[0]][nodePosition[1]] == 0:
                neighbors.append(Node(nodePosition, currentNode))

        for neighbor in neighbors:
            if any(node.position == neighbor.position for node in closedList):
                continue

            # Set g, h, and f values for the neighbor
            neighbor.g = currentNode.g + 1
            neighbor.h = manhattanDistance(neighbor.position, goalNode.position)
            neighbor.f = neighbor.g + neighbor.h

            existingNode = next((node for node in openList if node.position == neighbor.position), None)
            if existingNode:
                if neighbor.g < existingNode.g:
                    existingNode.g = neighbor.g
                    existingNode.f = neighbor.g + existingNode.h
                    existingNode.parent = currentNode
            else:
                openList.append(neighbor)

    return None

def printGrid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Add a wall to test pathfinding
grid[2][2] = 1  # Add a wall in the middle
print("Grid with wall:")
printGrid(grid)

path = aStar(grid, start, end)
print("\nThe path: ", path)