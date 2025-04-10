class SkuItem:
    def __init__(self, name, item_sku, price, image, category):
        self.name = name
        self.item_sku = item_sku
        self.price = price
        self.image = image
        self.category = category

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_image(self):
        return self.image

    def get_category(self):
        return self.category

    def get_item_sku(self):
        return self.item_sku

    def set_name(self, name):
        self.name = name

    def set_item_sku(self, item_sku):
        self.item_sku = item_sku

    def set_price(self, price):
        self.price = price

    def set_image(self, image):
        self.image = image

    def set_category(self, category):
        self.category = category

class InventoryItem:
    def __init__(self, inventory_name, inventory_amount, inventory_image):
        self.inventory_name = inventory_name
        self.inventory_image = inventory_image
        self.inventory_amount = inventory_amount

    def get_inventory_name(self):
        return self.inventory_name

    def set_inventory_name(self, inventory_name):
        self.inventory_name = inventory_name

    def get_inventory_image(self):
        return self.inventory_image

    def set_inventory_image(self, inventory_image):
        self.inventory_image = inventory_image

    def get_inventory_amount(self):
        return self.inventory_amount

    def set_inventory_amount(self, inventory_amount):
        self.inventory_amount = inventory_amount
