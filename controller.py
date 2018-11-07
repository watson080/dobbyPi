try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk

import model
import view

class Controller(object):
    def __init__(self):
        self._root = tk.Tk()
        self._model = model.Model()
        self._view = view.View(self._model, self._root)

    def run(self):
        self._root.title("dobbyPi")
        self._root.deiconify()
        self._root.mainloop()
