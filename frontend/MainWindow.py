from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk

class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.mainStyle = ttk.Style()
        self.mainStyle.configure('MainStyle', font=('Helvetica', 24))

        self.subStyle = ttk.Style()
        self.subStyle.configure('SubStyle', font=('Helvetica', 16))

        self.logo = Image.open("Assets/lcecg.png")
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logoLabel = ttk.Label(self, image=self.logo)
        self.logoLabel.pack(padx = 10, pady = 10)

        self.MainLabel = ttk.Label(self, text="Project BB")
        self.MainLabel.pack(padx = 10, pady = 10)

        self.WelcomeLabel = ttk.Label(self, text="Welcome")
        self.WelcomeLabel.pack(padx = 10, pady = 10)

        self.SignupButton = ttk.Button(self,text="Sign Up", command=self.on_signup_click)
        self.SignupButton.pack(side = tk.LEFT, expand = True, padx = 10, pady = 10)

        self.LoginButton = ttk.Button(self, text="Login", command=self.on_login_click)
        self.LoginButton.pack(side = tk.LEFT, expand = True, padx = 10, pady = 10)

    def on_signup_click(self, event=None):
        self.parent.show_frame("CredentialsFrame")
        self.parent.set_login(False)

    def on_login_click(self, event=None):
        self.parent.show_frame("CredentialsFrame")
        self.parent.set_login(True)