from controller import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)
        for activity in activities:
            print(activity)

    def show_all_people(self):
        people = self.controller.get_all_people()
        for person in people:
            print(person)

    def show_all_activities(self):
        activities = self.controller.get_all_activities()
        for activity in activities:
            print(activity)

    def add_person(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        self.controller.add_person(first_name, last_name)

    def add_activity(self):
        activity_name = input('Enter activity name: ')
        self.controller.add_activity(activity_name)


if __name__ == '__main__':
    cli = CLI()