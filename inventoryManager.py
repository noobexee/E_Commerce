from product import *;
from exception import ProductNotFoundError;

class InsufficientInventoryError(Exception):
    def __init__ (self, msg):
        super().__init__(msg);

class InventoryManager:

    __inventory = dict(); # key:product value: dict {"total", " reserve"}

    @staticmethod
    def addProduct(product: Product, amount: int):
        try:
            InventoryManager.__validateInput(product, amount)
            stockLevel = InventoryManager.__getStockLevel(product);
            stockLevel["total"] += amount;
            InventoryManager.__inventory[product] = stockLevel;
            print(f'Add {product.name} by {amount}. Total {stockLevel["total"]}');

        except ProductNotFoundError: #add new product
            InventoryManager.__inventory[product] = {"total": amount, "reserve": 0};
            print(f'Add new product {product.name}. Amount: {amount}');

        except:
            raise;        

    @staticmethod
    def removeProduct(product: Product, amount: int):
        try:
            InventoryManager.__validateInput(product, amount)
            stockLevel = InventoryManager.__getStockLevel(product);
            if(stockLevel["total"] - stockLevel["reserve"] < amount):
                raise InsufficientInventoryError("Not enough products in inventory");
            else:
                stockLevel["total"] -= amount;
                InventoryManager.__inventory[product] = stockLevel;
                print(f'Remove {product.name} by {amount}. Remaining: {stockLevel["total"]}');
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
            stockLevel = InventoryManager.__getStockLevel(product);

            if(amount < stockLevel["reserve"]):
                raise InsufficientInventoryError('Cannot set to be lower than the reserved amount');
            else:
                stockLevel["total"] = amount;
                InventoryManager.__inventory[product] = stockLevel;
                print(f'New total amount: {stockLevel["total"]}');

        except ProductNotFoundError: #add new product
            InventoryManager.__inventory[product] = {"total": amount, "reserve": 0};
            print(f'Add new product {product.name}. Amount: {amount}');

        except:
            raise;


    
    @staticmethod
    def reserve(product: Product, amount: int):
        try:
            InventoryManager.__validateInput(product, amount);
            stockLevel = InventoryManager.__getStockLevel(product);

            if(stockLevel["total"] - stockLevel["reserve"] < amount):
                raise InsufficientInventoryError('Cannot reserve more than the total amount');
            else:
                stockLevel["reserve"] += amount;
                InventoryManager.__inventory["product"] = stockLevel;
                print(f'New total reserve: {stockLevel["reserve"]}');
        except:
            raise;
        
        
        
    @staticmethod
    def release(product, amount):
        try:
            InventoryManager.__validateInput(product, amount);
            stockLevel = InventoryManager.__getStockLevel(product);

            if(stockLevel["reserve"] < amount):
                raise InsufficientInventoryError('Cannot release more than the reserved amount');
            else:
                stockLevel["reserve"] -= amount;
                InventoryManager.__inventory[product] = stockLevel;
                print(f'Remaining reserve: {stockLevel["reserve"]}');
        except:
            raise;
