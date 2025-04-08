class Sku:
    def __init__(self):
        super().__init__()
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, name):
        for item in self.inventory:
            if item.get_name() == name:
                self.inventory.remove(item)

    def get_categories(self) :
        categories = []
        for item in self.inventory:
            categories.append(item.get_category())
            print(item)

        unique_categories = list(dict.fromkeys(categories))
        for yes in unique_categories:
            print(yes)
        return unique_categories

    def get_inventory(self):
        return self.inventory

    def print_inventory(self):
        for item in self.inventory:
            print(item)

    def get_item(self, name):
        for item in self.inventory:
            if item.get_name() == name:
                return item

    def getIn_item(self, index):
        return self.inventory[index]

    def get_items(self):
        return self.inventory

    def get_size(self):
        return len(self.inventory)