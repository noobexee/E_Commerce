from discountPolicy import DiscountPolicy
from orderStatus import OrderStatus
import uuid
from typing import Final, Optional
from cart import Cart

class Order :
    def __init__(self, cart: Cart, discount_policy: Optional[DiscountPolicy] = None):
        self.__ITEMS : Final = cart.list_items();
        self.__status = OrderStatus.PENDING
        self.__ID : Final = uuid.uuid4()
        self.__total_price = cart.total_price();
        self.__discount_policy = discount_policy

    def update_status(self, new_status : OrderStatus):
        if not isinstance(new_status, OrderStatus):
            raise ValueError("Invalid status type")
        
        self.__status = new_status

    def update_discountPolicy(self, new_policy : DiscountPolicy):
        if not isinstance(new_policy , DiscountPolicy):
            raise ValueError("Invalid status type")
        
        self.__discount_policy = new_policy 
    

    def get_final_amount(self) -> float:
        return self.__discount_policy.apply_discount(self.__total_price)

    @property
    def id(self) :
        return self.__ID

    @property
    def status(self) :
        return self.__status
    
    @property
    def items(self) :
        return self.__ITEMS
    
    @property
    def totalprice(self) :
        return self.__total_price