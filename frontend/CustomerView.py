import tkinter as tk

class CustomerTopLevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

class CustomerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

