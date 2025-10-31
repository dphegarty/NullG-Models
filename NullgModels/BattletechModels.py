from datetime import datetime
from typing import List, Optional, Union, Dict, Any
from pydantic import Field, field_validator, ValidationInfo

from NullgModels.AlphaStrikeModels import AlphaStrikeData
from NullgModels.Constants import *
from NullgModels.PilotModels import PilotData
from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import UnitType
from NullgModels.TotalWarModels import TotalWarDropshipData, TotalWarInfantryData, TotalWarAerospaceData, \
    TotalWarBattleMechData, TotalWarVehicleData, TotalWarDropshipExtendedData, TotalWarInfantryExtendedData, \
    TotalWarAerospaceExtendedData, TotalWarBattleMechExtendedData, TotalWarVehicleExtendedData


class BasicItem(NullGBaseModel):
    category: Optional[str] = Field(
        description="Category of the item",
        default=None
    )
    name: str = Field(
        description="Name of the item"
    )
    id: int = Field(
        description="ID of the item"
    )


class EraItem(NullGBaseModel):
    """ Era BaseModel - Describes an era in the NullG database """
    id: int = Field(
        description="Integer, this is the era's unique identifier based on MUL",
        examples=["9", "10", "255"]
    )
    name: str = Field(
        description="Name of the item",
        examples=["Jihad", "Civil War"]
    )
    yearStart: int = Field(
        description="Year the era started",
        examples=["3050", "3080"]
    )
    yearEnd: int = Field(
        description="Year the era ended",
        examples=["3100", "3150"]
    )


class BoxsetItem(NullGBaseModel):
    """ Boxset BaseModel - Describes a boxset in the NullG database """
    id: str = Field(
        description="ID, this is the barcode of the physical box and corresponds to the barcodes field on units",
        examples=["0850011819135"]
    )
    name: str = Field(
        description="Name of the boxset",
        examples=["Comstar Battle Level I"]
    )
    completed: bool = Field(
        description="Has the box contents been recorded",
        examples=["true", "false"]
    )
    modelCount: int = Field(
        description="Number of models in the item",
        examples=["5", "4"]
    )
    maxPoints: int = Field(
        description="Maximum amount of Alpha Strike points in the item",
        examples=["150", "200"]
    )
    minPoints: int = Field(
        description="Minimum amount of Alpha Strike points in the item",
        examples=["100", "120"]
    )
    maxBattleValue: int = Field(
        description="Maximum BV of the units contained in the boxset",
        examples=["10000", "5000"]
    )
    minBattleValue: int = Field(
        description="Minimum Bv of the units contained in the boxset",
        examples=["4215", "11567"]
    )


# MUL BaseModel
class MULUnitItem(NullGBaseModel):
    mulTypeId: int = Field(
        description="Type ID",
        examples=["18"]
    )
    mulType: str = Field(
        description="Type",
        examples=["BattleMech"]
    )
    name: str = Field(
        description="Name",
        examples=["Warlock Prime"]
    )
    id: int = Field(
        description="The Id assigned to the unit in the MUL",
        examples=["8177"]
    )
    mass: float = Field(
        description="Mass",
        examples=["100", "50"]
    )
    bv: int = Field(
        description="Battle Value version 2",
        examples=["384", "5600"]
    )
    pv: int = Field(
        description="Alpha Strike points value",
        examples=["20", "43"]
    )
    role: str = Field(
        description="Role",
        examples=["Ambusher", "Brawler"]
    )
    roleId: int = Field(
        description="Role ID",
        examples=["0", "6"]
    )
    source: str = Field(
        description="Source the unit can be found in",
        examples=["Recognition Cards None", "TR:3145 RS:3145"]
    )
    rulesLevel: str = Field(
        description="Rule level",
        examples=["Advanced", "Standard"]
    )
    rulesLevelId: int = Field(
        description="Rule level ID",
        examples=["1", "3"]
    )
    era: str = Field(
        description="Era that this unit was introduced in.",
        examples=["Civil War", "Jihad"]
    )
    eraId: int = Field(
        description="Era ID that this unit was introduced in.",
        examples=["1", "3"]
    )
    intro: int = Field(
        description="In universe year the unit was introduced",
        examples=["3050", "3080"]
    )
    pullDate: str = Field(
        description="Date the unit was pulled",
        examples=["2022-01-01"]
    )
    availableEras: List[int] = Field(
        description="Era Ids in which the unit is available in",
        examples=["[1, 3]", "[1, 2]"]
    )
    factions: List[int] = Field(
        description="Faction Ids this unit is available to",
        examples=["[4,6,8", "[1,2,3]"]
    )
    nullgId: str = Field(
        description="Corresponding Unit Nullg Database UUID",
        examples=["6b6369f2-bcee-4a08-bd11-171d90cab87c"]
    )

    @field_validator('pullDate', mode='before')
    def validate_pullDate_type(cls, v: datetime) -> str:
        return str(v)

# Unit BaseModel

