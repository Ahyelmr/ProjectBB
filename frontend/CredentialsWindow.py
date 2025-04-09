import tkinter as tk
import customtkinter as ctk
from backend.Authentication import *


def open_confirmation_window(label):
    confirm_box = tk.Toplevel()
    confirm_box.title("Log In")
    confirm_box.resizable(False, False)
    confirm_box.geometry("200x150")
    confirm_box.update_idletasks()
    width = confirm_box.winfo_width()
    height = confirm_box.winfo_height()

    x = (confirm_box.winfo_screenwidth() // 2) - (width // 2)
    y = (confirm_box.winfo_screenheight() // 2) - (height // 2)
    confirm_box.geometry(f"{width}x{height}+{x}+{y}")
    confirm_box.focus_force()
    confirm_box.lift()

    confirm_login = tk.Label(confirm_box, text=label)
    confirm_login.pack(expand=True)

    confirm_button = tk.Button(confirm_box, text="Confirm", command=confirm_box.destroy)
    confirm_button.pack(expand=True)


class CredentialsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.credentialsLabel = ctk.CTkLabel(self)
        self.credentialsLabel.pack(side="top", expand=True)

        self.usernameLabel = ctk.CTkLabel(self, text = "Username")
        self.usernameLabel.pack(expand=True)

        self.usernameEntry = ctk.CTkEntry(self)
        self.usernameEntry.pack(expand = True)

        self.passwordLabel = ctk.CTkLabel(self, text="Password")
        self.passwordLabel.pack(expand=True)

        self.passwordEntry = ctk.CTkEntry(self, show="*")
        self.passwordEntry.pack(expand = True)

        self.enterButton = ctk.CTkButton(self, text="Enter", command=lambda: self.on_enter_button_clicked(), font = ("Helvetica", 20))
        self.enterButton.pack(expand = True)

        self.verifyLabel = ctk.CTkLabel(self)
        self.verifyLabel.pack(expand=True)

        self.returnButton = ctk.CTkButton(self, text="Return", command=lambda: self.on_return_button_clicked(), font = ("Helvetica", 20))
        self.returnButton.pack(side=tk.LEFT, anchor="s", padx=15, pady=15)

    def on_enter_button_clicked(self):
        print(self.parent.get_login())
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        login = self.parent.get_login()
        if login:
            if user_login(username, password):
                self.set_verify_label("You have logged in successfully!")
                open_confirmation_window("Successfully Logged In!")
                self.parent.set_user(username)
                self.parent.set_user_admin(check_admin(username, password))
                self.after(100, self.parent.show_frame("UserFrame"))

            else:
                self.set_verify_label("Invalid username or password!")

        else:
            if register_user(username, password):
                self.set_verify_label("You have registered successfully!")
                open_confirmation_window("Successfully Registered!")
                self.after(100, self.parent.show_frame("MainFrame"))
            else:
                self.set_verify_label("User has already been registered!")

    def on_return_button_clicked(self):
        self.parent.show_frame("MainFrame")

    def set_credentials_label(self):
        credentials = self.parent.get_login()
        print(f"Inside set_credentials_label, login state: {credentials}")
        if credentials:
            self.credentialsLabel.configure(text="Log In", font=("Arial", 20))
        else:
            self.credentialsLabel.configure(text="Register New Account", font=("Arial", 20))

    def set_verify_label(self, label):
        self.verifyLabel.configure(text=label)


