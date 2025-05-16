from orderStatus import OrderStatus
import uuid
from typing import Final

class Order :
    def __init__(self, items):
        self.__ITEMS : Final = items
        self.__status = OrderStatus.PENDING
        self.__ID : Final = uuid.uuid4()

    def update_status(self, new_status : OrderStatus):
        if not isinstance(new_status, OrderStatus):
            raise ValueError("Invalid status type")
        
        self.__status = new_status

    @property
    def id(self) :
        return self.__ID

    @property
    def orderStatus(self) :
        return self.__status
    
    @property
    def items(self) :
        return self.__ITEMS