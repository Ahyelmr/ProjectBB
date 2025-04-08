class Order:
    def __init__(self, number):
        self.number = number
        self.items = []

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def add_item(self, item):
        self.items.append(item)
