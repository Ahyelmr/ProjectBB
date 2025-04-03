class Sku:
    def __init__(self):
        super().__init__()
        self.inventory = {}

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory

    def print_inventory(self):
        for item in self.inventory:
            print(item)

    def get_item(self, name):
        for item in self.inventory:
            if item.name == name:
                return item
