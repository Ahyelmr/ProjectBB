"""
ProjectBB_Main.py

This is the main file where the program is run.
"""

import tkinter as tk
import customtkinter as ctk
from frontend.CredentialsWindow import CredentialsFrame
from frontend.MainWindow import MainFrame
from frontend.KitchenWindow import MainKitchenFrame
from backend.LoadItems import *
from frontend.CustomerWindow import CustomerTopLevel
from frontend.EditSKUWindow import EditSKUFrame
from frontend.InventoryWindow import MainInventoryFrame
from frontend.OrderWindow import OrderFrame
from frontend.ReportWindow import ReportFrame
from frontend.UserWindow import UserFrame
import datetime

# Function to run the actual application
def main():
    app = MainApplication()
    app.mainloop()

# This is the main custom tkinter CTk object which contains all other windows and frames
class MainApplication(ctk.CTk):
    def __init__(self): # Initializes class with elements
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

        self.frames = {}

        #Initializes different frames based on their name
        for F in (MainFrame, CredentialsFrame, MainKitchenFrame, UserFrame,
                  MainInventoryFrame, OrderFrame, EditSKUFrame, ReportFrame):
            frame = F(self)
            self.frames[F.__name__] = frame

        self.login = None
        self.user_admin = None

        self.show_frame("MainFrame")

    #Shows the corresponding frame based on the name given
    def show_frame(self, name):
        frame = self.frames[name]
        if frame:
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()

        if name == "CredentialsFrame":
            frame.set_credentials_label()

        if name == "UserFrame":
            frame.set_user_label()
            frame.show_edit_sku()

        if name == "ReportFrame":
            frame.report_frame.set_report_frames()

    # Gets the login Boolean value
    def get_login(self):
        return self.login

    # Sets the login Boolean value
    def set_login(self, login):
        self.login = login

    # Gets the whole SKU of the application
    def get_sku(self):
        return self.sku

    # Sets the whole SKU of the application
    def set_sku(self, sku_inventory):
        self.sku = sku_inventory

    # Gets the current order number of the system
    def get_number(self):
        return self.order_number

    # Increments order number of the system
    def add_number(self):
        self.order_number += 1

    # Gets the current user logged in the system
    def get_user(self):
        return self.user

    # Sets the current user logged in the system
    def set_user(self, user):
        self.user = user

    # Gets the Boolean value to check if current user is an admin
    def get_user_admin(self):
        return self.user_admin

    # Sets the Boolean value to check if current user is an admin
    def set_user_admin(self, user_admin):
        self.user_admin = user_admin

    # Adds an order to the preparing list
    def add_preparing_list(self, order):
        order_label = "#" + str(order.get_number())
        #for item in order.get_order_items():
            #order_label += (", " + item.get_name())
        self.customer_window.preparing_frame.customer_list.insert(tk.END, order_label)
        self.customer_window.preparing_orders.append(order)
        self.frames["OrderFrame"].preparing_frame.customer_list.insert(tk.END, order_label)
        self.frames["OrderFrame"].preparing_orders.append(order)

    # Adds an order from the preparing list to the ready list
    def add_ready_list(self, order, index):
        print(index)
        order_label = "#" + str(order.get_number())
        #for item in order.get_order_items():
           # order_label += (", " + item.get_name())
        self.customer_window.ready_frame.customer_list.insert(tk.END, order_label)
        self.customer_window.ready_orders.append(order)
        self.frames["OrderFrame"].ready_frame.customer_list.insert(tk.END, order_label)
        self.frames["OrderFrame"].ready_orders.append(order)

        self.customer_window.preparing_frame.customer_list.delete(index)
        self.customer_window.preparing_orders.remove(order)
        self.frames["OrderFrame"].preparing_orders.remove(order)
        self.frames["OrderFrame"].preparing_frame.customer_list.delete(index)

    # Adds an order from the ready list to the report view
    def add_order_report(self, order, index):
        order_label = str(order.get_number())
        for item in order.get_order_items():
            order_label += (", " + item.get_name())
        add_to_file(resource_path(self.daily_report_file), order_label)
        self.customer_window.ready_frame.customer_list.delete(index)
        self.customer_window.ready_orders.remove(order)
        self.frames["OrderFrame"].ready_frame.customer_list.delete(index)
        self.frames["OrderFrame"].ready_orders.remove(order)

    # Gets the inventory of the system
    def get_inventory(self):
        return self.inventory

    # Sets the inventory of the system
    def set_inventory(self, inventory):
        self.inventory = inventory

    # Gets the main font used in the elements' text
    def get_main_font(self):
        return self.main_font

    # Gets the sub font used in the elements' text
    def get_sub_font(self):
        return self.sub_font

# Runs the application through the main method
if __name__ == '__main__':
    main()
