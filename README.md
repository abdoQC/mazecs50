# Maze Generator & Solver — CS50 AI Practice Project

A Python practice project based on the maze-search material from Harvard's **CS50's Introduction to Artificial Intelligence with Python**. It generates a random maze and finds a path from the start point to the goal using **Breadth-First Search (BFS)**.

## Features

- Generates a new 21 × 21 maze every run using recursive backtracking.
- Places a start point (`A`) and goal point (`B`).
- Solves the maze with a queue-based Breadth-First Search (BFS) frontier.
- Prints the maze and the final path in the terminal.
- Exports a visual solution image (`maze.png`), including walls, the explored area, start, goal, and solution path.

## Attribution and personal modifications

This project builds on the maze-search concepts and starter structure from Harvard's CS50 AI course. I extended the project by adding:

- Random maze generation with `automaze.py`
- A queue-based BFS solver configuration
- A color-coded solution and explored-state image generated with Pillow

## Project files

```text
automaze.py  # Generates and saves maze.txt
maze.py      # Solves maze.txt and creates maze.png
```

`maze.txt` and `maze.png` are generated at runtime and are intentionally not tracked in the repository.

## How it works

1. `automaze.py` creates a randomized maze using recursive backtracking.
2. The maze is stored in `maze.txt`.
3. `maze.py` reads the maze and models each open cell as a search state.
4. BFS explores adjacent cells until it reaches `B`.
5. Parent pointers reconstruct the route from `A` to `B`.
6. Pillow generates a color-coded image of the result.

## Run locally

```bash
python automaze.py
python maze.py maze.txt
```

### Requirements

```bash
pip install pillow
```

> If your Windows terminal cannot print the maze walls, use UTF-8 output:

```powershell
$env:PYTHONIOENCODING = "utf-8"
python automaze.py
python maze.py maze.txt
```

## Color legend

- **Red:** Start point
- **Green:** Goal point
- **Yellow:** Final solution path
- **Orange:** Explored states
- **Dark gray:** Maze walls

## Concepts practiced

- Breadth-First Search (BFS)
- Queue frontier and graph traversal
- Maze generation with recursive backtracking
- State-space search
- Solution-path reconstruction
- Image generation with Pillow
