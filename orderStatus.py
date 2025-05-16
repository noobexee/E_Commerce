from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PAIDED = "paided"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"
