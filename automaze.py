import random
import os

WIDTH = 21
HEIGHT = 21

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "maze.txt")

def generate_maze(w, h):
    maze = [['#' for _ in range(w)] for _ in range(h)]
    
    def carve(x, y):
        dirs = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < w-1 and 1 <= ny < h-1 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[y + dy//2][x + dx//2] = ' '
                carve(nx, ny)

    # carve maze
    maze[1][1] = ' '
    carve(1, 1)

    # add Start (A) and End (B)
    maze[1][1] = 'A'
    maze[h-2][w-2] = 'B'

    return maze

def save_maze(maze, path):
    if os.path.exists(path):
        os.remove(path)
    with open(path, "w") as f:
        for row in maze:
            f.write("".join(row) + "\n")

maze = generate_maze(WIDTH, HEIGHT)
save_maze(maze, FILE_PATH)

print("Maze saved at:", FILE_PATH)
