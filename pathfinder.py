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

# reset the values of all nodes
def reset_values(grid):
    
    for x in grid:
        
        for y in x:
            
            y.set_value(0)
            
# reset the root nodes of all nodes            
def reset_root(grid):
    
    for x in grid:
        
        for y in x:
            
            y.set_root(None)
            
# return the length of the path
def path_length(grid):
    
    count = 0
    
    for x in grid:
        
        for y in x:
            
            if (y.get_path()):
                
                count += 1
                
    return count

# reconstructs the path from the end node to the start node
def reconstruct_path(came_from, current, draw):
    
    # check through all root nodes from current
    while current in came_from:
        
        # change current node to the root node of current
        current = came_from[current]
        
        # if current is not start
        if (not current.get_start()):
            
            # draw the path
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
    
    # while the queue is not empty
    while True:
        
        # if the queue is empty, return no path
        if (count == len(visited)):
            
            reset_root(grid)
            
            return ((count, False, path_length(grid)))
        
        # run through all opened nodes incrementally by 1
        for neighbour in visited[count].neighbours:
            
            if (neighbour.get_root() is None):
                
                    neighbour.set_root(visited[count])

            # set the root node to the first neighbour node        
            root = neighbour
            
            # if the neighbour is the end node, return path
            if (neighbour.get_end()):
                
                # while the root node is not the start node
                while (root.get_root().get_pos() != start.get_pos()):
                    
                    # draw the path
                    root.get_root().draw_path()
                    
                    # set the root node to the previous node
                    root = root.get_root()

                # reset the root node
                reset_root(grid)
                
                # return the path (path found)
                return ((count, True, path_length(grid)))
                    
            # if the neighbour is not the end node and not already searched, add it to the queue
            elif (not neighbour.opened_spot()) and not neighbour.get_value():
                    
                # add the neighbour to the queue    
                if (not neighbour.get_start()):
                    
                    neighbour.draw_opened()
                    
                # add the neighbour to the queue    
                visited.append(neighbour)
                
                #print(neighbour.get_pos(), neighbour.get_root().get_pos())
                
                draw()
                #time.sleep(0.1)

        # increment the count        
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

    # while the queue is not empty
    while not open_set.empty():

        # set current node to the first node in the queue
        current = open_set.get()[2]
        
        # remove the current node from the queue
        open_set_hash.remove(current)

        # if the current node is the end node, return path
        if current == end:
            
            reconstruct_path(came_from, end, draw)
            
            end.draw_end()
            
            #print(count)
            
            return ((count, True, path_length(grid)))

        # for all neighbours of current node
        for neighbour in current.neighbours:
            
            temp_g_score = g_score[current] + 1

            # if the temp g score is less than the g score of the neighbour, change the g score of the neighbour
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
        
    # node search limit (time constraint)    
    while (index <= 100000000):
        
        # initial temp value
        value = float ("inf")
        
        # if the euclidean distance from current position to end position is 0, return possible path
        
        # Look at the possible neighbours of current position
        for neighbour in cur_pos.neighbours:
            
            # if the neighbour has no root, set the root to the current position
            if (neighbour.get_root() is None):
                
                neighbour.set_root(cur_pos)
            
            # if the euclidean value of neighbour is greater than set value, change value
            if (euclidean_distance(neighbour.get_pos(), end.get_pos()) > neighbour.get_value()):
                
                neighbour.set_value(euclidean_distance(neighbour.get_pos(), end.get_pos()))
            
            #print(neighbour.get_pos(), neighbour.get_value())
            
            # searchs
            count += 1
            
            # if the neighbour is not already searched, apart of the current path, the end, or the start, search it
            if (not neighbour.get_path() and not neighbour.get_start() and not neighbour.get_end() and not neighbour.closed_spot()):
                
                neighbour.draw_opened()
            
            # if the neighbour value is less than current lowest value, that node is the best
            if neighbour.get_value() < value:
                
                value = neighbour.get_value()
                
                temp_pos = neighbour
                
            # if the neighbour is the end node, return path    
            if (euclidean_distance(cur_pos.get_pos(), end.get_pos()) == 0):
            
                #print(count)
            
                reset_values(grid)
                
                reset_root(grid)
            
                return ((count, True, path_length(grid)))
                
            # backtrack to root node    
            if (temp_pos == cur_pos.get_root()):
                
                index += 500;
                
                cur_pos = temp_pos

            # backtrack to root node    
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

# depth first search but with unweighted graphs
# the algorithm looks at child nodes with connected edges with the parent node
# if a parent node has no valid child nodes, it will return to the previous node

from queue import LifoQueue

def dfs_unweighted(draw, grid, start, end, index):
    visited = []
    stack = LifoQueue()
    
    count = 0

    stack.put(start)
    visited.append(start)
    
    # while the stack is not empty
    while not stack.empty():
        # pop the top node from the stack
        current_node = stack.get()

        # if the stack is empty, return no path
        if count == len(visited):
            reset_root(grid)
            return count, False, path_length(grid)

        # run through all opened nodes incrementally by 1
        for neighbour in current_node.neighbours:
            if neighbour.get_root() is None:
                neighbour.set_root(current_node)

            root = neighbour
            
            # if the neighbour is the end node, return path
            if neighbour.get_end():
                while root.get_root().get_pos() != start.get_pos():
                    root.get_root().draw_path()
                    root = root.get_root()

                reset_root(grid)
                return count, True, path_length(grid)

            # if the neighbour is not the end node and not already searched, add it to the stack
            elif not neighbour.opened_spot() and not neighbour.get_value():
                if not neighbour.get_start():
                    neighbour.draw_opened()

                stack.put(neighbour)
                visited.append(neighbour)

                draw()

        count += 1

    reset_root(grid)
    return count, False, path_length(grid)


                
                

