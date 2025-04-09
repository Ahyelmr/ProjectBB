import tkinter as tk
import customtkinter as ctk
from CredentialsWindow import CredentialsFrame
from MainWindow import MainFrame
from KitchenWindow import MainKitchenFrame
from backend.LoadItems import *
from frontend.CustomerView import CustomerTopLevel
from frontend.EditSKUWindow import EditSKUFrame
from frontend.InventoryView import MainInventoryFrame
from frontend.OrderView import OrderFrame
from frontend.UserWindow import UserFrame

def main():
    app = MainApplication()
    app.mainloop()

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.order_number = 0
        self.user = ""

        self.sku = export_sku(resource_path("Information/SKU.txt"))
        self.inventory = export_inventory(resource_path("Information/InventoryList.txt"))
        self.title("ProjectBB")
        self.maxsize(1920, 1080)
        self.geometry("1444x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.customer_window = CustomerTopLevel(self)

        self.frames = {}

        for F in (MainFrame, CredentialsFrame, MainKitchenFrame, UserFrame, MainInventoryFrame, OrderFrame, EditSKUFrame):
            frame = F(self)
            self.frames[F.__name__] = frame

        self.login = None
        self.user_admin = None

        self.show_frame("MainFrame")

    def show_frame(self, page):
        frame = self.frames[page]
        if frame:
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()

        if page == "CredentialsFrame":
            frame.set_credentials_label()

        if page == "UserFrame":
            frame.set_user_label()
            frame.show_edit_sku()

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_sku(self):
        return self.sku

    def set_sku(self, sku_inventory):
        self.sku = sku_inventory

    def get_number(self):
        return self.order_number

    def add_number(self):
        self.order_number += 1

    def print_skus(self):
        items = self.sku.get_items()
        for item in items:
            print(item.get_name())

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_user_admin(self):
        return self.user_admin

    def set_user_admin(self, user_admin):
        self.user_admin = user_admin

    def add_preparing_list(self):
        self.customer_window.preparing_frame.insert(tk.END)

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

if __name__ == '__main__':
    main()
