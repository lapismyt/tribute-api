from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums.shop import TributeOrderStatus


class TributeGetShopOrderStatusResponse(TributeModel):
    status: TributeOrderStatus = Field(
        ...,
        description="Order status",
        examples=[TributeOrderStatus.PAID],
    )
