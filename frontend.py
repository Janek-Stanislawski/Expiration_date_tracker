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
        self.button.place(x=270, y=80)
        self.button.bind("<Button-1>", self.handle_button_press)
        self.button_description = tk.Label(self.window, text="Click this button to add item to tracker",
                                           bg=background)
        self.button_description.place(x=30, y=80)
        self.button.bind()

        self.name_entry = Entry(self.window, width=15)
        self.name_entry.place(x=30, y=40)
        self.day_entry = Entry(self.window, width=2)
        self.day_entry.place(x=150, y=40)
        self.month_entry = Entry(self.window, width=2)
        self.month_entry.place(x=175, y=40)
        self.year_entry = Entry(self.window, width=4)
        self.year_entry.place(x=200, y=40)
        self.date_entry_label1 = tk.Label(self.window, text=".", bg=background, font=("Helvetica", 15))
        self.date_entry_label1.place(x=165, y=35)
        self.date_entry_label1.lower()
        self.date_entry_label2 = tk.Label(self.window, text=".", bg=background, font=("Helvetica", 15))
        self.date_entry_label2.place(x=190, y=35)
        self.date_entry_label2.lower()

    def handle_button_press(self, event):
        return

    def main(self):
        return


if __name__ == "__main__":
    Window().window.mainloop()
