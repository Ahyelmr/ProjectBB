from tkinter import ttk
from frontend.AuthenticationPack.Authentication import *

class CredentialsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.credentialsLabel = ttk.Label(self, text="Credentials")

        self.usernameEntry = ttk.Entry(self)
        self.usernameEntry.pack(expand = True)

        self.passwordEntry = ttk.Entry(self)
        self.passwordEntry.pack(expand = True)

        self.enterButton = ttk.Button(self, text="Enter", command=self.on_button_clicked)
        self.enterButton.pack(expand = True)

    def on_button_clicked(self, event=None):
        print(self.parent.get_login())
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        credentials = self.parent.get_login()
        if credentials:
            user_login(username, password)

        else:
            register_user(username, password)
            self.parent.show_frame("MainFrame")

        if username == "123" and password == "456":
            print("You are logged in")