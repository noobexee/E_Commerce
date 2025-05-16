from cart import Cart
from order import Order
from discountPolicy import DiscountPolicy
from inventoryManager import InsufficientInventoryError, InventoryManager

class Customer:

    def __init__(self, name):
        self.__NAME = name
        self.__cart = Cart()
        self.__orders = list();

    @property
    def name(self):
        return self.__NAME

    @property
    def orders(self):
        return self.__orders;
    
    @property
    def cart(self):
        return self.__cart;
    
    def place_order(self, discount_policy: DiscountPolicy = None):
        try:
            InventoryManager.finalizeOrder(self.__cart.list_items());
            self.__orders.append(Order(self.__cart, discount_policy))
            self.__cart.clear();
        except:
            raise;
