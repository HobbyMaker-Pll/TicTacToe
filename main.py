import tkinter as tk
import json
from tkinter import messagebox
from events import Game


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()

    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('+{}+{}'.format(x, y))


def main():
    with open('Dependencies/config.json') as table_config:
        gameConfiguration = json.load(table_config)

    title = gameConfiguration["windowTitle"]
    root = tk.Tk()
    root.iconbitmap("Dependencies/game.ico")
    root.resizable(False, False)
    root.title(title)
    root.configure(bg="black")

    Game(root, gameConfiguration)
    center(root)

    messagebox.showinfo("Welcome !",
                        '       This game was created by: Victor Pillon'
                        '\n                               Have fun! ☻'
                        '\n\n ( You can change settings by editing config.json ) ')


if __name__ == "__main__":
    main()
    tk.mainloop()
