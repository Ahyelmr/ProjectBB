import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.logo = Image.open("Assets/lcecg.png")
        self.logo = ImageTk.PhotoImage(self.logo)
        self.configure(bg="yellow")

        self.logoLabel = tk.Label(self, image=self.logo)
        self.logoLabel.pack(padx = 10, pady = 10)

        self.MainLabel = tk.Label(self, text="Project BB")
        self.MainLabel.pack(padx = 10, pady = 10)

        self.WelcomeLabel = tk.Label(self, text="Welcome")
        self.WelcomeLabel.pack(padx = 10, pady = 10)

        self.SignupButton = tk.Button(self,text="Sign Up", command=self.on_signup_click)
        self.SignupButton.pack(side = tk.LEFT, expand = True, padx = 10, pady = 10)

        self.LoginButton = tk.Button(self, text="Login", command=self.on_login_click)
        self.LoginButton.pack(side = tk.LEFT, expand = True, padx = 10, pady = 10)

    def on_signup_click(self, event=None):
        self.parent.show_frame("CredentialsFrame")
        self.parent.set_login(False)


    def on_login_click(self, event=None):
        self.parent.show_frame("CredentialsFrame")
        self.parent.set_login(True)