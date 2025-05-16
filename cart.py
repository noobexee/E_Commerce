from cartItem import CartItem

class Cart:
    def __init__(self):
        self.items = {}  # key: product.id, value: CartItem

    def add_item(self, product, quantity, inventory_manager):
        try:
            inventory_manager.reserve(product.id, quantity)
        except Exception as e:
            print(f"[Add] {e}")
            return False

        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product, quantity)
        return True

    def remove_item(self, product, quantity, inventory_manager):
        if product.id not in self.items:
            print(f"{product.name} not in cart.")
            return False

        cart_item = self.items[product.id]
        if quantity >= cart_item.quantity:
            inventory_manager.release(product.id, cart_item.quantity)
            del self.items[product.id]
        else:
            cart_item.quantity -= quantity
            inventory_manager.release(product.id, quantity)
        return True

    def total_price(self):
        return sum(item.total_price() for item in self.items.values())

    def list_items(self):
        return list(self.items.values())

    def clear(self, inventory_manager=None):
        if inventory_manager:
            for item in self.items.values():
                inventory_manager.release(item.product.id, item.quantity)
        self.items.clear()
