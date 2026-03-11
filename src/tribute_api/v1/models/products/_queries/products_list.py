from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.products._meta import TributeMeta
from tribute_api.v1.models.products._product import TributeProduct


class TributeGetProductsListResponse(TributeModel):
    rows: list[TributeProduct] | None = Field(None)
    meta: TributeMeta | None = Field(None)
