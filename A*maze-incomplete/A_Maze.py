import pygame
import math 
from queue import PriorityQueue

Width = 800
window = pygame.display.set_mode((Width, Width))
pygame.display.set_caption("A* Path finding Algorithm ")

RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
PURPLE = (128,0,128)
BLACK = (0,0,0)
WHITE = (255,255,255)
TEAL = (0,128,128)

class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * col
        self.y = col * row
        self.neighbour = []
        self.color = WHITE
        self.width = width 
        self.totalRows = totalRows

    def getPossition(self):
        return self.row, self.col
    def isCloses(self):
        return self.color == RED
    def isOpen (self):
        return self.color == GREEN
    def isBarier(self):
        return self.color == BLACK
    def isStart (self):
        return self.color == BLUE
    def isEnd (self):
        return self.color == PURPLE
    def reset (self):
        return self.color == WHITE 
    
    def makeCloses (self):
        self.color = RED
    def makeOpen (self):
        self.color = GREEN
    def makeBarier(self):
        self.color = BLACK
    def makeEnd (self):
        self.color = PURPLE
    def makePath (self):
        self.color = TEAL

    def Draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
    def updateNeighbours(self):
        pass
    def __lt__ (self, other):
        return False
        
def manhattanDistance(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def makeGrid(rows,width):
    grid = []
    gap = width // rows
    for index in range (rows):
        grid.append(rows)
        for i in range(rows):
            node = Node(index,i,gap,rows)
            grid[index].append(node)

    return grid