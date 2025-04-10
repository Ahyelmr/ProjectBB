import tkinter as tk
import customtkinter as ctk
from PIL import Image
from backend.FilePathing import resource_path
from backend.Order import Order

class MainKitchenFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options_frame = OptionsFrame(self)
        self.kitchen_frame = KitchenFrame(self, self.parent.get_sku().get_items())
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.kitchen_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.options_frame.grid(row = 0, column = 1, sticky = "nsew")

    def add_order(self, item):
        self.options_frame.add_to_list(item.get_name(), item.get_price())
        print(item.get_name() + " " + str(item.get_price()))

    def set_kitchen_items(self, items):
        for widget in self.kitchen_frame.winfo_children():
            widget.destroy()
        self.kitchen_frame.set_item_frames(items)
        self.kitchen_frame.grid(row = 0, column = 0, sticky = "nsew")

class KitchenFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, items):
        super().__init__(parent)

        self.parent = parent

        self.set_item_frames(items)

    def set_item_frames(self, items):
        size = len(items)
        cols = 5
        rows = (size + cols - 1) // cols
        k = 0
        for i in range(rows):
            for j in range(cols):
                self.grid_rowconfigure(i, weight=1)
                self.grid_columnconfigure(j, weight=1)
                if k < size:
                    item = items[k]
                    item_frame = ItemFrame(self, item)
                    item_frame.grid_rowconfigure(i, weight=1)
                    item_frame.grid_columnconfigure(j, weight=1)
                    item_frame.grid(row = i, column = j, sticky = "nsew", padx = 2.5, pady=2.5)
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

        self.category_order = ctk.CTkComboBox(self.organize_frame, values=self.parent.parent.get_sku().get_categories())
        self.category_order.pack(fill="x", pady=10)
        self.category_order.set("Category")

        self.sort_order = ctk.CTkComboBox(self.organize_frame, values=["Name (Ascending)", "Name (Descending)", "Price (Ascending)",  "Price (Descending)"])
        self.sort_order.pack(fill="x", pady=10)
        self.sort_order.set("Order")

        self.sort_button = ctk.CTkButton(self.organize_frame, text="Sort", command=lambda: self.sort_order_click())
        self.sort_button.pack(side="bottom", fill="x", pady=10)

        self.order_list = tk.Listbox(self, font= ("Helvetica", 16, "bold"))
        self.order_list.pack(side = "top", expand=True, fill = "both", pady = 10)

        self.confirm_order_button = ctk.CTkButton(self, text="Confirm Order", command=lambda: self.confirm_order_click())
        self.confirm_order_button.pack(side = "top", expand=True, fill = "x", pady = 10)

        self.return_button = ctk.CTkButton(self, text="Return", command=lambda: self.return_button_click())
        self.return_button.pack(side="top", fill="x", pady=10)

    def return_button_click(self):
        self.parent.parent.show_frame("UserFrame")

    def add_to_list(self, name, price):
        order = str(name) + ", " + str(price)
        if order:
            self.order_list.insert(tk.END, order)
            self.order_list.see(tk.END)

    def confirm_order_click(self):
        order = Order(self.parent.parent.get_number())
        for i in range(self.order_list.size()):
            name = self.order_list.get(i).split(", ")[0]
            item = self.parent.parent.get_sku().get_item(name)
            order.add_item(item)

        order_confirmation = OrderTopLevel(self, order)
        order_confirmation.deiconify()

        #if order_confirmation.get_confirm_purchase():


    def sort_order_click(self):
        category = self.category_order.get()
        sort = self.sort_order.get()
        new_items = []
        print(category, sort)
        for i in self.parent.parent.get_sku().get_items():
            if i.get_category() == category:
                new_items.append(i)
        if sort == "Name (Ascending)":
            new_items.sort(key = lambda item: item.get_name())
        elif sort == "Name (Descending)":
            new_items.sort(key = lambda item: item.get_name(), reverse = True)
        elif sort == "Price (Ascending)":
            new_items.sort(key = lambda item: item.get_price())
        elif sort == "Price (Descending)":
            new_items.sort(key = lambda item: item.get_price(), reverse = True)

        for i in new_items:
            print(i.get_name())

        self.parent.set_kitchen_items(new_items)


class ItemFrame(ctk.CTkFrame):
    def __init__(self, parent, item):
        super().__init__(parent)
        self.parent = parent

        self.item_image = Image.open(resource_path("Assets/SKU-Inv/" + item.get_image()))
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

class OrderTopLevel(ctk.CTkToplevel):
    def __init__(self, parent, order):
        super().__init__(parent)
        self.title("Confirm Purchase")
        self.resizable(False, False)
        self.geometry("200x200")
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        self.parent = parent
        self.order = order

        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)


        self.total = self.order.get_total_price()
        self.confirm_purchase = None
        self.confirm_text = ctk.CTkLabel(self, text = "Confirm Purchase", font=("Helvetica", 18, "bold"))
        self.confirm_text.pack(side = "top", fill = "x")
        self.total_label = ctk.CTkLabel(self, text = ("Total: " + str(self.total)))
        self.total_label.pack(side = "top", fill = "x")
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount")
        self.amount_entry.pack(side = "top", fill = "x")
        self.change_label = ctk.CTkLabel(self)
        self.confirm_button = ctk.CTkButton(self, text = "confirm", command=lambda: self.on_confirm_button_click())
        self.confirm_button.pack(side = "top", fill = "x")
        self.destroy_button = ctk.CTkButton(self, command=self.destroy)

    def on_confirm_button_click(self):
        amount = float(self.amount_entry.get())
        if amount < self.total:
            self.change_label.configure(text = "Not enough amount")
            self.change_label.pack(side = "top", fill = "x")
            self.set_confirm_purchase(False)
        if amount > self.total:
            change = amount - self.total
            self.change_label.configure(text = "Change: " + str(change))
            self.change_label.pack(side = "top", fill = "x")
            self.destroy_button.configure(text = "Confirm Purchase")
            self.destroy_button.pack(side = "top", fill = "x")
            self.set_confirm_purchase(True)
            self.parent.parent.parent.add_number()
            self.parent.parent.parent.add_preparing_list(self.order)
            self.parent.order_list.delete(0, tk.END)

    def set_confirm_purchase(self, value):
        self.confirm_purchase = value

    def get_confirm_purchase(self):
        return self.confirm_purchase

