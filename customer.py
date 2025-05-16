from cart import Cart
from order import Order
from discountPolicy import DiscountPolicy
from inventoryManager import InventoryManager

class Customer:

    def __init__(self, name):
        self.__NAME = name
        self.cart = Cart()

    @property
    def name(self):
        return self.__NAME
    
    def place_order(self, discount_policy: DiscountPolicy = None):
        for item in self.cart.list_items():
            InventoryManager.removeProduct(item.product, item.quantity)
        order = Order(self.cart.items.copy(), self.cart.total_price(), discount_policy)
        self.cart.clear()
        return order
