class Product:

    def __init__ (self, id, name, price):
        self.__ID = id;
        self.__NAME = name;
        self.__PRICE = price;

    @property
    def id(self):
        return self.__ID;
    
    @property
    def name(self):
        return self.__NAME;
    
    @property
    def price(self):
        return self.__PRICE;