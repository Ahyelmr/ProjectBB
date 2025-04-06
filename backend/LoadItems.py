import os

from backend.Item import SkuItem
from backend.Sku import Sku

def export_items(filename):
    skuList = Sku()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            items = f.readlines()
            for item in items:
                item_name, item_sku, item_price, item_image = item.strip().split(",")
                curr_item = SkuItem(item_name, item_sku, item_price, item_image)
                skuList.add_item(curr_item)
                print(skuList.get_item(item_name).get_name())

            return skuList


sku = export_items("Information/SKU.txt")