import tkinter as tk

from gui import HashCheckerGUI
from database import init_db


if __name__ == "__main__":

    init_db()

    root = tk.Tk()

    app = HashCheckerGUI(root)

    root.mainloop()