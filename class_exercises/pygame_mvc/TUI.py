from game_controller import Game


class TextInterface:
    """ Create a text-based interface for the turn-based game."""
    def __init__(self):
        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.game_area = []
        self.running = True

    def _create_area(self):

        pass


    def _draw_area(self):
        """ Loop through each row, join the characters in that row and print it out 'W' in the grid is replaced by '\u2593' (a gray square), borders of the grid are shown using the unicode box-drawing characters (https://jrgraphix.net/r/Unicode/2500-257F)"""
        pass


    def _handle_input(self):
        """Ask the user to input a direction and use game.move_character to move in that direction.
        Set self.running to false if the user enters Q."""
        pass



    def main_loop(self):
        """Keep drawing the area and asking for player moves while self.runnng is True."""
        print("Welcome to the Maze Game")
        while self.running:
            self._draw_area()
            self._handle_input()


if __name__ == "__main__":
    tui = TextInterface()
    tui.main_loop()

