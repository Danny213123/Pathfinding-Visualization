# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:11:34 2022

@author: danny
"""
import pygame
import random as r
import pathfinder as pf
#import clock

pygame.init()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
red = (128, 0, 0)
navy = (128,0,128)

gui_font = pygame.font.Font(None, 25)

width = 800
rows = 50
Game = pygame.display.set_mode((width, width))
pygame.display.set_caption("Game Test")
    
clock = pygame.time.Clock()

# Return all possible neighbours of current x_pos and y_pos
def find_neighbours(i, j):
    
    # LEFT  x,   y-1
    # RIGHT x,   y+1
    # UP    x+1, y
    # DOWN  x-1, y
    
    #return [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1,j+1), (i-1,j-1), (i-1,j+1), (i+1,j-1)]
    return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

# Check if neighbour x_pos and y_pos within boundaries
def is_valid(i, j, m_row):
    
    if (0 <= i < m_row and 0 <= j < m_row):
                
        return True
    
    else:
        
        return False
    
# Print all neighbours of current square
def return_neighbours(grid):
    for x in grid:
        for y in x:
            print(list(y.neighbours))
    
# Button
class button():
    
    def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

		# bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
		#text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
		# elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(Game,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(Game,self.top_color, self.top_rect,border_radius = 12)
        Game.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def return_click (self):
        return self.pressed

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    self.return_click()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'
        
    
buttons = []

buttons.append(button("Simulate", 200, 40, (width+100, width-700), 5))
buttons.append(button("Change", 200, 40, (width+100, width-650), 5))
buttons.append(button("Clear", 200, 40, (width+100, width-600), 5))
buttons.append(button("Reset", 200, 40, (width+100, width-550), 5))
    
# Square object class
class square():
    
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.colour = (255, 255, 255)
        self.value = 0
        self.neighbours = []
        self.root = None
        
    # return current position
    def get_pos(self):
        return (self.row, self.col)
    
    def get_clear(self):
        return self.colour == white
    
    def closed_spot(self):
        return self.colour == red
        
    def opened_spot(self):
        return self.colour == blue
    
    def get_wall(self):
        return self.colour == black
    
    def get_start(self):
        return self.colour == lime
    
    def get_end(self):
        return self.colour == navy
    
    def get_root(self):
        return self.root
    
    def get_path(self):
        return self.colour == (25, 145, 55)
    
    def set_root(self, node):
        self.root = node
    
    def set_value(self, value):
        self.value = value
        
    def add_value(self):
        self.value += 9999;
        
    def get_value(self):
        return self.value
    
    def reset(self):
        self.colour = white
        
    def draw_closed(self):
        self.colour = red
        
    def draw_opened(self):
        self.colour = blue
        
    def draw_wall(self):
        self.colour = black
        
    def draw_end(self):
        self.colour = navy
        
    def draw_start(self):
        self.colour = lime
        
    def draw_path(self):
        self.colour = (25, 145, 55)
    
    # Draw square
    def draw(self,  Game):
        pygame.draw.rect(Game, self.colour, (self.x, self.y, self.width, self.width))
    
    # Place all valid neighbours into neighbours list
    def find_nearby_spots(self, matrix):
        self.neighbours = []
        
        for k in find_neighbours(self.row, self.col):
            look_row, look_col = k
            
            if (is_valid(look_row, look_col, self.total_rows)):
                if (not matrix[look_row][look_col].get_wall()):
                    self.neighbours.append(matrix[look_row][look_col])
                
    # Less than operator
    def __lt__ (self, other):
        return False
    
# Creates square objects, puts it in a grid
def make_grid(rows, width):
    
    grid = []
    
    for x in range(rows):
        
        temp = []
        
        for y in range(rows):
            
            # Create square objects
            spot = square(x, y, (width // rows), rows)
            
            temp.append(spot)
            
        grid.append(temp)

    return grid

# draw grid
def draw_grid(Game, rows, width):
    
    # Gap for each square
	gap = width // rows
    
	for i in range(rows):
        
        # Draw lines (horizontal)
		pygame.draw.line(Game, black, (0, i * gap), (width, i * gap))
        
		for j in range(rows+1):
            
            # Draw lines (vertical)
			pygame.draw.line(Game, black, (j * gap, 0), (j * gap, width))

# draw on the grid
def draw(Game, grid, rows, width):
    
    Game.fill(white)

    for x in grid:
        
        for square in x:
            
            square.draw(Game)


    draw_grid(Game, rows, width)
    
    for x in buttons:
        x.draw()
    
    pygame.display.update()

# Get Position of mouse click
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

# Draw walls on the matrix
def initialize_game(Game, grid):
    
    for x in grid:
        
        for square in x:
            
            if (r.randint(0, 100) <= 75):
                
                square.draw(Game)
                
            else:
                
                square.draw_wall()

# Reset grid
def wipe_grid(Game, grid):
    
    for x in grid:
        
        for y in x:
            
            if (y.closed_spot() or y.opened_spot() or y.get_path()):
                
                y.reset()
                
def function(button):
    
    if (button.top_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
        
        button.draw()
        
        pygame.display.update()
        
        return True

# Main
def main(Game, rows, width, generate, g_type):
    
    grid = make_grid(rows, width)
    
    algorithm = ["DFS", "BFS", "A_STAR"]
    
    i = algorithm.index(g_type)

    # Square object of start
    start = None
    
    # Square object of end
    end = None
    
    if(generate):
        
        initialize_game(Game, grid)
    
    run = True
    
    while run:
        
        draw(Game, grid, rows, width)
        
        # Get pygame event
        for event in pygame.event.get():
            
            # Quit game
            if event.type == pygame.QUIT:
                
                run = False
            
            # Left Click
            if pygame.mouse.get_pressed()[0]:
            
                pos = pygame.mouse.get_pos()
                
                row, col = get_clicked_pos(pos, rows, width)
                
                if (row < rows):
                
                    spot = grid[row][col]
                                    
                    spot.find_nearby_spots(grid)
                                
                    # Draw start
                    if not start and spot != end:
                        
                        start = spot
                        
                        start.draw_start()
            
                    # Draw end
                    elif not end and spot != start:
                        
                        end = spot
                        
                        end.draw_end()
            
                    # Draw wall
                    elif spot != end and spot != start:
                        
                        spot.draw_wall()
        
            # Right Click, remove placed stuff
            elif pygame.mouse.get_pressed()[2]:
                
                pos = pygame.mouse.get_pos()
                
                row, col = get_clicked_pos(pos, rows, width)
                
                if (row < rows):
                    spot = grid[row][col]
                    
                    spot.reset()
                    
                    if spot == start:
                        
                        start = None
                        
                    elif spot == end:
                        
                        end = None       
            
        clock.tick(10)
        if function(buttons[0]) and start and end:
            
            wipe_grid(Game, grid)
            
            for row in grid:
                
                for spot in row:
                    
                    spot.find_nearby_spots(grid)
            
            if (i == 2):
                
                count, result, length = pf.astar_algorithm(lambda: draw(Game, grid, rows, width), grid, start, end)
                
                if (result):
                    
                    print(f"A-Star, {count} cells searched, length: {length}")
                
                else:
                    
                    print("No path found")
                    
            elif (i == 0):
                
                count, result, length = pf.dfs(lambda: draw(Game, grid, rows, width), grid, start, end, 1)
                
                if (result):
                    
                    print(f"Depth-First Search, {count} cells searched, length: {length}")
                
                else:
                    
                    print("No path found")
                    
            elif (i == 1):
                
                count, result, length = pf.bfs(lambda: draw(Game, grid, rows, width), grid, start, end, 1)
                
                if (result):
                    
                    print(f"Breadth-First Search, {count} cells searched, length: {length}")
                
                else:
                    
                    print("No path found")
                    
            else:
                
                i == 0
        
        elif function(buttons[1]):
            
            if (0 <= i + 1 <= 2):
                        
                i += 1
                #print(i)
            else:
                
                i = 0
                
            print(f"algorithm changed to {algorithm[i]}")
            
        elif function(buttons[2]):
            
            wipe_grid(Game, grid)
            
        elif (function(buttons[3])):
            
            start = None
                    
            end = None
            
            grid = make_grid(rows, width)
            
            if(generate):
                
                initialize_game(Game, grid)
                    
        #clock.tick(20)
                    
    pygame.quit()

#main(Game, rows, width, True)