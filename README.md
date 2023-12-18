# 2D-puzzle-solver


## Overview
This Python script provides a solution to solving a 2-Dimensional (2D) puzzle using the Breadth-First Search (BFS) algorithm. The puzzle is represented as a grid of size M x N, where M is the number of rows and N is the number of columns. The script finds a path from a specified source point to a destination point in the grid.

## Features
- **BFS Algorithm**: Efficiently navigates through the grid.
- **Path Recovery**: Recovers the entire path from source to destination.
- **Direction Tracking**: Keeps track of the directions taken along the path.

## Requirements
- Python 3.x
- No external libraries required.

## Installation
No installation is required. Simply download the `.py` file and run it using a Python interpreter.

## Usage
To use the script, you need to have a 2D grid representing the puzzle, where each cell can be traversable (marked by '-') or non-traversable. Define the source and destination points as coordinates within the grid.

Example:
\```python
puzzle = [
    ['-', '-', '-', '-'],
    ['-', 'X', 'X', '-'],
    ['-', '-', '-', '-'],
    ['-', 'X', '-', '-']
]
source = (0, 0)  # Starting point (row, column)
destination = (3, 3)  # Ending point (row, column)

path, directions = solve_puzzle(puzzle, source, destination)
\```

## Function Description
- `solve_puzzle(puzzle, source, destination)`: Solves the puzzle.
  - **Parameters**:
    - `puzzle`: 2D list representing the puzzle grid.
    - `source`: Tuple (x, y) representing the starting point.
    - `destination`: Tuple (x, y) representing the ending point.
  - **Returns**:
    - A tuple containing the path and directions if a path exists, otherwise `(None, None)`.

## Complexity
The time complexity of this algorithm is O(M x N), where M and N are the dimensions of the puzzle.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-issues-page) if you want to contribute.
