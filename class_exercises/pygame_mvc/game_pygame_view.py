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
    key_moves = {K_UP: 'n',
                 K_DOWN: 's',
                 K_RIGHT: 'e',
                 K_LEFT: 'w',
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
        print(self.player)

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
                if event.key == "W":
                    self.move_direction = "N"
                elif event.key == "A":
                    self.move_direction = "W"
                elif event.key == "D":
                    self.move_direction = "E"
                elif event.key == "S":
                    self.move_direction = "S"
                else:
                    self.move_direction = None

            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None
            ...

    def _process_game_logic(self):
        """ Implements character moves and checks if player has reached the exit """
        self.game.move_character(self.player, self.move_direction)

    def _draw(self):
        """draw background first then characters"""
        self.screen.fill(WHITE)
        self._draw_background()
        self._draw_characters()
        pygame.display.flip()

    def _draw_background(self):
        """Loop through all the game backgrounds and draw a rectangle of the appropriate colour"""
        for obj in self.game.background:
            colour = BACKGROUND_COLORS[obj.name]
            x, y = self._convert_position(obj.pos)
            rect = pygame.Rect(y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

            pygame.draw.rect(self.screen, colour, rect)

        pygame.display.flip()

    def _draw_characters(self):
        """Loop through the characters and draw a circle for each character"""
        #for char in self.game.characters:
        #    x, y = self._convert_position(char.pos, center=True)
        #    pygame.draw.circle(self.screen, center=(x, y), radius=SQUARE_SIZE, color=PLAYER_COLOR)
        x, y = self._convert_position(self.player.pos, center=True)
        pygame.draw.circle(self.screen, center=(x, y), radius=SQUARE_SIZE, color=PLAYER_COLOR)

if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()