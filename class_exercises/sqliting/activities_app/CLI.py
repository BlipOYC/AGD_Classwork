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

    def show_activity_attendees(self):
        activity = input('Enter activity name: ')
        attendees = self.controller.get_activity_attendees(activity)
        for attendee in attendees:
            print(attendee)

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

    def add_participant(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activity = input("Enter activity name: ")
        self.controller.add_participant(first_name, last_name, activity)


if __name__ == '__main__':
    cli = CLI()
    user_input = "placeholder"
    while user_input != "":
        print("Please select an option:")
        print("Show a person's activities: 1")
        print("Show an activity attendees: 2")
        print("Show all people: 3")
        print("Show all activities: 4")
        print("Add a person: 5")
        print("Add an activity: 6")
        print("Add a particular person to an activity: 7")
        print("Quit: press enter")

        user_input = input("Enter your choice: ")

        try:
            match user_input:
                case "1":
                    cli.show_person_activities()
                case "2":
                    cli.show_activity_attendees()
                case "3":
                    cli.show_all_people()
                case "4":
                    cli.show_all_activities()
                case "5":
                    cli.add_person()
                case "6":
                    cli.add_activity()
                case "7":
                    cli.add_participant()
                case _:
                    raise ValueError

            print("\n\n")
        except ValueError:
            if user_input:
                print("Invalid input. Please try again.")
            else:
                print("Exiting program...")