def generate_maze(grid):
    import random

    # Helper function to find neighbors of a square
    def find_neighbours_maze(i, j):
        return [(i - 2, j), (i + 2, j), (i, j - 2), (i, j + 2)]

    # Helper function to check if a coordinate is within the grid boundaries
    def is_valid(i, j, m_row):
        return 0 <= i < m_row and 0 <= j < m_row

    # Get the number of rows in the grid
    rows = len(grid)

    # Reset all squares to walls
    for x in grid:
        for square in x:
            square.draw_wall()

    # pick a random starting square
    # start_row = random.randint(0, rows - 1)
    # start_col = random.randint(0, rows - 1)

    start_row = 1
    start_col = 1

    # Make the starting square a passage
    cur_square = grid[start_col][start_row]
    # cur_square.draw_start()

    frontier = []
    path = [cur_square]

    # Find the neighbors of the starting square
    for x in range(3000):

        # Pick a random square from the path
        cur_square = random.choice(path)

        # Find the neighbors of the square
        cur_square.find_nearby_spots_maze(grid)
        
        # Find the neighbors of the square
        frontier.extend(cur_square.neighbours)

        # If there are no neighbors, remove the square from the path
        if frontier:

            # Pick a random neighbor
            random_frontier_square = random.choice(frontier)

            #for cell in frontier:
            #    cell.draw_opened()

            # Turn the square into a passage
            random_frontier_square.reset()
            random_frontier_square.root.reset()

            # Remove the square from the frontier
            frontier.remove(random_frontier_square)

            # Find the neighbors of the square
            random_frontier_square.find_nearby_spots_maze(grid)
            frontier.extend(random_frontier_square.neighbours)

            # Add the square to the path
            path.append(random_frontier_square)

    # remember to clear the neighbors list
    for x in grid:
        for square in x:
            square.neighbours = []

    return grid