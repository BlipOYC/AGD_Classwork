import tkinter as tk
from tkinter import ttk
COUNTRIES = [
    "USA",
    "Canada",
    "United Kingdom",
    "Australia",
    "Other",
]

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.title = tk.Label(self, text="Registration Form", font=("Arial", 20))
        self.full_name = tk.Label(self, text="Full Name")
        self.enter_name = tk.Entry(self)
        self.email = tk.Label(self, text="Email")
        self.enter_email = tk.Entry(self)
        self.gender = tk.Label(self, text="Gender")
        self.country = tk.Label(self, text="Country")
        self.current_country = tk.StringVar()
        self.country_combo = ttk.Combobox(self, textvariable=self.current_country)
        self.country_combo["values"] = COUNTRIES
        self.country_combo["state"] = "readonly"
        self.programming = tk.Label(self, text="Programming")

        self.submit = tk.Button(self, text="Submit", bg="#005eff", fg="white")

        self.place_widget()

    def place_widget(self):
        ew_settings = {"stick": "EW", "pady": 5}
        settings = {"stick": "W", "padx": 15, "pady": 5}
        self.rowconfigure(0, weight=11)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=11)
        self.columnconfigure(2, weight=1)


        self.title.grid(row=0, column=0, rowspan=2, **ew_settings)
        self.full_name.grid(row=1, column=0,  **settings)
        self.enter_name.grid(row=1, column=1, **ew_settings)
        self.email.grid(row=2, column=0, **settings)
        self.enter_email.grid(row=2, column=1, **ew_settings)
        self.gender.grid(row=3, column=0, sticky=tk.W, **settings)
        self.country.grid(row=4, column=0, sticky=tk.W, **settings)
        self.country_combo.grid(row=4, column=1, sticky=tk.W, **ew_settings)
        self.programming.grid(row=5, column=0, sticky=tk.W, **settings)
        self.submit.grid(row=6, column=0, **settings)

class GenderFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.gender = tk.Label(self, text="Gender")
        self.selected_gender = tk.StringVar()
        self.genders = ("Male", "Female")

        self.place_widget()

    def place_widget(self):
        settings = {"sticky": tk.EW, "padx": 15, "pady": 5}
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=10)

        for idx, gender in enumerate(self.genders):
            r = tk.Radiobutton(self, text=gender, variable=self.selected_gender, value=gender)
            r.focus()
            r.grid(row=0, column=idx + 1, stick=tk.EW)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Registration form")
    root.geometry("500x300")
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    gender_frame = GenderFrame(root)
    gender_frame.place(x=300, y=150)
    root.mainloop()