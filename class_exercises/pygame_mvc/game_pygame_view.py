import pygame
from game_controller import Game

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SQUARE_SIZE = 50

BACKGROUND_COLORS = {'W': 'gray30',
                     'S': 'gold',
                     'E': 'dodgerblue',
                     'F': 'white'
                     }

PLAYER_COLOR = 'firebrick'

class GameGUI:
    key_moves = {K_UP: 'N',
                 K_DOWN: 'S',
                 K_RIGHT: 'E',
                 K_LEFT: 'W',
                 }

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame MVC')

        # Set clock so that FPS can be limited
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.game.set_up()
        self.move_direction: str | None = None
        self.screen = pygame.display.set_mode([self.game.dimensions[1] * SQUARE_SIZE,
                                               self.game.dimensions[0] * SQUARE_SIZE])
        self.player = self.game.characters[0]
        self.running = True

    @staticmethod
    def _convert_position(pos: tuple, center: bool = False) -> tuple[int, int]:
        """ Convert a grid position in the game to an (x, y) coordinate
                if centre is false the position returned is top-left and if center is true
                the position returned is the centre """
        x, y = pos
        if center:
            return y * SQUARE_SIZE + SQUARE_SIZE // 2, x * SQUARE_SIZE + SQUARE_SIZE // 2
        else:
            return y * SQUARE_SIZE, x * SQUARE_SIZE


    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60) # cap to 60 FPS
        pygame.quit()

    def _handle_input(self):
        """ Checks key presses and adjusts GameGUI attributes depending on the presses """

        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False
            if event.type == KEYDOWN:
                if event.key in self.key_moves.keys():
                    self.move_direction = self.key_moves[event.key]
                else:
                    self.move_direction = None

            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None
            ...

    def _process_game_logic(self):
        """ Implements character moves and checks if player has reached the exit """
        #self.game.move_character(self.player, self.move_direction)
        self.player.move(self.move_direction)
        self.move_direction = None

    def _draw(self):
        """draw background first then characters"""
        self.screen.fill(WHITE)
        self._draw_background()
        self._draw_characters()
        pygame.display.flip()

    def _draw_background(self):
        x, y = self.game.dimensions
        """Loop through all the game backgrounds and draw a rectangle of the appropriate colour"""
        for obj in self.game.background:
            colour = BACKGROUND_COLORS[obj.name]
            x, y = self._convert_position(obj.pos)

            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)

            pygame.draw.rect(self.screen, colour, rect)




    def _draw_characters(self):
        """Loop through the characters and draw a circle for each character"""
        for character in self.game.characters:
            x, y = self._convert_position(character.pos, center=True)
            pygame.draw.circle(self.screen, center=(x, y), radius=SQUARE_SIZE//2, color=PLAYER_COLOR)

if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()