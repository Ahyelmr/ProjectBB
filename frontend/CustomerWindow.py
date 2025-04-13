"""
CustomerWindow.py

This is the customer top level window which shows all the current orders
being prepared and orders that are ready for pikcup
"""

import tkinter as tk
import customtkinter as ctk

# This is the class that shows the customer view window
class CustomerTopLevel(ctk.CTkToplevel):
    def __init__(self, parent): # Initilaizes class with elements
        super().__init__(parent)
        self.parent = parent
        self.geometry("720x900")
        self.preparing_orders = []
        self.ready_orders = []
        self.parent = parent
        self.title("Customer View")

        self.overall_frame = ctk.CTkFrame(self)
        self.overall_frame.pack(expand=True, fill="both")
        self.preparing_frame = OrdersFrame(self.overall_frame, "Preparing Orders")
        self.preparing_frame.pack(side="left", expand=True, fill="both")
        self.ready_frame = OrdersFrame(self.overall_frame, "Orders Ready")
        self.ready_frame.pack(side="right", expand=True, fill="both")

# This is the frame inside the customer top level which shows the orders
class OrdersFrame(ctk.CTkFrame):
    def __init__(self, parent, name): # Initializes class with elements
        super().__init__(parent)
        self.parent = parent

        self.label = ctk.CTkLabel(self, text = name, font= ("Helvetica", 46, "bold"))
        self.label.pack(side="top", fill="x")

        self.customer_list = tk.Listbox(self, font= ("Helvetica", 46, "bold"))
        self.customer_list.pack(side="top", expand = True, fill="both")
