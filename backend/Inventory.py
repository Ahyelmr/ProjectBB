"""
Inventory.py

This file contains the inventory class, which contains the inventory of items
of the system
"""

# This is the main class inventory with its functions
class Inventory:
    def __init__(self): # Initializes class
        super().__init__()
        self.inventory_items = []

    # Adds an item to the inventory
    def add_inventory_item(self, item):
        self.inventory_items.append(item)

    # Gets an item from the inventory based on the name
    def get_inventory_item(self, item_name):
        for item in self.inventory_items:
            if item.get_inventory_name() == item_name:
                return item

    # Removes an item from the inventory based on the name
    def remove_inventory_item(self, name):
        for item in self.inventory_items:
            if item.get_inventory_name() == name:
                self.inventory_items.remove(item)

    # Gets the whole inventory list
    def get_inventory_items(self):
        return self.inventory_items

    # Prints the names of the inventory items
    def print_inventory(self):
        for item in self.inventory_items:
            print(item)

    # Gets an item from the inventory based on the index
    def getIn_inventory(self, index):
        return self.inventory_items[index]