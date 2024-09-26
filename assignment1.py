import numpy as np
import matplotlib.pyplot as plt
import random

# Generate a maze using DFS approach
def generate_maze(size):
    maze = np.zeros((size, size), dtype=int)  # 0: unvisited, 1: unblocked, -1: blocked
    start = (random.randint(0, size - 1), random.randint(0, size - 1))
    stack = [start]
    maze[start] = 1  # Mark as unblocked
    
    # DFS generation of the maze
    def neighbors(cell):
        row, col = cell
        options = []
        if row > 0:
            options.append((row - 1, col))
        if row < size - 1:
            options.append((row + 1, col))
        if col > 0:
            options.append((row, col - 1))
        if col < size - 1:
            options.append((row, col + 1))
        return options
    
    while stack:
        current = stack[-1]
        unvisited_neighbors = [n for n in neighbors(current) if maze[n] == 0]
        
        if unvisited_neighbors:
            neighbor = random.choice(unvisited_neighbors)
            if random.random() < 0.3:
                maze[neighbor] = -1  # 30% chance to block
            else:
                maze[neighbor] = 1  # Mark as unblocked and visit
                stack.append(neighbor)
        else:
            stack.pop()  # Backtrack if no unvisited neighbors
            
    return maze

# Generate 50 gridworlds and store them
def generate_multiple_mazes(num_mazes, size):
    mazes = [generate_maze(size) for _ in range(num_mazes)]
    return mazes

# Visualize the maze
def visualize_maze(maze):
    plt.imshow(maze, cmap="gray")
    plt.show()

# Store mazes to files
def store_mazes(mazes):
    for i, maze in enumerate(mazes):
        np.savetxt(f"maze_{i}.txt", maze, fmt='%d')

# Main
if __name__ == "__main__":
    num_mazes = 50
    size = 101
    
    # Generate mazes
    mazes = generate_multiple_mazes(num_mazes, size)
    
    # Visualize one of the mazes
    visualize_maze(mazes[0])
    
    # Save the mazes to text files
    store_mazes(mazes)
    print(f"Stored {num_mazes} mazes.")
