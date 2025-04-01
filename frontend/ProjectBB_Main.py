import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from CredentialsFrame import CredentialsFrame

def main():
    app = MainApplication()
    app.mainloop()

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ProjectBB")
        self.maxsize(1920, 1080)
        self.geometry("1444x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.login = False

        self.frames = {}

        for F in (MainFrame, CredentialsFrame):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainFrame)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login



class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.logo = Image.open("lcecg.png")
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logoLabel = ttk.Label(self, image=self.logo)
        self.logoLabel.pack(padx = 10, pady = 10)

        self.MainLabel = ttk.Label(self, text="Project BB")
        self.MainLabel.pack(padx = 10, pady = 10)

        self.WelcomeLabel = ttk.Label(self, text="Welcome")
        self.WelcomeLabel.pack(padx = 10, pady = 10)

        self.SignupButton = ttk.Button(self, text="Sign Up", command=self.on_signup_click)
        self.SignupButton.pack(padx = 10, pady = 10)

        self.LoginButton = ttk.Button(self, text="Login", command=self.on_login_click)
        self.LoginButton.pack(padx = 10, pady = 10)

    def on_signup_click(self, event=None):
        self.master.show_frame(CredentialsFrame)
        self.master.set_login(False)

    def on_login_click(self, event=None):
        self.master.show_frame(CredentialsFrame)
        self.master.set_login(True)


if __name__ == '__main__':
    main()
