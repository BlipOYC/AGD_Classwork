from game_controller import Game


class TextInterface:
    """ Create a text-based interface for the turn-based game."""
    def __init__(self):
        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.game_area = []
        self.running = True
        self.win = False

    def _create_area(self):
        """ Create a list of lists where each [row][col] in self.game_area is given the first letter of the background or character in that grid location. If there is no background or character in a grid location, use the default '.'"""

        max_row = max(obj.pos[0] for obj in self.game.background)
        max_col = max(obj.pos[1] for obj in self.game.background)

        rows = max_row + 1
        cols = max_col + 1

        self.game_area = [["." for _ in range(cols)] for _ in range(rows)]

        for obj in self.game.background:
            r, c = obj.pos
            if obj.name == "F":
                placeholder = "."
            else:
                placeholder = obj.name
            self.game_area[r][c] = placeholder

        pr, pc = self.player.pos
        self.game_area[pr][pc] = "P"


    def _draw_area(self):
        """ Loop through each row, join the characters in that row and print it out 'W' in the grid is replaced by '\u2593' (a gray square), borders of the grid are shown using the unicode box-drawing characters (https://jrgraphix.net/r/Unicode/2500-257F)"""
        self._create_area()

        cols = len(self.game_area[0])

        print("╔" + "═" * cols + "╗")
        for row in self.game_area:
            line = ""
            for cell in row:
                if cell == "W":
                    line += "\u2593"
                else:
                    line += cell
            print("│" + line + "│")
        print("╚" + "═" * cols + "╝")


    def _handle_input(self):
        choice = input("Enter N,E,W or S to move (Q to Quit): ").upper()
        if choice == "Q":
            self.running = False

        new_pos = self.player.find_next_move(choice)

        if new_pos:
            self.game.move_character(self.player, new_pos)
            if new_pos == self.game.find_objects_by_name("E")[0].pos:
                running = False
                self.win = True



    def main_loop(self):
        """Keep drawing the area and asking for player moves while self.running is True."""
        print("Welcome to the Maze Game")
        while self.running:
            self._draw_area()
            self._handle_input()


if __name__ == "__main__":
    tui = TextInterface()
    tui.main_loop()

