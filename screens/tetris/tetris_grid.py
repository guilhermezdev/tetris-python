from typing import Tuple
from pygame.surface import Surface

from screens.tetris.tetris_square import *

from utils.colors import *

from screens.tetris.tetromino import *

from utils.position import *

from utils.assets import *

class TetrisGrid:
    def __init__(self) -> None:
        self.height = 24
        self.width = 10
        self.grid = [ [0 for j in range(self.width)] for i in range(self.height) ]
        
    
    def update_grid(self, row, column, value):
        self.grid[row][column] = value
        
    def draw(self, screen: Surface, position: Position = Position(0,0)):
        for y in range(self.height):
            for x in range(self.width):
                color = get_color_by_value(self.grid[y][x])
                
                position = Position( x * cell_size, y * cell_size ) 
                
                grid_square = TetrisSquare(cell_size, position, color)
                grid_square.draw(screen)
                
                