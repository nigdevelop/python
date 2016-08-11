"""
Clone of 2048 game.
"""

#import poc_2048_gui
#import user40_raqHmeU2I6_6 as poc_2048_test
#import poc_2048_test
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def create_slide_list(line):
    """
    Function that creates a new list with same size but 
    numbers slid over.
    """    
    slide_list = list()
    for num in line:
        if(num != 0):
            slide_list.append(num)
            
    zeros_to_insert = len(line) - len(slide_list)
    slide_list = slide_list + ([0] * zeros_to_insert)
        
    return slide_list

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    merged_list = create_slide_list(line)
    counter = 0
    while counter<len(merged_list)-1:
        if(merged_list[counter] == merged_list[counter+1]):
            merged_list[counter] = merged_list[counter] * 2
            merged_list[counter+1] = 0
            counter += 2
        else:
            counter = counter + 1
           
    return create_slide_list(merged_list)

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

        self._initial_tiles = {UP: self.list_initial_tiles(grid_width, 0, True),
                              DOWN: self.list_initial_tiles(grid_width,grid_height-1, True),
                              RIGHT: self.list_initial_tiles(grid_height, grid_width-1, False),
                              LEFT: self.list_initial_tiles(grid_height, 0, False)}
        print self._initial_tiles

    def list_initial_tiles(self, size, constant_element, first_constant):
        """
        Create the initial tile set for each direction.
        """
        initial_tiles = []
        for num in range(size):
            if(first_constant):
                initial_tiles.append((constant_element, num))
            else:
                initial_tiles.append((num, constant_element))
        return initial_tiles

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_i in range(self._grid_width)] for dummy_row in range(self._grid_height)] 
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return  str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        value_change = False
        if(direction<3):
            num_steps = self.get_grid_height()
        else:
            num_steps = self.get_grid_width()
        traverse =  OFFSETS[direction]
        starting_pos = self._initial_tiles[direction]
        for each_pos in starting_pos:
            to_be_merged = []
            for step in range(num_steps):
                row = each_pos[0] + step * traverse[0]
                col = each_pos[1] + step * traverse[1]
                to_be_merged.append(self.get_tile(row,col))
            merged_list = merge(to_be_merged)
            #print to_be_merged
            #print merged_list
           
            for step in range(num_steps):
                row = each_pos[0] + step * traverse[0]
                col = each_pos[1] + step * traverse[1]
                if(self.get_tile(row,col) != merged_list[step]):
                    value_change = True
                self.set_tile(row, col, merged_list[step])
         
        if(value_change):
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(0, self._grid_height)
        col = random.randrange(0, self._grid_width)
        while(self._grid[row][col] !=0):
            row = random.randrange(0, self._grid_height)
            col = random.randrange(0, self._grid_width)

        self._grid[row][col] = random.choice([2, 4, 2, 2, 2, 2, 2, 2, 2, 2])

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#poc_2048_test.run_suite(TwentyFortyEight(4, 4))
