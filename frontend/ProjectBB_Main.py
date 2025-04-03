import tkinter as tk
from CredentialsWindow import CredentialsFrame
from MainWindow import MainFrame
from KitchenView import MainKitchenFrame

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

        for F in (MainFrame, CredentialsFrame, MainKitchenFrame):
            frame = F(self)
            self.frames[F.__name__] = frame


        self.login = None

        self.show_frame("MainFrame")

    def show_frame(self, page):
        frame = self.frames[page]
        if frame:
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()

        if page == "CredentialsFrame":
            frame.set_credentials_label()

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

if __name__ == '__main__':
    main()
