# Inventory Models
from typing import Optional

from pydantic import Field

from NullgModels.BattletechModels import UnitData
from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import InventoryStorageType


class OrganizationItem(NullGBaseModel):
    id: Optional[str] = Field(description="", default=None)
    name: Optional[str] = Field(description="", default=None)
    armyListTypeId: int = Field(description="", default=0)
    bvTotal: int = Field(description="", default=None)
    bvUsed: int = Field(description="", default=None)
    pvTotal: int = Field(description="", default=None)
    pvUsed: int = Field(description="", default=None)
    combatCommand: str = Field(description="", default="")
    commandingOfficerId: str = Field(description="", default="")
    commandSpecialAbilities: List[str] = Field(description="", default=[])
    eraId: int = Field(description="", default=0)
    experienceLevelId: int = Field(description="", default=0)
    faction: str = Field(description="", default="")
    gameSystem: GameSystem = Field(description="", default=GameSystem.none)
    maxSize: int = Field(description="", default=0)
    militaryStructureId: int = Field(description="", default=0)
    organizationType: int = Field(description="", default=0)
    organizationId: str = Field(description="", default=0)
    parentOrganizationId: str = Field(description="", default=0)
    reputation: int = Field(description="", default=0)
    size: int = Field(description="", default=0)
    subCommand: str = Field(description="", default="")
    techRatingValue: int = Field(description="", default=0)
    customColor: bool = Field(description="", default=False)
    color: str = Field(description="", default="")


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


class InventoryItem(NullGBaseModel):
    # Base Fields that are stored
    id: str = Field(description="", default=None)
    unitId: str = Field(description="", default=None)
    storageType: InventoryStorageType = Field(description="", default=InventoryStorageType.inventory)
    organizationId: str = Field(description="", default=None)
    pilotId: str = Field(description="", default=None)

    #Fields that are derived from the base fields
    unitData: UnitData = Field(description="", default=None)
    pilotData: PilotData = Field(description="", default=None)
