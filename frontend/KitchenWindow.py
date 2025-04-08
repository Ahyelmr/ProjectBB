import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

from backend import FilePathing
from backend.Item import SkuItem
from backend.Order import Order


class MainKitchenFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options_frame = OptionsFrame(self)
        self.kitchen_frame = KitchenFrame(self, self.parent.get_sku_inventory())
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.kitchen_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.options_frame.grid(row = 0, column = 1, sticky = "nsew")

    def add_order(self, item):
        self.options_frame.add_to_list(item.get_name(), item.get_price())
        print(item.get_name() + " " + item.get_price())


class KitchenFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, items):
        super().__init__(parent)

        self.parent = parent

        size = items.get_size()
        print(size)
        l = size//5
        k = 0

        for i in range(l):
            for j in range(5):
                if i+j < size:
                    item = items.getIn_item(k)
                    item_frame = ItemFrame(self, item)
                    item_frame.grid(row = i, column = j, sticky = "nsew")
                    item_frame.grid_rowconfigure(i, weight = 1)
                    item_frame.grid_columnconfigure(j, weight = 1)
                    k+=1
                else:
                    break

class OptionsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.text_box = ctk.CTkLabel(self, text="Kitchen")
        self.text_box.pack(side="top", fill="x", pady=10)

        self.organize_frame = ctk.CTkFrame(self)
        self.organize_frame.pack(side="top", fill="x", pady = 10)

        self.category_order = ctk.CTkComboBox(self.organize_frame, values=self.parent.parent.get_sku_inventory().get_categories())
        self.category_order.pack(fill="x", pady=10)
        self.category_order.set("Category")

        self.sort_order = ctk.CTkComboBox(self.organize_frame, values=["Name (Ascending)", "Name (Descending)", "Price (Ascending)",  "Price (Descending)"])
        self.sort_order.pack(fill="x", pady=10)
        self.sort_order.set("Order")

        self.sort_button = ctk.CTkButton(self.organize_frame, text="Sort", command=lambda: self.sort_order)
        self.sort_button.pack(side="bottom", fill="x", pady=10)

        self.order_list = tk.Listbox(self)
        self.order_list.pack(side = "top", fill = "both", pady = 10)

        self.confirm_order_button = ctk.CTkButton(self, text="Confirm Order")


        self.confirm_order_button = ctk.CTkButton(self, text = "")

        self.return_button = ctk.CTkButton(self, text="Return", command=lambda: self.return_button_click())
        self.return_button.pack(side="top", fill="x", pady=10)

    def return_button_click(self):
        self.parent.parent.show_frame("MainFrame")

    def add_to_list(self, name, price):
        order = str(name) + " " + str(price)
        if order:
            self.order_list.insert(tk.END, order)
            self.order_list.see(tk.END)

    def confirm_order_click(self):
        order = Order(self.parent.parent.get_number())
        for i in range(self.order_list.size()):
            price = self.order_list.get(i).split(" ")[1]

        self.parent.parent.add_number()

    def sort_order_click(self):
        print(1)


class ItemFrame(ctk.CTkFrame):
    def __init__(self, parent, item):
        super().__init__(parent)
        self.parent = parent

        self.item_image = Image.open(FilePathing.resource_path("Assets/SKU-Inv/" + item.get_image()))
        self.item_image_label = ctk.CTkLabel(self, text = " ", image = ctk.CTkImage(self.item_image, size = (200, 200)), width = 200, height = 200)
        self.item_image_label.grid(row = 0, column = 0, sticky = "nsew")

        self.item_name = ctk.CTkLabel(self, text = item.get_name())
        self.item_name.grid(row = 1, column = 0, sticky = "nsew")

        self.item_price = ctk.CTkLabel(self, text = item.get_price())
        self.item_price.grid(row = 2, column = 0, sticky = "nsew")

        self.item_button = ctk.CTkButton(self, text = "Add", command=lambda: self.add_button_click(item))
        self.item_button.grid(row = 3, column = 0, sticky = "nsew")

    def add_button_click(self, item):
        self.parent.parent.add_order(item)