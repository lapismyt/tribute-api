from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeDeactivateShopTokenResponse(TributeModel):
    success: bool = Field(..., examples=[True])
    message: str = Field(..., examples=["token deactivated"])
