import pyinputplus as pyip
from fontTools.misc.textTools import hexStr

from controller import Controller


class CLI:
    def __init__(self):
        self.viewing_post = None
        self.controller = Controller()
        self.current_menu = self.login
        self.running = True
        self.run_menus()

    @staticmethod
    def show_title(title):
        print('\n' + title)
        print('-' * len(title) + '\n')

    def run_menus(self):
        while self.running:
            self.current_menu = self.current_menu()

    def exit_menus(self):
        self.running = False
        print("Goodbye")

    def login(self):
        self.show_title('Login Screen')
        users = self.controller.get_user_names()
        menu_items = ['Login',
                      'Create a new account',
                      'Exit',
                       ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select user or create a new account\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'create a new account':
            next_menu = self.create_account
        elif menu_choice.lower() == 'exit':
            next_menu = self.exit_menus
        else:
            user_name = input('Enter your name: ')
            if user_name in users:
                self.controller.set_current_user_from_name(user_name)
                next_menu = self.user_home
            else:
                print(f'Name: "{user_name.title()}" not recognised')
                next_menu = self.login
        return next_menu

    def create_account(self):
        self.show_title('Create Account')
        name = input("Enter your name: ")
        if name in self.controller.get_user_names():
            print("Your name is already taken, try and log in instead")
            return self.login
        else:
            age = None
            while not isinstance(age, int):
                age = input("Enter your age: ")
                try:
                    age = int(age)
                except ValueError:
                    print("Invalid age")

            genders = [
                'Male',
                'Female',
                'Other',
                'Professional',
                'Prefer not to say',
            ]
            gender_choice = pyip.inputMenu(genders,
                                           prompt='Select gender\n',
                                           numbered=True,)
            if gender_choice == "Prefer not to say":
                gender = None
            else:
                gender = gender_choice
            nationality = input("Enter your nationality: ")
            self.controller.make_user(name, age, gender, nationality)
        self.controller.set_current_user_from_name(name)
        return self.user_home

    def user_home(self):
        user_name = self.controller.get_user_name()
        self.show_title(f'User Home - {user_name.title()}')
        menu_item = ['Create posts',
                     'View posts',
                     'See profile',
                     'Exit',]
        menu_choice = pyip.inputMenu(menu_item,
                                     prompt='What would you like to do?\n',
                                     numbered=True,)

        if menu_choice.lower() == 'create posts':
            next_menu = self.create_posts
        elif menu_choice.lower() == 'view posts':
            next_menu = self.view_posts
        elif menu_choice.lower() == 'see profile':
            next_menu = self.see_profile
        elif menu_choice.lower() == 'exit':
            next_menu = self.login
        else:
            next_menu = self.user_home
        return next_menu

    def create_posts(self):
        self.show_title('Create Posts')
        input("Under Construction")
        pass

    def view_posts(self):
        self.show_title('View Posts')
        posts = self.controller.get_post_information()[::-1]

        post_menu = [f"{post['title']}: {post['description']}" for post in posts]
        post_choice = pyip.inputMenu(post_menu,
                                     prompt='What post would you like to see?\n',
                                     numbered=True,)

        self.viewing_post = posts[post_menu.index(post_choice)]['post_id']
        next_menu = self.view_specific_posts
        return next_menu

    def view_specific_posts(self):
        post_information = self.controller.get_specific_post()
        self.show_title(post_information['title'])
        print(post_information['description'])
        for comment in post_information['comments']:
            print(f"Comment {comment['comment']}")
        options = [
            "Return",
            "Leave a comment",
        ]
        option_choice = pyip.inputMenu(options,
                                       numbered=True,)

        if option_choice.lower() == 'return':
            next_menu = self.view_posts
        elif option_choice.lower() == 'leave a comment':
            next_menu = self.leave_comment
        else:
            next_menu = self.view_specific_posts

        return next_menu

    def leave_comment(self):
        pass


    def see_profile(self):
        self.show_title('Profile')
        input("Under Construction")
        pass

if __name__ == '__main__':
    cli = CLI()
    controller = Controller()
