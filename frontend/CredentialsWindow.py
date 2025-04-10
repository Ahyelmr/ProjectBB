import tkinter as tk
import customtkinter as ctk
from backend.Authentication import *
from PIL import Image


def open_confirmation_window(label, font):
    confirm_box = ctk.CTkToplevel()
    confirm_box.title("Log In")
    confirm_box.configure(fg_color="#fdc30d")
    confirm_box.update_idletasks()
    width = 500
    height = 350

    x = (confirm_box.winfo_screenwidth() // 2) - (width // 2)
    y = (confirm_box.winfo_screenheight() // 2) - (height // 2)
    confirm_box.geometry(f"{width}x{height}+{x}+{y}")
    confirm_box.lift()
    confirm_box.focus_force()
    confirm_box.attributes("-topmost", True)

    confirm_login = ctk.CTkLabel(confirm_box, text=label, font = font, text_color="#1a1a1a")
    confirm_login.pack(expand=True, pady=10)

    confirm_button = ctk.CTkButton(confirm_box, text="Confirm", font = font, command=confirm_box.destroy)
    confirm_button.pack(expand=True, pady=10)


class CredentialsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.configure(fg_color="#fdc30d")

        self.logo = Image.open(resource_path("Assets/BigBoyzLogo.png"))
        self.logoLabel = ctk.CTkLabel(self, text=" ", image=ctk.CTkImage(self.logo, size=(400, 400)),)
        self.logoLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.credentialsLabel = ctk.CTkLabel(self)
        self.credentialsLabel.grid(row=1, column=0, pady=10, sticky="ns")

        self.usernameLabel = ctk.CTkLabel(self, text="Username", font=self.parent.get_main_font())
        self.usernameLabel.grid(row=2, column=0, pady=10, sticky="ns")

        self.usernameEntry = ctk.CTkEntry(self, placeholder_text="Username", font=self.parent.get_main_font(), width = 250)
        self.usernameEntry.grid(row=3, column=0, pady=10, sticky="ns")

        self.passwordLabel = ctk.CTkLabel(self, text="Password", font=self.parent.get_main_font())
        self.passwordLabel.grid(row=4, column=0, pady=10, sticky="ns")

        self.passwordEntry = ctk.CTkEntry(self, placeholder_text="Password", show="*", font=self.parent.get_main_font(), width = 250)
        self.passwordEntry.grid(row=5, column=0, pady=10, sticky="ns")

        self.enterButton = ctk.CTkButton(self, text="Enter", command=lambda: self.on_enter_button_clicked(),
                                         font=self.parent.get_main_font())
        self.enterButton.grid(row=6, column=0, pady=10, sticky="ns")


        self.returnButton = ctk.CTkButton(self, text="Return", command=lambda: self.on_return_button_clicked(),
                                          font=self.parent.get_main_font())

        self.returnButton.grid(row=7, column=0, pady=10, sticky="w", padx=15)

        # Make sure the grid cells expand
        self.grid_rowconfigure(0, weight=3)
        for row in range(1, 8):
            self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def on_enter_button_clicked(self):
        print(self.parent.get_login())
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        login = self.parent.get_login()
        if login:
            if user_login(username, password):
                open_confirmation_window("Successfully Logged In!", self.parent.get_main_font())
                self.parent.set_user(username)
                self.parent.set_user_admin(check_admin(username, password))
                self.usernameEntry.delete(0, "end")
                self.passwordEntry.delete(0, "end")
                self.after(100, self.parent.show_frame("UserFrame"))

            else:
                self.set_verify_label("Invalid username or password!")

        else:
            if register_user(username, password):
                self.set_verify_label("You have registered successfully!")
                open_confirmation_window("Successfully Registered!", self.parent.get_main_font())
                self.usernameEntry.delete(0, "end")
                self.passwordEntry.delete(0, "end")
                self.after(100, self.parent.show_frame("MainFrame"))
            else:
                self.set_verify_label("User has already been registered!")

    def on_return_button_clicked(self):
        self.usernameEntry.delete(0, "end")
        self.passwordEntry.delete(0, "end")
        self.parent.show_frame("MainFrame")

    def set_credentials_label(self):
        credentials = self.parent.get_login()
        print(f"Inside set_credentials_label, login state: {credentials}")
        if credentials:
            self.credentialsLabel.configure(text="Log In", font=self.parent.get_main_font())
        else:
            self.credentialsLabel.configure(text="Register New Account", font=self.parent.get_main_font())