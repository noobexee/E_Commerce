from cart import Cart
from order import Order

class Customer:

    def __init__(self, name):
        self.__NAME = name
        self.cart = Cart()

    @property
    def name(self):
        return self.__NAME
    
    def place_order(self, inventory_manager):
        order = Order(self, self.cart.items)
        self.cart.clear()
        return order
