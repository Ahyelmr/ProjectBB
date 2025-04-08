import tkinter as tk
import customtkinter as ctk
from CredentialsWindow import CredentialsFrame
from MainWindow import MainFrame
from KitchenWindow import MainKitchenFrame
from backend.LoadItems import *
from backend import FilePathing
import os
from backend.Sku import *
from frontend.InventoryView import InventoryFrame
from frontend.UserWindow import UserFrame

print("Current directory: ", os.getcwd())

def main():
    app = MainApplication()
    app.mainloop()

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.sku_inventory = export_items(FilePathing.resource_path("Information/SKU.txt"))
        self.title("ProjectBB")
        self.maxsize(1920, 1080)
        self.geometry("1444x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (MainFrame, CredentialsFrame, MainKitchenFrame, UserFrame, InventoryFrame):
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

    def get_sku_inventory(self):
        return self.sku_inventory

    def set_sku_inventory(self, sku_inventory):
        self.sku_inventory = sku_inventory

    def print_skus(self):
        items = self.sku_inventory.get_items()
        for item in items:
            print(item.get_name())

if __name__ == '__main__':
    main()
