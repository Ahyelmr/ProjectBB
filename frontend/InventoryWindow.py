"""
InventoryWindow.py

This file is responsible for handling the current inventory in the system.
"""

import customtkinter as ctk
from PIL import Image
from FilePathing import resource_path

# This is the main inventory frame that contains all other sub frames and their functions
class MainInventoryFrame(ctk.CTkFrame):
    def __init__(self, parent): # Initializes class with elements
        super().__init__(parent)
        self.parent = parent
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 3)
        self.inventory_frame = InventoryItemsFrame(self)
        self.inventory_label = ctk.CTkLabel(self, text = "Inventory Management", font = self.parent.get_main_font())
        self.inventory_label.grid(row = 0, column = 0, sticky = "nsew")

        self.return_button = ctk.CTkButton(self, text = "Return", command=lambda: self.on_return_button_clicked(),
                                           font = self.parent.get_main_font())
        self.return_button.grid(row = 0, column = 1, sticky = "ns")

        self.inventory_frame.grid(row=1, column=0, sticky="nsew", columnspan = 2)
        self.inventory_frame.set_inventory_frames(self.parent.get_inventory().get_inventory_items())

    # Returns to the user window frame
    def on_return_button_clicked(self):
        self.parent.show_frame("UserFrame")

# This is the class which contains the items in the inventory of the system
class InventoryItemsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent): # Initializes class with elements
        super().__init__(parent)
        self.parent = parent

    # Sets the inventory frames from the inventory in the system
    def set_inventory_frames(self, items):
        size = len(items)
        cols = 7
        rows = (size + cols - 1) // cols
        k = 0
        for i in range(rows):
            for j in range(cols):
                self.grid_rowconfigure(i, weight = 1)
                self.grid_columnconfigure(j, weight = 1)
                if k < size:
                    item = items[k]
                    item_frame = InventoryFrame(self, item)
                    item_frame.grid(row = i, column = j, sticky = "nsew")
                    k+=1
                else:
                    break

# This is the individual frame that contains an item from the inventory
class InventoryFrame(ctk.CTkFrame):
    def __init__(self, parent, item): # Initializes class with elements
        super().__init__(parent)
        self.parent = parent

        self.item_image = Image.open(resource_path("Assets/InventoryPics/" + item.get_inventory_image()))
        self.item_image_label = ctk.CTkLabel(self, text = " ", image = ctk.CTkImage(self.item_image, size = (200, 200)))
        self.item_image_label.grid(row = 0, column = 0, sticky = "nsew")

        self.item_name = ctk.CTkLabel(self, text = item.get_inventory_name(), font = self.parent.parent.parent.get_sub_font())
        self.item_name.grid(row = 1, column = 0, sticky = "nsew")

        self.item_amount = ctk.CTkLabel(self, text = (item. get_inventory_amount() + " Pcs."), font = self.parent.parent.parent.get_sub_font())
        self.item_amount.grid(row = 2, column = 0, sticky = "nsew")

        self.item_field = ctk.CTkEntry(self, placeholder_text="Change Amount", font = self.parent.parent.parent.get_sub_font())
        self.item_field.grid(row = 3, column = 0, sticky = "nsew")

        self.set_amount_button = ctk.CTkButton(self, text = "Set Amount", command=lambda: self.on_set_amount_button_click(), font = self.parent.parent.parent.get_sub_font())
        self.set_amount_button.grid(row = 4, column = 0, sticky = "nsew")

    # Sets the current amount of the inventory item
    def on_set_amount_button_click(self):
        amount = int(self.item_field.get())
        inventory_item = self.parent.parent.parent.get_inventory().get_inventory_item(self.item_name.cget("text"))
        inventory_item.set_inventory_amount(amount)
        self.item_amount.configure(text = (str(amount) + " Pcs."), font = self.parent.parent.parent.get_sub_font())