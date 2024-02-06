import random
import os

def game_of_life(grid, draw, clock):
    print(grid)

    for x in grid:
        for square in x:
            square.reset()

    random_state(grid)

    for i in range(100):
        next_generation(grid, draw)
        draw()
        clock.tick(10)

    return grid

def next_generation (grid, draw):
    row, col = len(grid), len(grid[0])

    for i in range(row):
        for j in range (col):

            cur_square = grid[i][j]

            cur_square.find_nearby_spots_gol(grid)

            alive_neighbours = len(cur_square.neighbours)

            if cur_square.get_wall():
                if alive_neighbours < 2 or alive_neighbours > 3:
                    cur_square.reset()

            else:

                if alive_neighbours == 3:
                    cur_square.draw_wall()

def random_state(grid) -> None:

    total_alive = 0

    while total_alive <= 100:

        row = random.randint(0, len(grid) - 1)
        col = random.randint(0, len(grid) - 1)

        if not grid[row][col].get_wall():
            grid[row][col].draw_wall()
            total_alive += 1