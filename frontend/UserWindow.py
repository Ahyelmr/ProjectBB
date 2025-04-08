import customtkinter as ctk

class UserFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)

        self.user_label = ctk.CTkLabel(self, text = "User")

        self.kitchen_button = ctk.CTkButton(self, text="Take Order", command=lambda: self.on_kitchen_button_clicked())
        self.kitchen_button.grid(row=0, column=0, sticky="nsew")

        self.inventory_button = ctk.CTkButton(self, text="Check Inventory", command=lambda: self.on_inventory_button_clicked())
        self.inventory_button.grid(row=1, column=0, sticky="nsew")

        self.edit_sku_button = ctk.CTkButton(self, text="Edit SKU")
        self.edit_sku_button.grid(row=2, column=0, sticky="nsew")
        self.edit_sku_button.grid_forget()

        self.return_button = ctk.CTkButton(self, text="Return to Menu", command=lambda: self.on_return_button_clicked())
        self.return_button.grid(row=3, column=0, sticky="nsew")

    def on_return_button_clicked(self):
        self.parent.show_frame("MainFrame")

    def on_kitchen_button_clicked(self):
        self.parent.show_frame("MainKitchenFrame")

    def on_inventory_button_clicked(self):
        self.parent.show_frame("InventoryFrame")
