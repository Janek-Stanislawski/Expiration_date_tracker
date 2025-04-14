import tkinter as tk
from tkinter import Entry


class Window:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Expiration date tracker")
        self.window.geometry("500x250")
        self.window["background"] = "#1f9aa1"

        self.button = tk.Button(text="Add Item")
        self.button.place(x=270, y=80)
        self.button.bind("<Button-1>", self.handle_button_press)
        self.button_description = tk.Label(self.window, text="Click this button to add item to tracker", bg="#1f9aa1")
        self.button_description.place(x=30, y=80)
        self.button.bind()

        self.name_entry = Entry(self.window, width=20)
        self.name_entry.place(x=30, y=40)

    def handle_button_press(self, event):
        return

    def main(self):
        return


if __name__ == "__main__":
    Window().window.mainloop()
