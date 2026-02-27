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

    def set_background_from_file(self, background_file):
        pass

    def check_collision(self):
        pass

    def get_cell_contents(self, pos):
        valid_objects = []
        for cell in self.background:
            if cell.pos == pos:
                valid_objects.append(cell)
        return valid_objects

    def move_character(self, character, pos):
        pass

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
        match direction.lower():
            case "north":
                return self.pos[0], self.pos[1] + 1
            case "east":
                return self.pos[0] + 1, self.pos[1]
            case "south":
                return self.pos[0], self.pos[1] - 1
            case "west":
                return self.pos[0] - 1, self.pos[1]
            case _:
                return None

    def move(self):
        pass

