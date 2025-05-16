from cartItem import CartItem
from inventoryManager import InventoryManager

class Cart:
    def __init__(self):
        self.items = {}  # key: product, value: CartItem

    def add_item(self, product, quantity):
        try:
            InventoryManager.reserve(product, quantity)
        except Exception as e:
            print(f"[Add] {e}")
            return False

        if product in self.items:
            cart_item = self.items[product]
            cart_item.addQuantity(quantity)
        else:
            self.items[product] = CartItem(product, quantity)
        return True

    def remove_item(self, product, quantity):
        if product not in self.items:
            print(f"{product.name} not in cart.")
            return False

        cart_item = self.items[product]
        if quantity >= cart_item.quantity:
            InventoryManager.release(product, cart_item.quantity)
            del self.items[product]
        else:
            cart_item.removeQuantity(quantity)
            InventoryManager.release(product, quantity)
        return True

    def total_price(self):
        return sum(item.total_price() for item in self.items.values())

    def list_items(self):
        return list(self.items.values())

    def clear_cart(self):
        for item in self.items.values():
            InventoryManager.release(item.product, item.quantity)
        self.items.clear()

    def clear(self):
        self.items.clear()
