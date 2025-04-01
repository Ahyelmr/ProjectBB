import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from frontend.CredentialsView import CredentialsWindow

def main():
    app = MainApplication()
    app.mainloop()

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ProjectBB")
        self.maxsize(1920, 1080)
        self.geometry("1920x1080")
        self.configure(background="#efefef")

        frame = MainFrame(self)
        frame.place(relx = 0.5, rely = 0.3, anchor = "center")

class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.logo = Image.open("lcecg.png")
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logoLabel = ttk.Label(self, image=self.logo)
        self.logoLabel.grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = 10)

        self.MainLabel = ttk.Label(self, text="Project BB")
        self.MainLabel.grid(column=0, row=1, sticky="ew", padx=10, pady=10)

        self.WelcomeLabel = ttk.Label(self, text="Welcome")
        self.WelcomeLabel.grid(column=0, row=2, sticky="ew", padx=10, pady=10)

if __name__ == '__main__':
    main()
