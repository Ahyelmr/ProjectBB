import tkinter as tk
import customtkinter as ctk

class CustomerTopLevel(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.preparing_orders = []
        self.ready_orders = []
        self.parent = parent




class OrdersFrame(ctk.CTkFrame):
    def __init__(self, parent, order):
        super().__init__(parent)
        self.parent = parent
        self.order = order

