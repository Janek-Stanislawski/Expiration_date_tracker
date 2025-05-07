import tkinter as tk
from tkinter import Entry
from tkinter import ttk

background = "#1f9aa1"


def test():
    style = ttk.Style()
    style.configure(
         "Dot.TLabel",
        foreground="Black",
        background=background,
        font=("TkDefaultFont", 40)
        )


class Window:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Expiration date tracker")
        self.window.geometry("500x250")
        self.window["background"] = background

        self.button = tk.Button(text="Add Item")
        self.button_description = tk.Label(self.window, text="Click this button to add item to tracker",
                                           bg=background)

        self.name_entry = Entry(self.window, width=15)
        self.day_entry = Entry(self.window, width=2)
        self.month_entry = Entry(self.window, width=2)
        self.year_entry = Entry(self.window, width=4)

        self.date_entry_label_sep_dot1 = tk.Label(self.window, text=".", bg=background, font=("Helvetica", 15))
        self.date_entry_label_sep_dot2 = tk.Label(self.window, text=".", bg=background, font=("Helvetica", 15))

        self.validation()

    def window1(self):

        self.button.place(x=270, y=80)
        self.button.bind("<Button-1>", self.handle_button_press)

        self.button_description.place(x=30, y=80)
        self.button.bind()

        self.name_entry.place(x=30, y=40)

        self.day_entry.place(x=150, y=40)

        self.month_entry.place(x=175, y=40)

        self.year_entry.place(x=200, y=40)

        self.date_entry_label_sep_dot1.place(x=165, y=35)
        self.date_entry_label_sep_dot1.lower()

        self.date_entry_label_sep_dot2.place(x=190, y=35)
        self.date_entry_label_sep_dot2.lower()



    def validate_numeric_input(self, new_value, max_len):
        return len(new_value) <= int(max_len) and (new_value.isnumeric() or new_value == "")

    def validate_length(self, new_value, max_len):
        return len(new_value) <= int(max_len)

    def validation(self):
        validate_name = (self.window.register(self.validate_length), '%P', '30')
        validate_day = (self.window.register(self.validate_numeric_input), '%P', '2')
        validate_month = (self.window.register(self.validate_numeric_input), '%P', '2')
        validate_year = (self.window.register(self.validate_numeric_input), '%P', '4')

        self.day_entry.config(validate='key', validatecommand=validate_day)
        self.month_entry.config(validate='key', validatecommand=validate_month)
        self.year_entry.config(validate='key', validatecommand=validate_year)
        self.name_entry.config(validate='key', validatecommand=validate_name)


    def handle_button_press(self, event):
        return


if __name__ == "__main__":
    app = Window()
    app.window1()
    app.window.mainloop()
