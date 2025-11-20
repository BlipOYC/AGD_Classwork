import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.title = tk.Label(self, text="Temperature Converter", font=("Arial", 20))
        self.u_from = tk.Label(self, text="From:")

        self.temperatures_from = [("°C", "Celsius"),
                                  ("°F", "Farenheit"),
                                  ("K", "Kelvin"),
                                  ]
        self.selected_temperature = tk.StringVar()
        self.selected_temperature.set("Celsius")
        self.temperature_options = [tk.Radiobutton(self, text=temperature[0],
                                                   value=temperature[1],
                                                   variable=self.selected_temperature,
                                                   )
                                    for temperature in self.temperatures_from]

        self.celsius_return = tk.Label(self, text="°C")
        self.farenheit_return = tk.Label(self, text="°F")
        self.kelvin_return = tk.Label(self, text="K")
        self.celsius_return_box = tk.Label(self, text=" ")
        self.farenheit_return_box = tk.Label(self, text=" ")
        self.kelvin_return_box = tk.Label(self, text=" ")


        self.user_num = tk.StringVar()
        self.user_input = tk.Entry(self, textvariable=self.user_num)



        self.place_widgets()

    def place_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.title.grid(row=0, column=0, sticky="nsew")
        self.u_from.grid(row=1, column=0, sticky=tk.W)
        for idx, radiobutton in enumerate(self.temperature_options):
            radiobutton.grid(row=1 + idx, column=1, sticky=tk.W)

        self.celsius_return.grid(row=1, column=2, sticky=tk.W)
        self.farenheit_return.grid(row=2, column=2, sticky=tk.W)
        self.kelvin_return.grid(row=3, column=2, sticky=tk.W)

        self.celsius_return_box.grid(row=1, column=3, sticky=tk.W)
        self.farenheit_return_box.grid(row=2, column=3, sticky=tk.W)
        self.kelvin_return_box.grid(row=3, column=3, sticky=tk.W)

        self.user_input.grid(row=4, column=0, sticky="nsew", columnspan=2)

if __name__ == '__main__':
    root = tk.Tk()
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()