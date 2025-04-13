"""
Order.py

This file contains the order class
"""

# This is the main order class which contains items purchased and total amount
class Order:
    def __init__(self, number): # Initializes class
        self.number = number
        self.order_items = []
        self.total_price = 0

    # Gets order number
    def get_number(self):
        return self.number

    # Sets order number
    def set_number(self, number):
        self.number = number

    # Adds an item to the order
    def add_item(self, item):
        self.order_items.append(item)

    # Computes the total amount from items ordered
    def compute_total_price(self):
        self.total_price = 0
        for item in self.order_items:
            self.total_price += item.get_price()

    # Gets the total price of the order
    def get_total_price(self):
        self.compute_total_price()
        return self.total_price

    # Sets the total price of the order
    def get_order_items(self):
        return self.order_items

