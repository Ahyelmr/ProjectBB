"""
LoadItems.py

This file is responsible for file handling in the system
It adds/deletes/reads from different files connected in the system
"""

import os
from FilePathing import resource_path
from backend.Inventory import Inventory
from backend.Item import SkuItem, InventoryItem
from backend.Sku import Sku

# This function exports the details of the SKU list
def export_sku(filename):
    skuList = Sku()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            items = f.readlines()
            for item in items:
                item_name, item_sku, item_price, item_image, item_category = item.strip().split(",")
                curr_item = SkuItem(item_name, item_sku, float(item_price), item_image, item_category)
                skuList.add_item(curr_item)
                print(skuList.get_item(item_name).get_name())

            return skuList

# This function exports the details of the inventory list
def export_inventory(filename):
    inventory = Inventory()
    if os.path.exists(filename):
        with open(resource_path(filename), "r") as f:
            items = f.readlines()
            for item in items:
                item_name, item_amount, item_image = item.strip().split(",")
                curr_item = InventoryItem(item_name, item_amount, item_image)
                inventory.add_inventory_item(curr_item)

            return inventory

# This function creates a file that does not exist yet
def create_file(filename, value):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(value)

# This function adds a line to an existing file
def add_to_file(filename, value):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(value)

    else:
        with open(filename, "rb") as f:  # Open in binary mode to detect newlines exactly
            f.seek(-1, os.SEEK_END)  # Move to the last byte of the file
            last_char = f.read(1)  # Read the last byte

            # If the last character is a newline, don't add another
            if last_char != b'\n':
                with open(filename, "a") as f_append:
                    f_append.write("\n" + value)
            else:
                with open(filename, "a") as f_append:
                    f_append.write(value)

# This function deletes a specific line from a file
def delete_from_file(filename, value):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(value)

    else:
        with open(filename, "r") as f:
            items = f.readlines()
        with open(filename, "w") as f:
            for item in items:
                if item.strip() and not item.startswith(value):
                    f.write(item)

# This file compiles the reports from orders completed
def get_report(filename):
    report = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            report = f.readlines()

    return report