"""
Item.py

Contains individual SkuItem and Item classes for the system
"""

# This is the class that defines a singular SKU item
class SkuItem:
    # Initializes class
    def __init__(self, name, item_sku, price, image, category):
        self.name = name
        self.item_sku = item_sku
        self.price = price
        self.image = image
        self.category = category

    # Gets SKU item name
    def get_name(self):
        return self.name

    # Gets SKU item price
    def get_price(self):
        return self.price

    # Gets SKU item image name
    def get_image(self):
        return self.image

    # Gets SKU item cateory
    def get_category(self):
        return self.category

    # Gets SKU item SKU code
    def get_item_sku(self):
        return self.item_sku

    # Sets SKU item name
    def set_name(self, name):
        self.name = name

    # Sets SKU item SKU code
    def set_item_sku(self, item_sku):
        self.item_sku = item_sku

    # Sets SKU item price
    def set_price(self, price):
        self.price = price

    # Sets SKU item image name
    def set_image(self, image):
        self.image = image

    # Sets SKU item category
    def set_category(self, category):
        self.category = category

# This is the class that defines a singular inventory item
class InventoryItem:
    # Initializes class
    def __init__(self, inventory_name, inventory_amount, inventory_image):
        self.inventory_name = inventory_name
        self.inventory_image = inventory_image
        self.inventory_amount = inventory_amount

    # Gets inventory name
    def get_inventory_name(self):
        return self.inventory_name

    # Sets inventory name
    def set_inventory_name(self, inventory_name):
        self.inventory_name = inventory_name

    # Gets inventory image name
    def get_inventory_image(self):
        return self.inventory_image

    # Sets inventory image name
    def set_inventory_image(self, inventory_image):
        self.inventory_image = inventory_image

    # Gets inventory amount
    def get_inventory_amount(self):
        return self.inventory_amount

    # Sets inventory amount
    def set_inventory_amount(self, inventory_amount):
        self.inventory_amount = inventory_amount
