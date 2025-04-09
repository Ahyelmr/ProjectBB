import customtkinter as ctk
import tkinter as tk

class EditSKUFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options_frame = EditOptionsFrame(self)
        self.edit_frame = EditItemFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.options_frame.grid(row=0, column=0, sticky="nsew")
        self.edit_frame.grid(row=0, column=1, sticky="nsew")

class EditOptionsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.add_button = ctk.CTkButton(self, text = "Add SKU")
        self.add_button.pack(side="top", fill="x")
        self.delete_button = ctk.CTkButton(self, text = "Delete SKU")
        self.delete_button.pack(side="top", fill="x")
        self.edit_button = ctk.CTkButton(self, text = "Edit SKU")
        self.edit_button.pack(side="top", fill="x")

class EditItemFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.item_frame_label = ctk.CTkLabel(self, text = "SKU Item")
        self.item_frame_label.pack(side="top", fill="x")

        self.item_image = ctk.CTkLabel(self, text = " ")
        self.item_image.pack(side="top", fill="x")

