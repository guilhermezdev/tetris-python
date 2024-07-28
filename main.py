import  pygame

from game_state_manager import *

from screens.tetris.tetris_screen import TetrisScreen

w = 540
h = 960

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tetris')
        
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        
        self.game_state_manager = GameStateManager('tetris')
        
        self.tetris_screen = TetrisScreen(self.screen, self.game_state_manager)
        
        self.game_states = {'tetris': self.tetris_screen}
        
    def run(self):
        while True:
            pygame.display.update()
            self.clock.tick(60)
        
            self.game_states[self.game_state_manager.get_state()].run()

game = Game()
game.run()
