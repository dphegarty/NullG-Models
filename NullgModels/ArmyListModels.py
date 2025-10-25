from typing import List

from pydantic import Field

from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import RecordSheetType


### Army List Models

class ArmyUnitMember(NullGBaseModel):
    id: str = Field(description="", default=None)
    skill: str = Field(description="", default=None)
    availability: str = Field(description="", default=None)
    pilot: str = Field(description="", default=None)
    name: str = Field(description="", default=None)
    pilotAbilities: List[str] = Field(description="", default=None)
    rsType: RecordSheetType = Field(description="", default=None)
    points: str = Field(description="", default=None)


class ArmyListMember(NullGBaseModel):
    name: str = Field(description="", default="")
    specialAbilities: List[str] = Field(description="", default=[])
    type: str = Field(description="", default="")
    formationType: str = Field(description="", default="")
    pointsType: str = Field(description="", default="")
    pointsTotal: str = Field(description="", default="")
    customFields: List[str] = Field(description="", default=[])
    experience: str = Field(description="")
    techRating: str = Field(description="")
    members: List[ArmyUnitMember] = Field(description="", default=[])


class ArmyList(NullGBaseModel):
    name: str = Field(description="", default="")
    subCommand: str = Field(description="", default="")
    fiction: str = Field(description="", default="")
    era: str = Field(description="", default="")
    points: str = Field(description="", default="")
    pointsType: str = Field(description="", default="")
    experience: str = Field(description="", default="")
    abilities: List[str] = Field(description="", default=[])
    type: str = Field(description="", default="")
    combatCommand: str = Field(description="", default="")
    addNotes: bool = Field(description="", default=False)
    rsType: RecordSheetType = Field(description="", default=RecordSheetType.none)
    format: str = Field(description="", default="")
    techRating: str = Field(description="", default="")
    members: List[ArmyListMember] = Field(description="", default=[])