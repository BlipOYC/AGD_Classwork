import tkinter as tk
from random import choice

class ClickApp(tk.Tk):
    """ Button clicker application """

    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()

        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.clicker_frame.pack(side=tk.LEFT)


class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)
        self.txt1 = tk.Label(self, text = "My clicker app", bg = "darkslategrey", fg = "white")
        self.btn = tk.Button(self, text = "Something?", bg = "seagreen2", fg = "white", command = self.click_button)
        self.response_txt = tk.Label(self, text = "No clicks", bg = "goldenrod", fg = "white")
        self.last_pressed = tk.Label(self, text = "Last pressed", bg = "light green", fg = "white")
        self.counter = 0
        self.place_widgets()

        self.config(bg = "snow")

    def click_button(self):
        self.counter += 1
        self.response_txt.config(text = self.counter)

    def on_key_press(self, event):
        print("You pressed: ", event.keysym)
        self.last_pressed.config(text = f"Last pressed: {event.keysym}")

    def place_widgets(self):
        settings = {"padx": 10, "pady": 10, "sticky": "nswe"}
        self.txt1.grid(column = 0, row = 0, **settings)
        self.btn.grid(column=0, row=1, **settings)
        self.response_txt.grid(column=0, row=2, **settings)
        self.last_pressed.grid(column=0, row=3, **settings)


class BackgroundColorFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        # Color choices
        self.colors = ["Choose a colour", "Any colour"]

        # Create a tk variable which will hold the value of the selected color
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color)
                              for color in self.colors]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        color = "#" + "".join([choice("0123456789ABCDEF") for i in range(6)])
        self.config(bg = color)
        self.app.config(bg=color)
        self.app.clicker_frame.config(bg=color)

if __name__ == '__main__':
    app = ClickApp()
    b_f = BackgroundColorFrame(app)
    b_f.pack(side=tk.TOP)
    app.mainloop()