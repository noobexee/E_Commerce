from discountPolicy import DiscountPolicy
from orderStatus import OrderStatus
import uuid
from typing import Final
from cart import Cart

class Order :
    def __init__(self, items, total_price, discount_policy: DiscountPolicy):
        self.__ITEMS : Final = items
        self.__status = OrderStatus.PENDING
        self.__ID : Final = uuid.uuid4()
        self.total_price = total_price
        self.discount_policy = discount_policy

    def update_status(self, new_status : OrderStatus):
        if not isinstance(new_status, OrderStatus):
            raise ValueError("Invalid status type")
        
        self.__status = new_status

    def get_final_amount(self) -> float:
        return self.discount_policy.apply_discount(self.total_price)

    @property
    def id(self) :
        return self.__ID

    @property
    def orderStatus(self) :
        return self.__status
    
    @property
    def items(self) :
        return self.__ITEMS