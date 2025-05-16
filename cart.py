from cartItem import CartItem
from inventoryManager import InventoryManager
from exception import ProductNotFoundError;

class Cart:
    def __init__(self):
        self.items = {}  # key: product, value: CartItem

    @staticmethod
    def __validateInput(product: Product, quantity: int):
        if(type(product) != Product or type(quantity) != int):
            raise ValueError("Wrong input data type");
        
        if(quantity < 0):
            raise ValueError("The amount cannot be less than 0");

    def add_item(self, product: Product, quantity: int):
        try:
            Cart.__validateInput(product, quantity)
            InventoryManager.removeProduct(quantity);
            if product in self.items:
                cart_item = self.items[product]
                cart_item.addQuantity(quantity)
            else:
                self.items[product] = CartItem(product, quantity)
        except:
            raise;

    def remove_item(self, product: Product, quantity: int):
        try:
            Cart.__validateInput(product, quantity);
            if product not in self.items:
                raise ProductNotFoundError(f"{product.name} is not in cart.");
            cart_item = self.items[product]
            cart_item.removeQuantity(quantity)
            if(cart_item.quantity == 0):
                del self.items[product];
            InventoryManager.addProduct(quantity);
        except:
            raise;

    def total_price(self):
        return sum(item.total_price() for item in self.items.values())

    def list_items(self):
        return list(self.items.values())

    def clear_cart(self): #clear by return all items
        for item in self.items.values():
            InventoryManager.addProduct(item.product, item.quantity);
        self.items.clear()

    def clear(self): #clear after finished with cart
        self.items.clear()
