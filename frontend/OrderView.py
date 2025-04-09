import customtkinter as ctk
from frontend.CustomerView import OrdersFrame

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

        self.preparing_frame.customer_list.bind("<Double-1>", self.double_click_order)

        self.return_button = ctk.CTkButton(self, text="Return")

    def double_click_order(self):
        index = self.preparing_frame.customer_list.curselection()
        if index:
            selected_item = self.preparing_frame.customer_list.get(index)
            self.parent.parent.add_ready_list(selected_item, index)
            print(f"Double-Clicked on {selected_item}")