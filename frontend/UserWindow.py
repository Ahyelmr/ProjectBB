import customtkinter as ctk
from PIL import Image
from FilePathing import resource_path


class UserFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="#fdc30d")

        self.logo = Image.open(resource_path("Assets/BigBoyzLogo.png"))

        self.logoLabel = ctk.CTkLabel(self, text=" ", image=ctk.CTkImage(self.logo, size=(400, 400)))
        self.logoLabel.grid(row = 0, column = 0, padx=10, pady=10, sticky="nsew", columnspan = 2)

        self.user_label = ctk.CTkLabel(self)
        self.user_label.grid(row = 1, column = 0, pady=10, sticky="ns", columnspan = 2)

        self.kitchen_button = ctk.CTkButton(self, text="Take Order", command=lambda: self.on_kitchen_button_clicked(),
                                            font = self.parent.get_main_font())
        self.kitchen_button.grid(row = 2, column = 0, pady=10, sticky="ns")

        self.order_button = ctk.CTkButton(self, text="Manage Orders", command=lambda: self.on_order_button_clicked(), font = self.parent.get_main_font())
        self.order_button.grid(row = 2, column = 1, pady=10, sticky="ns")

        self.inventory_button = ctk.CTkButton(self, text="View Inventory", command=lambda: self.on_inventory_button_clicked(), font = self.parent.get_main_font())
        self.inventory_button.grid(row = 3, column = 0, pady=10, sticky="ns")

        self.edit_sku_button = ctk.CTkButton(self, text="Edit SKU", command=lambda: self.on_edit_sku_button_clicked(), font = self.parent.get_main_font())

        self.check_report_button = ctk.CTkButton(self, text = "View Today's Report", command=lambda: self.on_report_button_clicked(), font = self.parent.get_main_font())
        self.check_report_button.grid(row = 3, column = 1, pady=10, sticky="ns")

        self.return_button = ctk.CTkButton(self, text="Return to Menu", command=lambda: self.on_return_button_clicked(), font = self.parent.get_main_font())
        self.return_button.grid(row = 5, column = 0, pady=10, sticky="ns", columnspan=2)

        for row in range(1, 5):
            self.grid_rowconfigure(row, weight=1)

        self.grid_columnconfigure(0, weight= 1)
        self.grid_columnconfigure(1, weight= 1)

    def on_return_button_clicked(self):
        self.parent.show_frame("MainFrame")

    def on_kitchen_button_clicked(self):
        self.parent.show_frame("MainKitchenFrame")

    def on_inventory_button_clicked(self):
        self.parent.show_frame("MainInventoryFrame")

    def on_order_button_clicked(self):
        self.parent.show_frame("OrderFrame")

    def on_edit_sku_button_clicked(self):
        self.parent.show_frame("EditSKUFrame")

    def on_report_button_clicked(self):
        self.parent.show_frame("ReportFrame")

    def set_user_label(self):
        user = self.parent.get_user()
        print(user)
        self.user_label.configure(text = "Welcome " + user + "!", font = self.parent.get_main_font(), text_color="#1a1a1a")

    def show_edit_sku(self):
        if self.parent.get_user_admin():
            print(self.parent.get_user_admin())
            self.edit_sku_button.grid(row = 4, column = 0, pady=10, sticky="ns", columnspan=2)
        else:
            print(self.parent.get_user_admin())
            self.edit_sku_button.grid_forget()