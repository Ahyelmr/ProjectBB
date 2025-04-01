import tkinter as tk
from tkinter import ttk

class CredentialsWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.usernameEntry = ttk.Entry(self)
        self.usernameEntry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        self.passwordEntry = ttk.Entry(self)
        self.passwordEntry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.enterButton = ttk.Button(self)
        self.enterButton.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    def on_button_clicked(self, event=None):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == "123" and password == "456":
            print("You are logged in")
