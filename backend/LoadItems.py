import os

from backend.FilePathing import resource_path
from backend.Inventory import Inventory
from backend.Item import SkuItem, InventoryItem
from backend.Sku import Sku

def export_sku(filename):
    skuList = Sku()
    if os.path.exists(resource_path(filename)):
        with open(filename, "r") as f:
            items = f.readlines()
            for item in items:
                item_name, item_sku, item_price, item_image, item_category = item.strip().split(",")
                curr_item = SkuItem(item_name, item_sku, item_price, item_image, item_category)
                skuList.add_item(curr_item)
                print(skuList.get_item(item_name).get_name())

            return skuList

def export_inventory(filename):
    inventory = Inventory()
    if os.path.exists(resource_path(filename)):
        with open(filename, "r") as f:
            items = f.readlines()
            for item in items:
                item_name, item_amount, item_image = item.strip().split(",")
                curr_item = InventoryItem(item_name, item_amount, item_image)
                inventory.add_inventory_item(curr_item)

            return inventory
"""
def add_inventory_item(filename, item):
    if os.path.exists(resource_path(filename)):
        with open(filename, "a") as f:

def edit_sku(filename):
"""