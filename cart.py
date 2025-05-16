from cartItem import CartItem
from inventoryManager import InventoryManager

class Cart:
    def __init__(self):
        self.items = {}  # key: product.id, value: CartItem

    def add_item(self, product, quantity):
        try:
            InventoryManager.reserve(product.id, quantity)
        except Exception as e:
            print(f"[Add] {e}")
            return False

        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product, quantity)
        return True

    def remove_item(self, product, quantity):
        if product.id not in self.items:
            print(f"{product.name} not in cart.")
            return False

        cart_item = self.items[product.id]
        if quantity >= cart_item.quantity:
            InventoryManager.release(product.id, cart_item.quantity)
            del self.items[product.id]
        else:
            cart_item.quantity -= quantity
            InventoryManager.release(product.id, quantity)
        return True

    def total_price(self):
        return sum(item.total_price() for item in self.items.values())

    def list_items(self):
        return list(self.items.values())

    def clear_cart(self):
        for item in self.items.values():
            InventoryManager.release_stock(item.product.id, item.quantity)
        self.items.clear()

    def clear(self):
        self.items.clear()
