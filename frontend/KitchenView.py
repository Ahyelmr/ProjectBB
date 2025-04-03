import tkinter as tk

class MainKitchenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.kitchen_frame = KitchenFrame(self)
        self.options_frame = OptionsFrame(self)



class KitchenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


class OptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

