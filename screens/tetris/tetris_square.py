import pygame

from utils.colors import *

from utils.position import *

from utils.assets import *

class TetrisSquare:
    def __init__(self, size: float, position: Position, color, border_color = white) -> None:
        self.position = position
        self.color = color
        self.border_color = border_color
    
    def draw(self, screen):
        rect = pygame.Rect(self.position.x, self.position.y, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, self.border_color, rect, 1)