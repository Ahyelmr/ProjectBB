from PIL import Image, ImageTk
import tkinter as tk
import customtkinter as ctk

from backend import FilePathing


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.logo = Image.open(FilePathing.resource_path("Assets/BigBoyzLogo.png"))

        #self.configure(bg="yellow")

        self.logoLabel = ctk.CTkLabel(self, text = " ", image=ctk.CTkImage(self.logo, size = (500, 500)), width = 500, height = 500)
        self.logoLabel.pack(padx = 10, pady = 10)

        self.MainLabel = ctk.CTkLabel(self, text="Project BB")
        self.MainLabel.pack(padx = 10, pady = 10)

        self.WelcomeLabel = ctk.CTkLabel(self, text="Welcome")
        self.WelcomeLabel.pack(padx = 10, pady = 10)

        self.SignupButton = ctk.CTkButton(self,text="Sign Up", command=lambda: self.on_signup_click())
        self.SignupButton.pack(side = tk.LEFT, expand = True, padx = 10, pady = 10)

        self.LoginButton = ctk.CTkButton(self, text="Login", command=lambda: self.on_login_click())
        self.LoginButton.pack(side = tk.LEFT, expand = True, padx = 10, pady = 10)

    def on_signup_click(self):
        print("Sign Up button clicked")  # Debugging
        self.parent.set_login(False)  # Set login state for registration
        print(f"Login state after signup: {self.parent.get_login()}")  # Debugging
        self.parent.show_frame("CredentialsFrame")


    def on_login_click(self):
        print("Login button clicked")  # Debugging
        self.parent.set_login(True)  # Set login state for login
        print(f"Login state after login: {self.parent.get_login()}")  # Debugging
        self.parent.show_frame("CredentialsFrame")
