import random
import pygame

# Parameters for the maze
WIDTH, HEIGHT = 800, 800  # Pygame window size
GRID_SIZE = 200  # Size of the grid (200x200)
CELL_SIZE = WIDTH // GRID_SIZE  # Size of each cell

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prim's Maze Generator")

# Directions for random movement (up, down, left, right)
directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

# Create a grid of walls (1) and empty cells (0)
def initialize_maze():
    maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Start with a random cell
    start_x, start_y = random.randrange(0, GRID_SIZE, 2), random.randrange(0, GRID_SIZE, 2)
    maze[start_y][start_x] = 0  # Mark the start cell as open
    
    # List of walls to be processed
    walls = []
    walls.append((start_x, start_y))
    
    return maze, walls

# Prims Algorithm for maze generation
def generate_maze():
    maze, walls = initialize_maze()
    
    while walls:
        # Pick a random wall from the walls list
        wx, wy = random.choice(walls)
        walls.remove((wx, wy))  # Remove this wall from the list
        
        # Check if the wall is adjacent to exactly one open cell
        neighbors = 0
        directions_to_check = []
        for dx, dy in directions:
            nx, ny = wx + dx, wy + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[ny][nx] == 0:
                neighbors += 1
            elif 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[ny][nx] == 1:
                directions_to_check.append((nx, ny))
        
        # If exactly one neighbor is open, it's part of the maze
        if neighbors == 1:
            maze[wy][wx] = 0  # Mark the wall as part of the path
            for nx, ny in directions_to_check:
                if maze[ny][nx] == 1:
                    walls.append((nx, ny))  # Add neighboring walls to the list
    
    return maze

# Function to render the maze using Pygame
def render_maze(maze):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()  # Update the screen after drawing

# Main Game Loop
def main():
    maze = generate_maze()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(GREEN)  # Fill the screen with green before drawing
        render_maze(maze)
        pygame.display.update()  # Ensure the screen updates after rendering
    
    pygame.quit()

if __name__ == "__main__":
    main()

