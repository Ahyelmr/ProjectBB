class SkuItem:
    def __init__(self, name, sku, price, image, category):
        self.name = name
        self.sku = sku
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

    def set_name(self, name):
        self.name = name

    def set_sku(self, sku):
        self.sku = sku

    def set_price(self, price):
        self.price = price

    def set_image(self, image):
        self.image = image

    def set_category(self, category):
        self.category = category

class MenuItem:
    def __init__(self, name, image):
        self.name = name
        self.image = image
    def get_name(self):
        return self.name