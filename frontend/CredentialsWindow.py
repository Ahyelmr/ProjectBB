import tkinter as tk
from backend.AuthenticationPack.Authentication import *

class CredentialsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.credentialsLabel = tk.Label(self)
        self.credentialsLabel.pack(side="top", expand=True)

        self.usernameLabel = tk.Label(self, text = "Username")
        self.usernameLabel.pack(expand=True)

        self.usernameEntry = tk.Entry(self)
        self.usernameEntry.pack(expand = True)

        self.passwordLabel = tk.Label(self, text="Password")
        self.passwordLabel.pack(expand=True)

        self.passwordEntry = tk.Entry(self, show="*")
        self.passwordEntry.pack(expand = True)

        self.enterButton = tk.Button(self, text="Enter", command=self.on_enter_button_clicked,font = ("Helvetica", 20))
        self.enterButton.pack(expand = True)

        self.verifyLabel = tk.Label(self)
        self.verifyLabel.pack(expand=True)

        self.returnButton = tk.Button(self, text="Return", command=self.on_return_button_clicked, font = ("Helvetica", 20))
        self.returnButton.pack(side=tk.LEFT, anchor="s", padx=15, pady=15)

    def on_enter_button_clicked(self, event=None):
        print(self.parent.get_login())
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        login = self.parent.get_login()
        if login:
            if user_login(username, password):
                self.set_verify_label("You have logged in successfully!")
                self.open_confirmation_window()
                self.after(100, self.parent.get_login("MainKitchenFrame"))

            else:
                self.set_verify_label("Invalid username or password!")

        else:
            register_user(username, password)
            self.parent.show_frame("MainKitchenFrame")

        if username == "123" and password == "456":
            print("You are logged in")

    def on_return_button_clicked(self, event=None):
        self.parent.show_frame("MainFrame")

    def set_credentials_label(self):
        credentials = self.parent.get_login()
        print(f"Inside set_credentials_label, login state: {credentials}")
        if credentials:
            self.credentialsLabel.configure(text="Log In", font=("Arial", 20), foreground="black")
        else:
            self.credentialsLabel.configure(text="Register New Account", font=("Arial", 20), foreground="black")

    def set_verify_label(self, label):
        self.verifyLabel.configure(text=label)

    def open_confirmation_window(self):
        confirm_box = tk.Toplevel()
        confirm_box.title("Log In")
        confirm_box.resizable(False, False)
        confirm_box.geometry("200x200")

        confirm_login = tk.Label(confirm_box, text="Successfully Logged in!")
        confirm_login.pack(expand=True)

        confirm_button = tk.Button(confirm_box, text="Confirm", command=confirm_box.destroy)
        confirm_button.pack(expand=True)


