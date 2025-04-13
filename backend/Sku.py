"""
Sku.py

This file contains the Sku class, which contains the list of SKU items
"""

# This is the main Sku class that contains SKU items
class Sku:
    def __init__(self): # initializes class
        super().__init__()
        self.sku = []

    # Adds an SKU item to the list
    def add_item(self, item):
        self.sku.append(item)

    # Removes an SKU item from the list based on its name
    def remove_item(self, name):
        for item in self.sku:
            if item.get_name() == name:
                self.sku.remove(item)

    # Gets the current categories of SKU items in the list
    def get_categories(self) :
        categories = []
        for item in self.sku:
            categories.append(item.get_category())

        unique_categories = list(dict.fromkeys(categories))

        return unique_categories

    # Prints the SKU items
    def print_sku(self):
        for item in self.sku:
            print(item)

    # Gets a specific SKU item based on its name
    def get_item(self, name):
        for item in self.sku:
            if item.get_name() == name:
                return item

    # Gets a specific SKu item based on the index
    def getIn_item(self, index):
        return self.sku[index]

    # Gets all the SKU items
    def get_items(self):
        return self.sku

    # Gets the size of the SKU list
    def get_size(self):
        return len(self.sku)