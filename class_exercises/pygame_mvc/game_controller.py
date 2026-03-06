from game_objects import GameObj, Character
import csv

class Game:
    def __init__(self):
        self.characters = []
        self.background = []
        self.dimensions = None
        self.start = None
        self.exit = None

    def __repr__(self):
        return f"self.characters: {self.characters}\nself.background: {self.background}\nself.dimensions: {self.dimensions}\nstart: {self.start}\nexit: {self.exit}"

    def set_up(self, characters, background):
        self.characters = characters
        self.background = background

    def add_background_object(self, btype, pos, solid):
        self.background.append(GameObj(name=btype, pos=pos, solid=solid))
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
        for cell in sorted(self.background, key=lambda unit: unit.pos):
            print(cell.name)