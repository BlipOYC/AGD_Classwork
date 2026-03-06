class GameObj:
    def __init__(self, name, pos, solid):
        self.name = name
        self.pos = pos
        self.solid = solid

    def __repr__(self):
        return f"GameObj({self.name}, {self.pos}, {self.solid})"

    def is_solid(self):
        return self.solid

class Character(GameObj):
    def __init__(self, name, pos, solid):
        GameObj.__init__(self, name, pos, solid)

    def find_next_move(self, direction):
        row, col = self.pos
        match direction.lower():
            case "north":
                return row - 1, col
            case "south":
                return row + 1, col
            case "east":
                return row, col + 1
            case "west":
                return row, col - 1
            case _:
                return None

    def move(self, game):
        return game.find_next_move(self)

