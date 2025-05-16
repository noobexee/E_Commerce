from typing import Final;

class Product:
    def __init__ (self, id, name, price):
        self.__ID: Final = id;
        self.__NAME: Final = name;
        self.__PRICE: Final = price;

    @property
    def id(self):
        return self.__ID;
    
    @property
    def name(self):
        return self.__NAME;
    
    @property
    def price(self):
        return self.__PRICE;