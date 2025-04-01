import tkinter as tk
from CredentialsWindow import CredentialsFrame
from MainWindow import MainFrame

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

        self.frames = {}

        for F in (MainFrame, CredentialsFrame):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.login = False

        self.show_frame("MainFrame")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_mainStyle(self):
        return self.mainStyle

    def get_subStyle(self):
        return self.subStyle

if __name__ == '__main__':
    main()