class UnitData(NullGBaseModel):
    id: Optional[str] = Field(description="ID of the unit", default=None, title="ID")
    name: Optional[str] = Field(description="Name of the unit", default=None, title="Name")
    model: Optional[str] = Field(description="Model of the unit", default=None, title="Model")
    productionEra: Optional[int] = Field(description="The era the unit started production", default=None)
    mass: Optional[float] = Field(description="Mass or tonnage of the unit", default=None)
    version: Optional[float] = Field(description="Version of the unit document", default=None)
    bv: Optional[float] = Field(description="Battle Value v2", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    techbase: Optional[str] = Field(description="Unit overall technology base", default=None)
    mulId: Optional[int] = Field(description="The corresponding Master Unit List Id", default=None)
    weightClassId: Optional[int] = Field(description="Weight Class Id", default=None)
    roleId: Optional[int] = Field(description="Unit role Id", default=None)
    rulesLevel: Optional[int] = Field(description="Rules Level the unit is part of", default=None)
    barcodes: Optional[List[str]] = Field(description="Barcodes of any boxsets the unit miniature is part of",
                                          default=None)
    fullName: Optional[str] = Field(description="Units full name", default=None)
    metadata: Optional[Dict[str, bool]] = Field(description="Metadata", default=None)
    notes: Optional[str] = Field(description="Any extra notes", default=None)
    unitCategory: Optional[int] = Field(description="Unit category: Official, User Created..", default=None)
    factions: Optional[List[int]] = Field(description="List of Faction Ids that the unit is available to", default=None)
    creationSource: Optional[str] = Field(description="How was the created", default=None)
    productionYear: Optional[int] = Field(description="The year the unit went into production", default=None)
    availableEras: Optional[List[int]] = Field(description="Eras the unit is available in", default=None)
    alphaStrike: Optional[AlphaStrikeData] = Field(description="Alpha Strike Data", default=None)
    alphaStrikeResults: Optional[Dict[str, Any]] = Field(description="Alpha Strike Calculation Data", default=None)
    unitTypeId: int = Field(description="Type of unit", default=None)
    unitSubtypeId: int = Field(description="Subtype of unit", default=None)
    expanded: bool = Field(
        description="Is the unit data expanded to include full equipment and Mul data",
        default=False,
        examples=[True, False]
    )
    totalWar: Optional[Union[
        TotalWarDropshipData, TotalWarInfantryData, TotalWarAerospaceData, TotalWarBattleMechData,
        TotalWarVehicleData]] = Field(description="Total War Data", default=None)
    bvResults: Optional[Dict[str, Any]] = Field(description="Battle Value v2 Calculation Data", default=None)
    statistics: Optional[Dict[str, Any]] = Field(description="Different type of statistics about the unit",
                                                 default=None)
    pilotData: Optional[List[PilotData]] = Field(description="List of Pilot Data class that describe a pilot", default_factory=list)

    @field_validator(FIELD_TOTAL_WAR, mode='before')
    @classmethod
    def validate_totalwar_type(cls, v: Dict, info: ValidationInfo):
        if v is not None and isinstance(v, dict):
            if FIELD_UNIT_TYPE_ID in info.data and isinstance(info.data[FIELD_UNIT_TYPE_ID], int):
                try:
                    thisUnitType = UnitType(info.data[FIELD_UNIT_TYPE_ID])
                except ValueError:
                    raise ValueError('Invalid unit type')

                unitTypesMap = {
                    UnitType.mech: TotalWarBattleMechData,
                    UnitType.vehicle: TotalWarVehicleData,
                    UnitType.infantry: TotalWarInfantryData,
                    UnitType.aerospace: TotalWarAerospaceData,
                    UnitType.dropship: TotalWarDropshipData,
                }

                try:
                    return unitTypesMap[thisUnitType](**v)
                except KeyError:
                    raise ValueError('Invalid unit type')
            else:
                raise ValueError('Unit type id field does not exist')
        else:
            return v


class UnitDataExtended(UnitData):
    expanded: bool = Field(
        description="Is the unit data expanded to include full equipment and Mul data",
        default=True,
        examples=[True, False]
    )
    mulData: Optional[MULUnitItem] = Field(description="MUL Unit Data", default=None)
    totalWar: Optional[Union[
        TotalWarDropshipExtendedData,
        TotalWarInfantryExtendedData,
        TotalWarAerospaceExtendedData,
        TotalWarBattleMechExtendedData,
        TotalWarVehicleExtendedData
    ]] = Field(description="Extended Total War Data that includes fill equipment data", default=None)

    @field_validator(FIELD_TOTAL_WAR, mode='before')
    @classmethod
    def validate_totalwar_type(cls, v: Dict, info: ValidationInfo):
        if v is not None and isinstance(v, dict):
            if FIELD_UNIT_TYPE_ID in info.data and isinstance(info.data[FIELD_UNIT_TYPE_ID], int):
                try:
                    thisUnitType = UnitType(info.data[FIELD_UNIT_TYPE_ID])
                except ValueError:
                    raise ValueError('Invalid unit type')

                unitTypesMap = {
                    UnitType.mech: TotalWarBattleMechExtendedData,
                    UnitType.vehicle: TotalWarVehicleExtendedData,
                    UnitType.infantry: TotalWarInfantryExtendedData,
                    UnitType.aerospace: TotalWarAerospaceExtendedData,
                    UnitType.dropship: TotalWarDropshipExtendedData,
                }

                try:
                    return unitTypesMap[thisUnitType](**v)
                except KeyError:
                    raise ValueError('Invalid unit type')
            else:
                raise ValueError('Unit type id field does not exist')
        else:
            return v
