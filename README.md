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
