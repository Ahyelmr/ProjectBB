import tkinter as tk

class MainKitchenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.kitchen_frame = KitchenFrame(self)
        self.options_frame = OptionsFrame(self)
        self.kitchen_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.options_frame.grid(row = 0, column = 1, sticky = "nsew")
        self.options_frame.rowconfigure(0, weight = 1)
        self.options_frame.columnconfigure(0, weight = 1)



class KitchenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


class OptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

