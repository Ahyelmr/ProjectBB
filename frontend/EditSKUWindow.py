import os
import shutil

import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

from FilePathing import resource_path, get_app_dir
from backend.Item import SkuItem
from backend.LoadItems import add_to_file, delete_from_file


class EditSKUFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options_frame = EditOptionsFrame(self)
        self.edit_frame = EditItemFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.edit_frame.grid(row=0, column=1, sticky="nsew")
        self.options_frame.grid(row=0, column=0, sticky="nsew")

    def show_edit_item_frame(self):
        self.edit_frame.show_add_item_frame()

    def edit_item_frame_label(self, text):
        self.edit_frame.set_item_frame_label(text)

class EditOptionsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.add_button = ctk.CTkButton(self, text = "Add SKU Item", command=lambda:self.on_add_button_clicked())
        self.add_button.pack(side="top", fill="x", pady=20)
        self.delete_button = ctk.CTkButton(self, text = "Delete SKU Item", command =lambda:self.on_delete_button_clicked())
        self.delete_button.pack(side="top", fill="x", pady=20)
        self.edit_button = ctk.CTkButton(self, text = "Edit SKU")
        self.edit_button.pack(side="top", fill="x", pady=20)

        self.search_entry = ctk.CTkEntry(self, placeholder_text = "Search Item")
        self.search_entry.pack(side="top", fill="x", pady=20)

        self.search_button = ctk.CTkButton(self, text = "Search SKU", command=lambda: self.on_search_button_clicked())
        self.search_button.pack(side="top", fill="x", pady=10)

        self.search_label = ctk.CTkLabel(self, text = " ")
        self.search_label.pack(side="top", fill="x", pady=5)

        self.return_button = ctk.CTkButton(self, text = "Return", command=lambda:self.parent.parent.show_frame("UserFrame"))
        self.return_button.pack(side="top", fill="x", pady=10)

    def on_add_button_clicked(self):
        self.parent.show_edit_item_frame()
        self.configure_search_label(True)
        self.parent.edit_item_frame_label("Add SKU Item")

    def on_delete_button_clicked(self):
        self.parent.edit_item_frame_label("Delete SKU Item")
        item_name = self.search_entry.get()
        print("Item name", item_name)
        self.parent.parent.get_sku().remove_item(item_name)
        delete_from_file(resource_path("Information/SKU.txt"), str(item_name))

    def on_search_button_clicked(self):
        item_name = self.search_entry.get()
        item = self.parent.parent.get_sku().get_item(item_name)
        self.parent.edit_frame.set_item_frame(item)

    def configure_search_label(self, found):
        if not found:
            self.search_label.configure(text="Item not found")
        else:
            self.search_label.forget()


class EditItemFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.image_name = ""
        self.item_frame_label = ctk.CTkLabel(self, text = " ")
        self.item_frame_label.pack(side="top", fill="x")

        self.item_image = ctk.CTkLabel(self, text = "", width = 200, height = 200)
        self.item_image.pack(side="top", fill="x")
        self.item_image_button = ctk.CTkButton(self, text="Add Image", command=lambda: self.on_add_image_button_clicked())

        self.item_name_label = ctk.CTkLabel(self, text = "Name")
        self.item_name_label.pack(side="top", fill="x")
        self.item_name_entry = ctk.CTkEntry(self, width = 20)
        self.item_name_entry.pack(side="top", fill="x")

        self.item_SKU_label = ctk.CTkLabel(self, text = "SKU")
        self.item_SKU_label.pack(side="top", fill="x")
        self.item_SKU_entry = ctk.CTkEntry(self, width = 20)
        self.item_SKU_entry.pack(side="top", fill="x")

        self.item_price_label = ctk.CTkLabel(self, text = "Price")
        self.item_price_label.pack(side="top", fill="x")
        self.item_price_entry = ctk.CTkEntry(self, width = 20)
        self.item_price_entry.pack(side="top", fill="x")

        self.item_category_label = ctk.CTkLabel(self, text = "Category")
        self.item_category_label.pack(side="top", fill="x")
        self.item_category_entry = ctk.CTkEntry(self, width = 20)
        self.item_category_entry.pack(side="top", fill="x")

        self.add_item_button = ctk.CTkButton(self, text = "Confirm Add SKU Item", command=lambda:self.on_add_SKU_button_clicked())

    def set_item_frame_label(self, text):
        self.item_frame_label.configure(text = text)

    def on_add_SKU_button_clicked(self):
        name = self.item_name_entry.get()
        SKU = self.item_SKU_entry.get()
        price = self.item_price_entry.get()
        category = self.item_category_entry.get()
        image = self.get_image_name()
        item = SkuItem(name, SKU, price, image, category)

        self.parent.parent.get_sku().add_item(item)

        item_line_name = name + "," + SKU + "," + price + "," + image + "," + category
        add_to_file(resource_path("Information/SKU.txt"), item_line_name)

    def on_add_image_button_clicked(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        if file_path:
            image = Image.open(file_path)
            ctk_image = ctk.CTkImage(image, size = (300, 300))
            self.item_image.configure(image = ctk_image)
            self.item_image.image=ctk_image

            filename = os.path.basename(file_path)
            print(filename)
            self.set_image_name(filename)
            save_path = os.path.join(os.path.join(get_app_dir(), "Assets", "SKU-Inv"), filename)
            print(save_path)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            shutil.copy(file_path, save_path)
            print(f"Image saved to: {save_path}")

    def set_item_frame(self, item):
        if item is not None:
            item_image = Image.open(resource_path("Assets/SKU-Inv/" + item.get_image()))
            self.item_image.configure(image = ctk.CTkImage(item_image, size=(200,200)))
            self.item_name_label.configure(text = item.get_name())
            self.item_SKU_label.configure(text = item.get_item_sku())
            self.item_price_label.configure(text = item.get_price())
            self.item_category_label.configure(text = item.get_category())
            self.item_image_button.forget()
            self.add_item_button.forget()
            self.item_frame_label.forget()
        else:
            self.parent.options_frame.configure_search_label(False)

    def show_add_item_frame(self):
        self.item_image.configure(image=None)
        self.item_name_label.configure(text="Name")
        self.item_SKU_label.configure(text="SKU")
        self.item_price_label.configure(text="Price")
        self.item_category_label.configure(text="Category")
        self.item_image_button.pack(side="top", fill="x", pady=10)
        self.add_item_button.pack(side="top", fill="x", pady=10)

    def get_image_name(self):
        return self.image_name

    def set_image_name(self, name):
        self.image_name = name


