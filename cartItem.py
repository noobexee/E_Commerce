from product import Product
from exception import InsufficientQuantityError, InvalidQuantityError

class CartItem:
    def __init__(self, product: Product, quantity: int):
        if(type(product) != Product or type(quantity) != int):
            raise ValueError("Wrong input data type")
        if quantity <= 0:
            raise InvalidQuantityError("Initial quantity must be greater than 0.")
            
        self._product = product
        self._quantity = quantity

    def removeQuantity(self, quantity: int):
        if(type(quantity) != int):
            raise ValueError("Wrong input data type")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity to remove must be positive.")
        if quantity > self._quantity:
            raise InsufficientQuantityError("Not enough quantity in cart to remove.")

        self._quantity -= quantity
        print(f"Successfully remove {quantity} {self._product.name} to CartItem")

    def addQuantity(self, quantity: int):
        if(type(quantity) != int):
            raise ValueError("Wrong input data type")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity to add must be positive.")

        self._quantity += quantity
        print(f"Successfully add {quantity} {self._product.name} to CartItem")
   
    def total_price(self):
        return self.product.price * self.quantity

    def copy(self):
        return CartItem(self.product, self.quantity)
    
    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity
    