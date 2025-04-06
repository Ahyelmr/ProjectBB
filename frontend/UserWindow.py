import customtkinter as ctk

class UserFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
