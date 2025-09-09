import random
import pygame
import time
import heapq

# Parameters for the maze
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 50
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Maze Solver")

class Node:
    def __init__(self, x, y, g_cost=0, h_cost=0):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = None

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def get_valid_neighbors(maze, x, y):
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and 
            maze[new_y][new_x] == 0):
            neighbors.append((new_x, new_y))
    return neighbors

def a_star(maze, start, goal):
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    open_list = []
    closed_set = set()
    
    heapq.heappush(open_list, start_node)
    node_dict = {(start[0], start[1]): start_node}
    
    while open_list:
        current = heapq.heappop(open_list)
        
        if (current.x, current.y) == (goal_node.x, goal_node.y):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            print("Path found:", path[::-1])  # Debug print
            return path[::-1]
        
        closed_set.add((current.x, current.y))
        
        for next_x, next_y in get_valid_neighbors(maze, current.x, current.y):
            if (next_x, next_y) in closed_set:
                continue
                
            g_cost = current.g_cost + 1
            h_cost = manhattan_distance((next_x, next_y), (goal_node.x, goal_node.y))
            
            if (next_x, next_y) not in node_dict:
                neighbor = Node(next_x, next_y, g_cost, h_cost)
                neighbor.parent = current
                heapq.heappush(open_list, neighbor)
                node_dict[(next_x, next_y)] = neighbor
            else:
                neighbor = node_dict[(next_x, next_y)]
                if g_cost < neighbor.g_cost:
                    neighbor.g_cost = g_cost
                    neighbor.f_cost = g_cost + neighbor.h_cost
                    neighbor.parent = current
    
    print("No path found")  # Debug print
    return None

def initialize_maze():
    maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    frontiers = []
    add_frontiers(maze, start_x, start_y, frontiers)
    return maze, frontiers

def add_frontiers(maze, x, y, frontiers):
    for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < GRID_SIZE - 1 and 0 <= new_y < GRID_SIZE - 1 and 
            maze[new_y][new_x] == 1):
            frontiers.append((new_x, new_y))

def generate_maze():
    maze, frontiers = initialize_maze()
    
    while frontiers:
        current = random.choice(frontiers)
        frontiers.remove(current)
        x, y = current
        
        neighbors = []
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and
                maze[new_y][new_x] == 0):
                neighbors.append((new_x, new_y))
        
        if neighbors:
            nx, ny = random.choice(neighbors)
            middle_x = x + (nx - x) // 2
            middle_y = y + (ny - y) // 2
            
            if (0 <= middle_x < GRID_SIZE and 0 <= middle_y < GRID_SIZE):
                maze[y][x] = 0
                maze[middle_y][middle_x] = 0
                add_frontiers(maze, x, y, frontiers)
        
        screen.fill(BLACK)
        render_maze(maze)
        for fx, fy in frontiers:
            pygame.draw.rect(screen, RED, 
                           (fx * CELL_SIZE, fy * CELL_SIZE, 
                            CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        time.sleep(0.01)
    
    print("Maze generated")  # Debug print
    return maze

def render_maze(maze, path=None):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, 
                           (x * CELL_SIZE, y * CELL_SIZE, 
                            CELL_SIZE, CELL_SIZE))
    
    if path:
        for x, y in path:
            pygame.draw.rect(screen, GREEN, 
                           (x * CELL_SIZE, y * CELL_SIZE, 
                            CELL_SIZE, CELL_SIZE))

def main():
    maze = generate_maze()
    start = (1, 1)
    goal = (GRID_SIZE-2, GRID_SIZE-2)
    
    path = a_star(maze, start, goal)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    maze = generate_maze()
                    path = a_star(maze, start, goal)
        
        screen.fill(BLACK)
        render_maze(maze, path)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()