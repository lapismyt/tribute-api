from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeErrorCode


class TributeError(TributeModel):
    error: TributeErrorCode = Field(
        ...,
        description="Error code",
        examples=[TributeErrorCode.NOT_FOUND],
    )
    message: str = Field(
        ...,
        description="Error description",
        examples=["Invalid status"],
    )
