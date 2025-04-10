import customtkinter as ctk
from frontend.CustomerWindow import OrdersFrame

class OrderFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.preparing_orders = []
        self.ready_orders = []

        self.overall_frame = ctk.CTkFrame(self)
        self.overall_frame.pack(expand=True, fill="both")
        self.preparing_frame = OrdersFrame(self.overall_frame, "Preparing Orders")
        self.preparing_frame.pack(side="left", expand=True, fill="both")
        self.ready_frame = OrdersFrame(self.overall_frame, "Orders Ready")
        self.ready_frame.pack(side="right", expand=True, fill="both")

        self.preparing_frame.customer_list.bind("<Double-1>", self.double_click_preparing)
        self.ready_frame.customer_list.bind("<Double-1>", self.double_click_ready)

        self.return_button = ctk.CTkButton(self, text="Return", font = self.parent.get_main_font(), command=lambda: self.on_return_button_click())
        self.return_button.pack(side="left", expand=True, fill="both")

    def double_click_preparing(self, event):
        index = self.preparing_frame.customer_list.curselection()[0]
        selected_item = self.preparing_orders[index]
        print(selected_item)
        self.parent.add_ready_list(selected_item, index)
        print(f"Double-Clicked on {selected_item}")

    def double_click_ready(self, event):
        index = self.ready_frame.customer_list.curselection()[0]
        selected_item = self.ready_orders[index]
        self.parent.add_order_report(selected_item, index)

    def on_return_button_click(self):
        self.parent.show_frame("UserFrame")