import tkinter as tk
import customtkinter as ctk

class CustomerTopLevel(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.preparing_orders = []
        self.ready_orders = []
        self.parent = parent
        self.title = "Customer Orders"

        self.overall_frame = ctk.CTkFrame(self)
        self.overall_frame.pack(expand=True, fill="both")
        self.preparing_frame = OrdersFrame(self.overall_frame, "Preparing Orders")
        self.preparing_frame.pack(side="left", expand=True, fill="both")
        self.ready_frame = OrdersFrame(self.overall_frame, "Orders Ready")
        self.ready_frame.pack(side="right", expand=True, fill="both")

class OrdersFrame(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.parent = parent

        self.label = ctk.CTkLabel(self, text = name)
        self.label.pack(side="top", fill="x")

        self.customer_list = tk.Listbox(self)
        self.customer_list.pack(side="top", expand = True, fill="both")
