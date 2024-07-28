from enum import Enum

from tetris_square import *

from position import Position

from assets import *

class TetrominoShape(Enum):
    I = 1
    O = 2
    T = 3
    S = 4
    Z = 5
    J = 6
    L = 7
    
class Tetromino:
    def __init__(self, shape: TetrominoShape) -> None:
        self.shape = shape
        self.rotation = 0
        self.cell_size = 25
        self.horizontal_move = 0
        self.vertical_move = 0
        self.cells : dict[int, list[Position]] = {}
        
    def move(self, horizontal_move, vertical_move):
        self.horizontal_move += horizontal_move
        self.vertical_move += vertical_move
        
    def rotate(self):
        self.rotation += 1
        if self.rotation >= len(self.cells):
            self.rotation = 0 
        
    def get_cell_positions(self) -> list[Position]:
        cells = self.cells[self.rotation]
        cells_position = []
        for cell in cells:
            moved_position = Position(cell.x + self.vertical_move, cell.y + self.horizontal_move)
            cells_position.append(moved_position)
        return cells_position
        
    def draw(self, screen):
        for cell in self.get_cell_positions():
            square = TetrisSquare(self.cell_size, Position(cell.y * self.cell_size, cell.x * self.cell_size), get_color_by_value(self.shape.value))
            square.draw(screen)
            
          
class TetrominoI(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.I)
        self.cells = {
            0 : [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1 : [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2 : [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3 : [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]
        }
        self.move(3, -1)
    
class TetrominoJ(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.J)
        self.cells = {
            0 : [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
            1 : [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
            2 : [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
            3 : [Position(0,1), Position(1,1), Position(2,0), Position(2,1)]
        }
        self.move(3, 0)
        
    
class TetrominoL(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.L)
        self.cells = {
            0 : [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1 : [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            2 : [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3 : [Position(0,0), Position(0,1), Position(1,1), Position(2,1)]
        }
        self.move(3, 0)

class TetrominoO(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.O)
        self.cells = {
            0 : [Position(0,1), Position(0,2), Position(1,1), Position(1,2)],
        }
        self.move(3, 0)
        
class TetrominoS(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.S)
        self.cells = {
            0 : [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],
            1 : [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2 : [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],
            3 : [Position(0,0), Position(1,0), Position(1,1), Position(2,1)]
        }
        self.move(3, 0)

        
class TetrominoT(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.T)
        self.cells = {
            0 : [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
            1 : [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
            2 : [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],
            3 : [Position(0,1), Position(1,0), Position(1,1), Position(2,1)]
        }
        self.move(3, 0)

class TetrominoZ(Tetromino):
    def __init__(self) -> None:
        super().__init__(TetrominoShape.Z)
        self.cells = {
            0 : [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],
            1 : [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2 : [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3 : [Position(0,1), Position(1,0), Position(1,1), Position(2,0)]
        }
        self.move(3, 0)