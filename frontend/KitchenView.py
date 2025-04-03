import tkinter as tk
from PIL import Image, ImageTk

from backend.Item import SkuItem


class MainKitchenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.kitchen_frame = KitchenFrame(self)
        self.options_frame = OptionsFrame(self)
        self.kitchen_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.options_frame.grid(row = 0, column = 1, sticky = "nsew")
        self.options_frame.rowconfigure(0, weight = 1)
        self.options_frame.columnconfigure(0, weight = 1)
        self.options_frame.columnconfigure(1, weight = 1)



class KitchenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        #self.text_box = tk.Label(self, text = "Kitchen")
        #self.text_box.grid(row = 0, column = 0, sticky = "nsew")

        #self.canvas = tk.Canvas(self)
        #self.canvas.pack(fill = "both", expand = True, side = tk.LEFT)

        #self.scrollbar = tk.Scrollbar(self, orient = tk.VERTICAL, command = self.canvas.yview)
        #self.scrollbar.pack(fill = tk.Y, side = tk.RIGHT)

        #self.canvas.configure(yscrollcommand = self.scrollbar.set)
        #self.canvas.bind('<Configure>', Lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all"))))

        #size = self.parent.parent.get_sku_inventory.get_size()
        l = 5
        k = 0

        for i in range(l):
            for j in range(5):
                item = self.parent.parent.get_sku_inventory().getIn_item(k)
                item_frame = ItemFrame(self, item)
                item_frame.grid(row = i, column = j, sticky = "nsew")
                k+=1

    def return_screen(self, name):
        self.parent.show_screen(name)


class OptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.text_box = tk.Label(self, text="Kitchen")
        self.text_box.pack(side = tk.TOP)

        self.return_box = tk.Button(self, text = "Return", command = self.return_button_click())
        self.return_box.pack(side = tk.TOP)

    def return_button_click(self, event =  None):
        self.parent.return_screen("MainFrame")

class ItemFrame(tk.Frame):
    def __init__(self, parent, item):
        super().__init__(parent)
        self.parent = parent

        self.item_image = Image.open("Assets/SKU-Inv/" + item.get_image())
        self.item_image = ImageTk.PhotoImage(self.item_image.resize((200, 200)))
        self.item_image_label = tk.Label(self, image = self.item_image)
        self.item_image_label.grid(row = 0, column = 0, sticky = "nsew")

        self.item_name = tk.Label(self, text = item.get_name())
        self.item_name.grid(row = 1, column = 0, sticky = "nsew")

        self.item_price = tk.Label(self, text = item.get_price())
        self.item_price.grid(row = 2, column = 0, sticky = "nsew")

        self.item_button = tk.Button(self, text = "Add")
        self.item_button.grid(row = 3, column = 0, sticky = "nsew")