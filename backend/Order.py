class Order:
    def __init__(self, number):
        self.number = number
        self.order_items = []
        self.total_price = 0

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def add_item(self, item):
        self.order_items.append(item)

    def compute_total_price(self):
        self.total_price = 0
        for item in self.order_items:
            self.total_price += item.get_price()

    def get_total_price(self):
        self.compute_total_price()
        return self.total_price

    def get_order_items(self):
        return self.order_items

