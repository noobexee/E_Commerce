from product import Product
from exception import InsufficientQuantityError, InvalidQuantityError


class CartItem:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise InvalidQuantityError("Initial quantity must be greater than 0.")
        self._product = product
        self._quantity = quantity

    def removeQuantity(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity to remove must be positive.")
        if quantity > self._quantity:
            raise InsufficientQuantityError("Not enough quantity in cart to remove.")
        self._quantity -= quantity

    def addQuantity(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity to add must be positive.")
        self._quantity += quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity
