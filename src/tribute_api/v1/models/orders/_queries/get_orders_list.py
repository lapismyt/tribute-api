from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.orders._physical_order import TributePhysicalOrder
from tribute_api.v1.models.products import TributeMeta


class TributePhysicalOrdersListResponse(TributeModel):
    rows: list[TributePhysicalOrder] | None = Field(None)
    meta: TributeMeta | None = Field(None)
