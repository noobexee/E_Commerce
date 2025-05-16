from cart import Cart
from order import Order
from discountPolicy import DiscountPolicy

class Customer:

    def __init__(self, name):
        self.__NAME = name
        self.cart = Cart()

    @property
    def name(self):
        return self.__NAME
    
    def place_order(self, discount=None):
        order = Order(self, self.cart.items, discount)
        self.cart.clear()
        return order
