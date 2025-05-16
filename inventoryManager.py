from product import *;
from exception import ProductNotFoundError;

class InsufficientInventoryError(Exception):
    def __init__ (self, msg):
        super().__init__(msg);

class InventoryManager:

    __inventory = dict(); # key:product value: total

    @staticmethod
    def finalizeOrder(cart: Cart):
        if(type(cart) != Cart):
            raise ValueError("Wrong input data type");
        try:
            tempInv = InventoryManager.__inventory;
            for(items in cart.list_items):
                removeProduct(items.product, items.quantity);
            cart.clear();
        except:
            InventoryManager.__inventory = tempInv;
            raise;

    @staticmethod
    def addProduct(product: Product, amount: int):
        try:
            InventoryManager.__validateInput(product, amount)
            InventoryManager.__inventory[product] += amount;
            # print(f'Add {product.name} by {amount}. Total {stockLevel["total"]}');

        except KeyError: #add new product
            InventoryManager.__inventory[product] = amount;
            # print(f'Add new product {product.name}. Amount: {amount}');

        except:
            raise;        

    @staticmethod
    def removeProduct(product: Product, amount: int):
        try:
            InventoryManager.__validateInput(product, amount)
            stockLevel = InventoryManager.__getStockLevel(product);
            if(InventoryManager.__inventory[product] < amount):
                raise InsufficientInventoryError("Cannot remove more than what is in the inventory");
            else:
                InventoryManager.__inventory[product] -= amount;
                # print(f'Remove {product.name} by {amount}. Remaining: {InventoryManager.__inventory[product]}');
        except:
            raise;

    @staticmethod
    def __getStockLevel(product: Product):
        if(type(product) != Product):
            raise ValueError("Wrong input data type");

        try:
            return InventoryManager.__inventory[product];

        except KeyError:
            raise ProductNotFoundError(f'{product.name} is not found');

    @staticmethod
    def __validateInput(product: Product, amount: int):
        if type(product) != Product or type(amount) != int:
            raise ValueError("Wrong input data type")

        if amount < 0:
            raise ValueError("The amount cannot be less than 0")


    @staticmethod
    def set(product: Product, amount: int):
        try:
            InventoryManager.__validateInput(product, amount);
            InventoryManager.__inventory[product] = amount;
            # print(f'New total amount: {amount}');

        except KeyError: #add new product
            InventoryManager.__inventory[product] = amount;
            # print(f'Add new product {product.name}. Amount: {amount}');

        except:
            raise;