from screens.tetris.tetris_grid import *

from screens.tetris.tetromino import *

import random

class TetrisGame:
    def __init__(self) -> None:
        self.tetris_grid = TetrisGrid()
        
        self.available_tetrominos = self.get_all_tetrominos()
        
        self.current_tetromino = self.get_random_tetromino()
        self.next_tetromino = self.get_random_tetromino()
        
    def get_all_tetrominos(self):
        return [
            TetrominoI(),
            TetrominoJ(),
            TetrominoL(),
            TetrominoO(),
            TetrominoS(),
            TetrominoT(),
            TetrominoZ(),
        ]
        
    def get_random_tetromino(self) -> Tetromino:
        if len(self.available_tetrominos) == 0:
            self.available_tetrominos = self.get_all_tetrominos()
        tetromino = random.choice(self.available_tetrominos)
        self.available_tetrominos.remove(tetromino)
        return tetromino
    
    def rotate(self):
        self.current_tetromino.rotate()
        
    def move_down(self):
        self.current_tetromino.move(0, 1)
        
        if self.tetromino_collided_bottom():
            self.current_tetromino.move(0, -1)
            self.stop_tetromino()
    
    def move_left(self):
        self.current_tetromino.move(-1, 0)
        if self.tetromino_collided_side():
            self.current_tetromino.move(1, 0)
        
    def move_right(self):
        self.current_tetromino.move(1, 0)
        if self.tetromino_collided_side():
            self.current_tetromino.move(-1, 0)
        
    def stop_tetromino(self):
        for cell in self.current_tetromino.get_cell_positions():
            self.tetris_grid.update_grid(cell.x, cell.y, self.current_tetromino.shape.value)
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = self.get_random_tetromino()
        self.clear_completed_rows()
        
    def tetromino_collided_side(self):
        collided_side = False
        for cell in self.current_tetromino.get_cell_positions():
            if cell.y == self.tetris_grid.width or cell.y == -1 or self.tetris_grid.grid[cell.x][cell.y] != 0:
                collided_side = True
        return collided_side
        
    def tetromino_collided_bottom(self):
        collided_bottom = False
        for cell in self.current_tetromino.get_cell_positions():
            if cell.x == self.tetris_grid.height or self.tetris_grid.grid[cell.x][cell.y] != 0:
                collided_bottom = True
        return collided_bottom
    
    def clear_completed_rows(self):
        for index, row in enumerate(self.tetris_grid.grid):
            if self.is_row_completed(row):
                self.tetris_grid.grid[index] = [0 for _ in range(self.tetris_grid.width)]
             
    def is_row_completed(self, row: list[int]):
        return all(value != 0 for value in row)
        
    def draw(self, screen):
        self.tetris_grid.draw(screen)
        self.current_tetromino.draw(screen)