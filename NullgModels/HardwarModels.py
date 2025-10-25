from enum import IntEnum
from typing import List, Optional

from pydantic import BaseModel, Field


class WeaponsAbilityType(IntEnum):
    normal = 0
    weapon = 1
    armamentUpgrade = 2

class ElementType(IntEnum):
    vehicle = 0
    walker = 1

class WeaponsAbilityData(BaseModel):
    """ Description an Element ability """
    name: str = Field(
        description="Name of the ability",
        examples=["Tracked", "Rail Gun"]
    )
    weaponsAbilityType: WeaponsAbilityType = Field(
        description="Type of the ability",
        examples=["0", "1"]
    )

class ElementStats(BaseModel):
    """ Description of an Element's stats """
    mobility: int = Field(
        description="Mobility Value",
        default=0,
        examples=["4", "6"]
    )
    firePower: int = Field(
        description="Fire Power Value",
        default=0,
        examples=["4", "6"]
    )
    armor: int = Field(
        description="Armor Value",
        default=0,
        examples=["4", "6"]
    )
    defense: int = Field(
        description="Defense Value",
        default=0,
        examples=["4", "6"]
    )
    weaponsAbilities: List[WeaponsAbilityData] = Field(
        description="List of abilities",
        default_factory=list,
        examples=[]
    )

class ElementData(BaseModel):
    """ Description of an Element """
    id: str = Field(
        description="UUID of the element",
        examples=[""]
    )
    name: str = Field(
        description="Name of the element",
        examples=[""]
    )
    imageUrl: str = Field(
        description="Image URL of the element",
        examples=[""]
    )
    elementType: ElementType = Field(
        description="Type of the element, see ElementType Enum",
        examples=["0", "1"]
    )
    elementClass: int = Field(
        description="Class of the element",
        examples=["0", "1"]
    )
    stats: ElementStats = Field(
        description="Stats of the element",
        examples=[]
    )
    version: float = Field(
        description="Version of the element",
        examples=["1.0", "1.12", "1.76"]
    )
    manufacturer: str = Field(
        description="Manufacturer of the element",
        examples=["", ""]
    )

