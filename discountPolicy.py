from abc import ABC, abstractmethod

class DiscountPolicy(ABC):
    @abstractmethod
    def apply_discount(self, total_price: float) -> float:
        pass

class FixedAmountDiscount(DiscountPolicy):
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount
    def apply_discount(self, total_price: float) -> float:
        return max(0.0, total_price - self.discount_amount)

class PercentageDiscount(DiscountPolicy):
    def __init__(self, discount_percent: float):
        self.discount_percent = discount_percent
    def apply_discount(self, total_price: float) -> float:
        discount = total_price * (self.discount_percent / 100)
        return max(0.0, total_price - discount)

class FreeShippingDiscount(DiscountPolicy):
    def __init__(self, shipping_cost: float):
        self.shipping_cost = shipping_cost
    def apply_discount(self, total_price: float) -> float:
        return max(0.0, total_price - self.shipping_cost)