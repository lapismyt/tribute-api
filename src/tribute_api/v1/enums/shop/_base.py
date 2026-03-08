from enum import StrEnum


class TributeBillingPeriod(StrEnum):
    ONETIME = "onetime"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    HALFYEARLY = "halfyearly"
    YEARLY = "yearly"


class TributeShopStatus(StrEnum):
    INACTIVE = 0
    ACTIVE = 1


class TributeOrderStatus(StrEnum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


class TributeMemberStatus(StrEnum):
    ACTIVE = "active"
    CANCELLED = "cancelled"


class TributeRefundStatus(StrEnum):
    INITIATED = "initiated"
    COMPLETED = "completed"
