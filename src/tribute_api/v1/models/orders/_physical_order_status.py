from enum import StrEnum


class TributePhysicalOrderStatus(StrEnum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"
    PROCESSING = "processing"
