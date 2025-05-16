from product import *;

class InsufficientInventoryError(Exception):
    def __init__ (self, msg):
        super().__init__(msg);

class ProductNotFoundError(Exception):
    def __init__ (self, msg):
        super().__init__(msg);

class InventoryManager:

    __inventory = dict();

    @staticmethod
    def validateInput(product, amount):
        if(type(product) != Product or type(amount) != int):
            raise ValueError("Wrong input data type");
        
        if(amount < 0):
            raise ValueError("The amount cannot be less than 0");

    @staticmethod
    def set(product, amount):
        try:
            InventoryManager.validateInput(product, amount);
        except:
            raise;

        try:
            stockLevel = InventoryManager.__inventory[product];
        except KeyError:
            InventoryManager.__inventory[product] = {"total": amount, "reserve": 0};
            print(f'Add new product {product.name}. Amount: {amount}');
            return;

        if(amount < stockLevel["reserve"]):
            raise InsufficientInventoryError('Cannot set to be lower than the reserved amount');
        else:
            stockLevel["total"] = amount;
            __inventory[product] = stockLevel;
            print(f'Success! New total amount: {stockLevel["total"]}');
    
    @staticmethod
    def reserve(product, amount):
        try:
            InventoryManager.validateInput(product, amount);
        except:
            raise;
        
        try:
            stockLevel = InventoryManager.__inventory[product];
        except KeyError:
            raise ProductNotFoundError(f'{product.name} is not found');
        
        if(stockLevel["total"] - stockLevel["reserve"] < amount):
            raise InsufficientInventoryError('Cannot reserve more than the total amount');
        else:
            stockLevel["reserve"] += amount;
            InventoryManager.__inventory["product"] = stockLevel;
            print(f'New total reserve: {stockLevel["reserve"]}');
        
    @staticmethod
    def release(product, amount):
        try:
            InventoryManager.validateInput(product, amount);
        except:
            raise;
        
        try:
            stockLevel = InventoryManager.__inventory[product];
        except KeyError:
            raise ProductNotFoundError(f'{product.name} is not found');

        if(stockLevel["reserve"] < amount):
            raise InsufficientInventoryError('Cannot release more than the reserved amount');
        else:
            stockLevel["reserve"] -= amount;
            InventoryManager.__inventory[product] = stockLevel;
            print(f'Remaining reserve: {stockLevel["reserve"]}');