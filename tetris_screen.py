import pygame, sys

from pygame.surface import Surface

from game_state_manager import *

move_down_event = pygame.USEREVENT + 1

MOVE_SIDE = 100

from assets import *

from tetris_game import *

class TetrisScreen:
    def __init__(self, screen: Surface, game_state_manager: GameStateManager):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        
        self.game_state_manger = game_state_manager
        
        self.pos_x = 50
        self.pos_y = 50
        
        pygame.time.set_timer(move_down_event, MOVE_SIDE)
        
        self.game = TetrisGame()    
        
    def run(self):
        self.screen.fill(black_pearl)
        self.handle_events()
        
        self.game.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == move_down_event:
                self.game.move_down()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.move_left()
                if event.key == pygame.K_RIGHT:
                    self.game.move_right()
                if event.key == pygame.K_UP:
                    self.game.rotate()
