from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeErrorCode


class TributeError(TributeModel):
    request_id: str = Field(
        ...,

        examples=["9c5606ac80274d0f97a0c63689e540f8"])
    """Request ID"""
    code: TributeErrorCode = Field(
        ...,

        examples=[TributeErrorCode.NOT_FOUND])
    """Error code"""
    message: str = Field(
        ...,

        examples=["shop not found"])
    """Error description"""
