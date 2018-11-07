import os

try:
    import Tkinter as tk
    import tkMessageBox
    import tkFileDialog
except ModuleNotFoundError:
    import tkinter as tk

class View(tk.Frame):
    def __init__(self, model, master=None):
        tk.Frame.__init__(self,master)
        self._model = model
        self._master = master

        self._wif_file_path_name = ""

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self._current_line_number = tk.Entry()
        self._current_line_number.pack( padx=3, pady=3, anchor=tk.W)

        self._seek_button = tk.Button(self._master, text="seek")
        self._seek_button.pack(padx=3, pady=3,anchor=tk.W)

        self._file_name_entry = tk.Entry(width = 60)
        self._file_name_entry.pack(padx=3, pady=3,anchor=tk.W)
        self._file_name_entry.insert(tk.END, self._wif_file_path_name)

        self._read_button = tk.Button(self._master, text="Read", command=self.select_file_from_file_dialog)
        self._read_button.pack(padx=3, pady=3,anchor=tk.W )

    def select_file_from_file_dialog(self):
        self._file_name_entry.delete(0, tk.END)
        self._filetypes = [('wif_file','*.wif')]
        self._initialdir = "./wif"
        self._wif_file_path_name = tkFileDialog.askopenfilename(filetypes=self._filetypes,initialdir=self._initialdir)
        self._file_name_entry.insert(tk.END, self._wif_file_path_name)

        self._model.set_wif_file_path = str(self._wif_file_path_name)
        self._model.convert_wif_lift_plan()