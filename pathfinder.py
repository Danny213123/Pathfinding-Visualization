# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:20:20 2022

@author: danny
"""

import math
from queue import PriorityQueue

# return manhattan distance between 2 points
def manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    
    return abs(x1 - x2) + abs(y1 - y2)

# return euclidean distance between 2 points
def euclidean_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

def reset_values(grid):
    
    for x in grid:
        
        for y in x:
            
            y.set_value(0)
            
def reset_root(grid):
    
    for x in grid:
        
        for y in x:
            
            y.set_root(None)
            
def path_length(grid):
    
    count = 0
    
    for x in grid:
        
        for y in x:
            
            if (y.get_path()):
                
                count += 1
                
    return count

def reconstruct_path(came_from, current, draw):
    
    while current in came_from:
        
        current = came_from[current]
        
        if (not current.get_start()):
            
            current.draw_path()
            
            draw()

# Breadth-first search
# Searches every node from last added node
def bfs (draw, grid, start, end, index):
    
    # moves = priorityqueue
    # neighbours appended into priority queue
    # print(start.get_pos())
    
    visited = []
    possible_moves = PriorityQueue()
    
    count = 0

    possible_moves.put(start)
    visited.append(start)
    
    while True:
        
        if (count == len(visited)):
            
            reset_root(grid)
            
            return ((count, False, path_length(grid)))
        
        for neighbour in visited[count].neighbours:
            
            if (neighbour.get_root() is None):
                
                    neighbour.set_root(visited[count])
                    
            root = neighbour
            
            if (neighbour.get_end()):
                
                while (root.get_root().get_pos() != start.get_pos()):
                    
                    root.get_root().draw_path()
                    
                    root = root.get_root()

                reset_root(grid)
                
                return ((count, True, path_length(grid)))
                    
            elif (not neighbour.opened_spot()) and not neighbour.get_value():
                    
                if (not neighbour.get_start()):
                    
                    neighbour.draw_opened()
                    
                visited.append(neighbour)
                
                #print(neighbour.get_pos(), neighbour.get_root().get_pos())
                
                draw()
                #time.sleep(0.1)
        count += 1
        
    #print(t_visited)
    reset_root(grid)
    return ((count, False, path_length(grid)))

# A star algorithm
def astar_algorithm(draw, grid, start, end):
    
    count = 0
    
    open_set = PriorityQueue()
    
    open_set.put((0, count, start))
    
    came_from = {}
    
    g_score = {spot: float("inf") for row in grid for spot in row}
    
    g_score[start] = 0
    
    f_score = {spot: float("inf") for row in grid for spot in row}
    
    f_score[start] = manhattan_distance(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        
        open_set_hash.remove(current)

        if current == end:
            
            reconstruct_path(came_from, end, draw)
            
            end.draw_end()
            
            #print(count)
            
            return ((count, True, path_length(grid)))

        for neighbour in current.neighbours:
            
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                
                came_from[neighbour] = current
                
                g_score[neighbour] = temp_g_score
                
                f_score[neighbour] = temp_g_score + manhattan_distance(neighbour.get_pos(), end.get_pos())
                
                if neighbour not in open_set_hash:
                    
                    count += 1
                    
                    open_set.put((f_score[neighbour], count, neighbour))
                    
                    open_set_hash.add(neighbour)
                    
                    neighbour.draw_opened()

        draw()

        if current != start:
            
            current.draw_closed()

    return ((count, False, path_length(grid)))



# depth first search but with weighted graphs
# the algorithm looks at child nodes with connected edges with the parent node
# it will pick the child node with the lowest euclidean distance to end position
# if a parent node has no valid child nodes, it will return to the previous node

def dfs(draw, grid, start, end, index):
    count = 0
    
    cur_pos = start
        
    while (index <= 100000):
        
        # initial temp value
        value = float ("inf")
        
        # if the euclidean distance from current position to end position is 0, return possible path
        
        # Look at the possible neighbours of current position
        for neighbour in cur_pos.neighbours:
            
            if (neighbour.get_root() is None):
                
                    neighbour.set_root(cur_pos)
            
            # if the euclidean value of neighbour is greater than set value, change value
            if (euclidean_distance(neighbour.get_pos(), end.get_pos()) > neighbour.get_value()):
                
                neighbour.set_value(euclidean_distance(neighbour.get_pos(), end.get_pos()))
            
            #print(neighbour.get_pos(), neighbour.get_value())
            
            # searchs
            count += 1
            
            if (not neighbour.get_path() and not neighbour.get_start() and not neighbour.get_end() and not neighbour.closed_spot()):
                
                neighbour.draw_opened()
            
            # if the neighbour value is less than current lowest value, that node is the best
            if neighbour.get_value() < value:
                
                value = neighbour.get_value()
                
                temp_pos = neighbour
                
            if (euclidean_distance(cur_pos.get_pos(), end.get_pos()) == 0):
            
                #print(count)
            
                reset_values(grid)
                
                reset_root(grid)
            
                return ((count, True, path_length(grid)))
                
            if (temp_pos == cur_pos.get_root()):
                
                index += 500;
                
                cur_pos = temp_pos
            else:
                
                cur_pos = temp_pos
        
        draw()
        
        cur_pos.add_value()
        
        if (not cur_pos.get_end() and not cur_pos.get_start() and not cur_pos.closed_spot()):
            
            cur_pos.draw_path()
            
        index += 1
        
                
        
    reset_root(grid)
    reset_values(grid)
    return ((count, False, path_length(grid)))
