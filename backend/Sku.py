class Sku:
    def __init__(self):
        super().__init__()
        self.sku = []

    def add_item(self, item):
        self.sku.append(item)

    def remove_item(self, name):
        for item in self.sku:
            if item.get_name() == name:
                self.sku.remove(item)

    def get_categories(self) :
        categories = []
        for item in self.sku:
            categories.append(item.get_category())

        unique_categories = list(dict.fromkeys(categories))

        return unique_categories

    def print_sku(self):
        for item in self.sku:
            print(item)

    def get_item(self, name):
        for item in self.sku:
            if item.get_name() == name:
                return item

    def getIn_item(self, index):
        return self.sku[index]

    def get_items(self):
        return self.sku

    def get_size(self):
        return len(self.sku)