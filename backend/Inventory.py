class Inventory:
    def __init__(self):
        super().__init__()
        self.inventory_items = []

    def add_inventory_item(self, item):
        self.inventory_items.append(item)

    def get_inventory_item(self, item_name):
        for item in self.inventory_items:
            if item.get_inventory_name() == item_name:
                return item

    def remove_inventory_item(self, name):
        for item in self.inventory_items:
            if item.get_inventory_name() == name:
                self.inventory_items.remove(item)

    def get_inventory_items(self):
        return self.inventory_items

    def print_inventory(self):
        for item in self.inventory_items:
            print(item)

    def getIn_inventory(self, index):
        return self.inventory_items[index]