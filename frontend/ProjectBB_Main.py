import tkinter as tk
from tkinter import font

import customtkinter as ctk
from CredentialsWindow import CredentialsFrame
from MainWindow import MainFrame
from KitchenWindow import MainKitchenFrame
from backend.LoadItems import *
from frontend.CustomerWindow import CustomerTopLevel
from frontend.EditSKUWindow import EditSKUFrame
from frontend.InventoryWindow import MainInventoryFrame
from frontend.OrderWindow import OrderFrame
from frontend.ReportWindow import ReportFrame
from frontend.UserWindow import UserFrame
import datetime

def main():
    app = MainApplication()
    app.mainloop()

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.daily_report_file = "Records/" + str(datetime.datetime.now().strftime("%Y_%m_%d")) + ".txt"
        print(self.daily_report_file)
        create_file(resource_path(self.daily_report_file), str(datetime.datetime.now().strftime("%Y_%m_%d")))
        self._set_appearance_mode("dark")
        self.title("ProjectBB")
        self.maxsize(1920, 1080)
        self.geometry("1444x900")

        self.order_number = 1
        self.user = ""

        self.sku = export_sku(resource_path("Information/SKU.txt"))
        self.inventory = export_inventory(resource_path("Information/InventoryList.txt"))

        self.main_font = ("Helvetica", 36, "bold")
        self.sub_font = ("Helvetica", 14, "bold")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.customer_window = CustomerTopLevel(self)
        self.customer_window.withdraw()

        self.frames = {}

        for F in (MainFrame, CredentialsFrame, MainKitchenFrame, UserFrame,
                  MainInventoryFrame, OrderFrame, EditSKUFrame, ReportFrame):
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
            self.customer_window.deiconify()

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

    def add_preparing_list(self, order):
        order_label = str(order.get_number())
        for item in order.get_order_items():
            order_label += (", " + item.get_name())
        self.customer_window.preparing_frame.customer_list.insert(tk.END, order_label)
        self.customer_window.preparing_orders.append(order)
        self.frames["OrderFrame"].preparing_frame.customer_list.insert(tk.END, order_label)
        self.frames["OrderFrame"].preparing_orders.append(order)

    def add_ready_list(self, order, index):
        print(index)
        order_label = str(order.get_number())
        for item in order.get_order_items():
            order_label += (", " + item.get_name())
        self.customer_window.ready_frame.customer_list.insert(tk.END, order_label)
        self.customer_window.ready_orders.append(order)
        self.frames["OrderFrame"].ready_frame.customer_list.insert(tk.END, order_label)
        self.frames["OrderFrame"].ready_orders.append(order)

        self.customer_window.preparing_frame.customer_list.delete(index)
        self.customer_window.preparing_orders.remove(order)
        self.frames["OrderFrame"].preparing_orders.remove(order)
        self.frames["OrderFrame"].preparing_frame.customer_list.delete(index)

    def add_order_report(self, order, index):
        order_label = str(order.get_number())
        for item in order.get_order_items():
            order_label += (" " + item.get_name())
        add_to_file(resource_path(self.daily_report_file), order_label)
        self.customer_window.ready_frame.customer_list.delete(index)
        self.customer_window.ready_orders.remove(order)
        self.frames["OrderFrame"].ready_frame.customer_list.delete(index)
        self.frames["OrderFrame"].ready_orders.remove(order)


    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_main_font(self):
        return self.main_font

    def get_sub_font(self):
        return self.sub_font


if __name__ == '__main__':
    main()
