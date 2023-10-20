# Pathfinding Algorithms Visualization

This project implements various pathfinding algorithms and visualizes their operation on a grid. The algorithms included are Breadth-First Search (BFS), A* algorithm, Depth-First Search (DFS) for both weighted and unweighted graphs.

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- Python 3.x
- Required Python packages (install them using `pip install <package-name>`):
  - `pygame` for visualization

### Installing

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/pathfinding-algorithms.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pathfinding-algorithms
    ```

3. Install the required Python packages:

    ```bash
    pip install pygame
    ```

## Running the Application

1. Run the main script:

    ```bash
    python main.py
    ```

2. Follow on-screen instructions to draw obstacles and choose the start and end points.

3. Choose the algorithm you want to visualize.

4. Watch the visualization of the selected pathfinding algorithm.

## Algorithms

### Breadth-First Search (BFS)

BFS is an algorithm for traversing or searching tree or graph data structures. It explores all the vertices at the present depth prior to moving on to vertices at the next depth level.

### A* Algorithm

A* is a popular pathfinding algorithm that uses a combination of the cost to reach the node (known as `g-score`) and the estimated cost to the goal from the current node (known as `h-score`). It uses a priority queue to explore nodes in order of their total cost (`f-score`).

### Depth-First Search (DFS)

DFS is an algorithm for traversing or searching tree or graph data structures. It explores as far as possible along each branch before backtracking.

### Depth-First Search (DFS) with Weighted Graphs

DFS for weighted graphs. It looks at child nodes with connected edges to the parent node and picks the child node with the lowest Euclidean distance to the end position. If a parent node has no valid child nodes, it returns to the previous node.

### Depth-First Search (DFS) with Unweighted Graphs

DFS for unweighted graphs. It looks at child nodes with connected edges to the parent node and picks the child node with the lowest Euclidean distance to the end position. If a parent node has no valid child nodes, it returns to the previous node.

## Classes

### `square` Class

Represents a square in the grid.

**Attributes:**
- `row` and `col`: Row and column indices of the square.
- `x` and `y`: Coordinates of the square.
- `width`: Width of the square.
- `total_rows`: Total number of rows in the grid.
- `colour`: Color of the square.
- `value`: A numerical value associated with the square.
- `neighbours`: List of neighboring squares.
- `root`: The root node of the square (used in pathfinding algorithms).

### `button` Class

Represents a button for user interaction.

**Attributes:**
- `pressed`: Indicates whether the button is pressed.
- `elevation` and `dynamic_elevation`: Control button elevation.
- `original_y_pos`: Original y-position of the button.
- `top_rect` and `bottom_rect`: Rectangles representing the button.
- `top_color` and `bottom_color`: Colors of the button.
- `text_surf` and `text_rect`: Surface and rectangle for the button's text.

**Methods:**
- `draw()`: Draws the button.
- `return_click()`: Returns whether the button is clicked.
- `check_click()`: Checks if the button is clicked.

## Functions

### `find_neighbours(i, j)` Function

Returns a list of neighboring coordinates for a given position `(i, j)`.

### `is_valid(i, j, m_row)` Function

Checks if a given coordinate `(i, j)` is within the grid boundaries.

### `return_neighbours(grid)` Function

Prints the neighbors of each square in the grid.

### `save_grid(grid)` and `load_grid()` Functions

Save and load the grid state using Pickle.

### `draw_grid(Game, rows, width)` Function

Draws the grid lines on the game window.

### `draw(Game, grid, rows, width)` Function

Draws the entire grid, including squares and grid lines.

### `get_clicked_pos(pos, rows, width)` Function

Converts mouse click position to grid coordinates.

### `initialize_game(Game, grid)` Function

Initializes the game by randomly drawing walls on the grid.

### `wipe_grid(Game, grid)` Function

Resets the grid by clearing previously drawn paths and walls.

### `function(button)` Function

Handles button interactions and returns whether a button is clicked.

### `main(Game, rows, width, generate, g_type)` Function

The main function that sets up the game, handles user input, and runs pathfinding algorithms based on user interactions.

## generate_maze(grid)

### Set Up Helper Functions

- **find_neighbours_maze(i, j):**
  Returns a list of neighboring coordinates for a given position (i, j).

- **is_valid(i, j, m_row):**
  Checks if a given coordinate (i, j) is within the grid boundaries.

### Initialization

- **Reset all squares in the grid to walls.**

### Randomly Choose a Starting Square

- Pick a random starting square (currently set at a fixed position for reproducibility).
- Make the starting square a passage.

### Randomized Prim's Algorithm

- Create a list called frontier to store frontier cells.
- Create a list called path and add the starting square to it.
- Loop until the frontier list is empty:
  - Pick a random square from the path.
  - Find the neighbors of the square.
  - Extend the frontier list with the neighbors.
  - If there are frontier squares:
    - Pick a random frontier square.
    - Turn the square into a passage and remove it from the frontier.
    - Find the neighbors of the chosen square and add them to the frontier.
    - Add the chosen square to the path.

### Clean Up

- Clear the neighbors list for each square in the grid.

### Return the Modified Grid

The function returns the modified grid with the generated maze.

