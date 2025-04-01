import tkinter as tk
from tkinter import ttk

class CredentialsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.usernameEntry = ttk.Entry(self)
        self.usernameEntry.pack(side = "top", expand = True)

        self.passwordEntry = ttk.Entry(self)
        self.passwordEntry.pack(side = "top", expand = True)

        self.enterButton = ttk.Button(self, text="Enter", command=self.on_button_clicked)
        self.enterButton.pack(side = "top", expand = True)

    def on_button_clicked(self, event=None):
        print(self.parent.get_login())
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == "123" and password == "456":
            print("You are logged in")
