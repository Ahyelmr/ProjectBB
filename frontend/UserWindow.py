import customtkinter as ctk

from frontend.CustomerView import CustomerTopLevel


class UserFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        self.customer_window = CustomerTopLevel(self)

        self.user_label = ctk.CTkLabel(self)
        self.user_label.pack()

        self.kitchen_button = ctk.CTkButton(self, text="Take Order", command=lambda: self.on_kitchen_button_clicked())
        self.kitchen_button.pack()

        self.inventory_button = ctk.CTkButton(self, text="Check Inventory", command=lambda: self.on_inventory_button_clicked())
        self.inventory_button.pack()

        self.edit_sku_button = ctk.CTkButton(self, text="Edit SKU", command=lambda: self.on_edit_sku_button_clicked())
        self.edit_sku_button.pack()

        self.return_button = ctk.CTkButton(self, text="Return to Menu", command=lambda: self.on_return_button_clicked())
        self.return_button.pack()

    def on_return_button_clicked(self):
        self.parent.show_frame("MainFrame")

    def on_kitchen_button_clicked(self):
        self.parent.show_frame("MainKitchenFrame")

    def on_inventory_button_clicked(self):
        self.parent.show_frame("InventoryFrame")

    def on_edit_sku_button_clicked(self):
        self.parent.show_frame("EditSKUFrame")

    def set_user_label(self):
        user = self.parent.get_user()
        print(user)
        self.user_label.configure(text = "Welcome " + user + "!")

    def show_edit_sku(self):
        if self.parent.get_user_admin():
            print(self.parent.get_user_admin())
            self.edit_sku_button.pack()
        else:
            print(self.parent.get_user_admin())
            self.edit_sku_button.pack_forget()