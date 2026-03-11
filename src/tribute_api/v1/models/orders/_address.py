from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeAddress(TributeModel):
    country_iso2: str | None = Field(None, examples=["US"])
    """Two-letter ISO country code."""
    country_iso3: str | None = Field(None, examples=["USA"])
    """Three-letter ISO country code."""
