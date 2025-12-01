import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from temperature import Temperature

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

        self.celsius_return = tk.Label(self, text="Celsius:")
        self.farenheit_return = tk.Label(self, text="Farenheit:")
        self.kelvin_return = tk.Label(self, text="Kelvin:")

        self.celsius_return_box = tk.Label(self, text="—")
        self.farenheit_return_box = tk.Label(self, text="—")
        self.kelvin_return_box = tk.Label(self, text="—")

        self.calculate_button = tk.Button(self, text="Calculations", command = self.show_calcs, bg = "#EEFEFF")
        self.enter_button = tk.Button(self, text="Enter", command=self.show_values, bg = "#1081F9", activebackground="ivory")


        self.user_num = tk.StringVar()
        self.user_input = tk.Entry(self, textvariable=self.user_num)

        self.temperature_holder = Temperature(0)

        self.place_widgets()

        master.bind("<Return>", lambda event: self.enter_button.invoke())

    def show_values(self):
        current_temperature = self.selected_temperature.get()

        try:
            num = float(self.user_num.get())
            match current_temperature:
                case "Celsius":
                    self.temperature_holder.celsius = num
                case "Farenheit":
                    self.temperature_holder.farenheit = num
                case "Kelvin":
                    self.temperature_holder.kelvin = num

        except ValueError:
            showinfo("Error", "Please enter a valid number.")
            return


        for idx, temp_box in enumerate([self.celsius_return_box, self.farenheit_return_box, self.kelvin_return_box]):
            if ["Celsius", "Farenheit", "Kelvin"][idx] == current_temperature:
                temp_box.config(text = "N/A")
            else:
                match ["Celsius", "Farenheit", "Kelvin"][idx]:
                    case "Celsius":
                        temp_box.config(text = f"{round(self.temperature_holder.celsius, 2)}°C")
                    case "Farenheit":
                        temp_box.config(text = f"{round(self.temperature_holder.farenheit, 2)}°F")
                    case "Kelvin":
                        temp_box.config(text = f"{round(self.temperature_holder.kelvin, 2)}K")

    def calc_message(self):
        message = []
        message.append("Celsius:")
        if self.selected_temperature.get() == "Celsius":
            message.append("This is the temperature of the original measurement.")
        else:
            message.append(f"We turn the original measurement into celsius: {round(self.temperature_holder.celsius, 2)}°C")

        for temperature in ["Farenheit", "Kelvin"]:
            message.append(f"{temperature}:")
            if self.selected_temperature.get() == temperature:
                message.append("This is the temperature of the original measurement.")
            else:
                match temperature:
                    case "Farenheit":
                        message.append(f"{self.temperature_holder.celsius} * 9 / 5 + 32 = {round(self.temperature_holder.farenheit, 2)}°F")
                    case "Kelvin":
                        message.append(f"{self.temperature_holder.celsius} + 273.15 = {round(self.temperature_holder.kelvin, 2)}")
        return "\n".join(message)



    def show_calcs(self):
        showinfo("Calculations", self.calc_message())


    def place_widgets(self):
        settings = {"padx": 10, "pady": 10, "sticky": tk.W}
        for row in range(5):
            self.rowconfigure(row, weight=1)
        
        for col in range(4):
            self.columnconfigure(col, weight=0, uniform="col")

        self.title.grid(row=0, column=0, columnspan=4, **settings)
        self.u_from.grid(row=1, column=0, **settings)
        for idx, radiobutton in enumerate(self.temperature_options):
            radiobutton.grid(row=1 + idx, column=1, **settings)

        self.celsius_return.grid(row=1, column=2, **settings)
        self.farenheit_return.grid(row=2, column=2, **settings)
        self.kelvin_return.grid(row=3, column=2, **settings)

        self.celsius_return_box.grid(row=1, column=3, **settings)
        self.farenheit_return_box.grid(row=2, column=3, **settings)
        self.kelvin_return_box.grid(row=3, column=3, **settings)

        self.user_input.grid(row=4, column=0, columnspan=2, **settings)
        self.calculate_button.grid(row=4, column=2, **settings)
        self.enter_button.grid(row=4, column=3, **settings)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Temperature Converter")
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()