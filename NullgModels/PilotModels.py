from pydantic import Field

from NullgModels.NullGBaseModels import NullGBaseModel


class Skills(NullGBaseModel):
    piloting: int = Field(description="", default=5)
    gunnery: int = Field(description="", default=4)


class PilotData(NullGBaseModel):
    id: str = Field(description="", default=None)
    firstName: str = Field(description="", default=None)
    lastName: str = Field(description="", default=None)
    skills: Skills = Field(description="", default=None)
    bio: str = Field(description="", default=None)
    organizationId: str = Field(description="", default=None)
    kills: int = Field(description="", default=None)
    deaths: int = Field(description="", default=None)
    imageUrl: str = Field(description="", default=None)

