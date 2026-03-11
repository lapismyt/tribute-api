from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeMeta(TributeModel):
    total: int | None = Field(None)
    """Total number of items."""

    offset: int | None = Field(None)
    """Current page number."""

    limit: int | None = Field(None)
    """Page size."""
