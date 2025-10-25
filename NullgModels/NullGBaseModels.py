from pydantic import BaseModel, ConfigDict


class NullGBaseModel(BaseModel):
    """ Base class for null and empty values"""
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
