from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeErrorCode


class TributeError(TributeModel):
    request_id: str | None = Field(None, examples=["9c5606ac80274d0f97a0c63689e540f8"])
    """Request ID"""

    code: TributeErrorCode | None = Field(None, examples=[TributeErrorCode.NOT_FOUND])
    """Error code"""

    error: TributeErrorCode | None = Field(None, examples=[TributeErrorCode.NOT_FOUND])
    """Error code"""

    message: str | None = Field(None, examples=["shop not found"])
    """Error description"""
