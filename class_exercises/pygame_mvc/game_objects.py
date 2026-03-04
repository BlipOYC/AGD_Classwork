import csv
class Game:
    def __init__(self):
        self.characters = []
        self.background = []
        self.dimensions = None
        self.start = None
        self.exit = None

    def set_up(self, characters, background):
        self.characters = characters
        self.background = background

    def add_background_object(self, btype, pos):
        self.background.append(GameObj(name=btype, pos=pos))
        self.background = sorted(self.background, key=lambda obj: obj.pos)

    def set_background_from_file(self, background_file):
        with open(background_file, mode='r') as file:
            csvFile = csv.reader(file)
            for i, row in enumerate(csvFile):
                for j, obj in enumerate(row):
                    solid = obj == "W"
                    self.add_background_object(obj, (i, j), solid)


    def check_collision(self, pos):
        for obj in self.get_cell_contents(pos):
            if obj.is_solid():
                return True
        return False

    def get_cell_contents(self, pos):
        valid_objects = []
        for cell in self.background:
            if cell.pos == pos:
                valid_objects.append(cell)
        return valid_objects

    def move_character(self, character, new_pos):
        if not self.check_collision(new_pos):
            character.pos = new_pos

    def find_objects_by_name(self, name):
        valid_objects = []
        for cell in self.background:
            if cell.name == name:
                valid_objects.append(cell)
        return valid_objects

    def show_game_grid(self):
        for cell in sorted(self.background, key=lambda cell: cell.pos):
            pass


class GameObj:
    def __init__(self, name, pos, solid):
        self.name = name
        self.pos = pos
        self.solid = solid

    def __str__(self):
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

