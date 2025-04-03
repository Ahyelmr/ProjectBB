class Item:
    def __init__(self, name, sku, price, image):
        self.name = name
        self.sku = sku
        self.price = price
        self.image = image + ".png"

    def get_name(self):
        return self.name

    def get_category(self):
        return self.sku

    def get_price(self):
        return self.price

    def get_image(self):
        return self.image

    def set_name(self, name):
        self.name = name

    def set_sku(self, sku):
        self.sku = sku

    def set_price(self, price):
        self.price = price

    def set_image(self, image):
        self.image = image
