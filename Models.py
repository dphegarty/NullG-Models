from datetime import datetime
from enum import Enum, IntEnum
from typing import List, Optional, Union, Dict, Any

from pydantic import BaseModel, Field, field_validator


class OperationStatus(str, Enum):
    success = "success"
    failure = "failure"

class EquipmentType(IntEnum):
    armor = 0
    weapon = 1
    ammo = 2
    engine = 3
    gyro = 4
    structure = 5
    cockpit = 6
    other = 7
    myomer = 8
    manipulator = 9
    heatsink = 10
    conversion = 11
    enhancement = 12
    bay = 13
    weaponbay = 14

class WeightClass(IntEnum):
    ultralight = 0
    light = 1
    medium = 2
    heavy = 3
    assault = 4
    superHeavy = 5

class UnitCategory(IntEnum):
    official = 0
    userCreated = 1
    apocryphal = 2
    illegal = 3

# SearchQuery BaseModel
class SearchFilter(BaseModel):
    filter: Dict = Field(description="The query to run against the data. The query is based on MongoDb filter.",
                         default=None,
                         examples=[
                            "{'name': 'Warhammer'}",
                            "{'totalWar.walkMp': { '$ge': 5}}"
                            "{'alphaStrike.size': 2, '$and': [{'alphaStrike.damageShort': {'$ge': 3}}, {'alphaStrike.damageLong': {'$ge': 2}}]}'"
                        ])
    project: Optional[Dict[str, Union[int, bool]]] = Field(description="Fields to return in the response. "
                                                                       "This is in the MongoDb **projection** format.\n\nA Dictionary with "
                                                                       "field names, Use **1**  or **True** to include, **0** or **False** to exclude",
                                                           default=None,
                                                           examples=[
                                                               "`{'name': 1, 'totalWar.equipmentList': 1, 'alphaStrike': 0}`",
                                                               "`{'fullName: 1, 'id': 1}`"
                                                           ])
    page: Optional[int] = Field(description="The page number to return.", default=1, ge=1, le=20)
    itemsPerPage: Optional[int] = Field(description="The maximum number of items to return per page.", default=50, ge=1,
                                        le=100)


class PipelineFilter(BaseModel):
    pipeline: List[Dict[str, Any]] = Field(description="The aggregation pipeline", default=None)
    page: Optional[int] = Field(description="The page number to return.", default=1, ge=1, le=20)
    itemsPerPage: Optional[int] = Field(description="The maximum number of items to return.", default=50, ge=1, le=100)


class BasicItem(BaseModel):
    category: Optional[str] = Field(description="Category of the item", default=None)
    name: str = Field(description="Name of the item", default=None)
    id: int = Field(description="ID of the item", default=None)

### Boxset BaseModel
class BoxsetItem(BaseModel):
    id: Optional[str] = Field(description="ID, this is the barcode of the physical box and corresponds to the barcodes field on units", default=None)
    name: Optional[str] = Field(description="Name of the boxset", default=None)
    completed: Optional[bool] = Field(description="Has the box contents been recorded", default=None)
    modelCount: Optional[int] = Field(description="Number of models in the item", default=None)
    maxPoints: Optional[int] = Field(description="Maximum amount of Alpha Strike points in the item", default=None)
    minPoints: Optional[int] = Field(description="Minimum amount of Alpha Strike points in the item", default=None)
    maxBattleValue: Optional[int] = Field(description="Maximum BV of the units contained in the boxset", default=None)
    minBattleValue: Optional[int] = Field(description="Minimum Bv of the units contained in the boxset", default=None)


# MUL BaseModel
class MULUnitItem(BaseModel):
    mulTypeId: Optional[int] = Field(description="Type ID", default=None)
    mulType: Optional[str] = Field(description="Type", default=None)
    name: Optional[str] = Field(description="Name", default=None)
    id: Optional[int] = Field(description="ID", default=None)
    mass: Optional[float] = Field(description="Mass", default=None)
    bv: Optional[int] = Field(description="Battle Value version 2", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    role: Optional[str] = Field(description="Role", default=None)
    roleId: Optional[int] = Field(description="Role ID", default=None)
    source: Optional[str] = Field(description="Source the unit can be found in", default=None)
    rulesLevel: Optional[str] = Field(description="Rule level", default=None)
    rulesLevelId: Optional[int] = Field(description="Rule level ID", default=None)
    era: Optional[str] = Field(description="Era", default=None)
    eraId: Optional[int] = Field(description="Era ID ", default=None)
    intro: Optional[int] = Field(description="Year the unit was introduced", default=None)
    pullDate: Optional[str] = Field(description="Date the unit was pulled", default=None)
    availableEras: Optional[List[int]] = Field(description="Eras in which the unit is available", default=None)
    factions: Optional[List[int]] = Field(description="Factions this unit is available to", default=None)
    nullgId: Optional[str] = Field(description="Corresponding Unit Nullg ID", default=None)

    @field_validator('pullDate', mode='before')
    def validate_pullDate_type(cls, v: datetime) -> str:
        return str(v)


# TotalWar BaseModels

class TotalWarBasicItem(BaseModel):
    name: Optional[str] = Field(description="Name", default=None)
    value: Optional[int] = Field(description="Value", default=None)


class TotalWarBayItem(BaseModel):
    id: Optional[str] = Field(description="ID of the bay", default=None)
    name: Optional[str] = Field(description="Name of the bay", default=None)
    value: Optional[float] = Field(description="How much the bay holds", default=None)
    doors: Optional[int] = Field(description="Number of doors in the bay", default=None)


class TotalWarArmorLocation(BaseModel):
    armor: Optional[str] = Field(description="Armor type, mainly used for Patchwork armor", default=None)
    location: Optional[str] = Field(description="Location of the armor", default=None)
    value: Optional[int] = Field(description="Value of the armor", default=None)


class TotalWarEquipmentItem(BaseModel):
    id: str = Field(description="ID of the equipment", default=None)
    name: str = Field(description="Name of the equipment", default=None)
    location: str = Field(description="Location of the equipment", default=None)
    options: str = Field(description="Options of the equipment", default=None)
    type: str = Field(description="Type of the equipment", default=None)


class TotalWarCriticalLocationItem(BaseModel):
    location: str = Field(description="Critical location", default=None)
    slots: List[Union[str, None]] = Field(description="Slots of the critical location", default=None)


# Tested and Works
class TotalWarBattleMech(BaseModel):
    armor: Optional[str] = Field(description="Armor", default=None)
    armorTechbase: Optional[str] = Field(description="Armor Technology base", default=None)
    bv: Optional[float] = Field(description="BV2 of the unit", default=None)
    cockpit: Optional[str] = Field(description="Type of Cockpit", default=None)
    config: Optional[str] = Field(description="Unit configuration", default=None)
    constructionInvalid: Optional[List[str]] = Field(description="List of reason the unit construction is invalid",
                                                     default=None)
    constructionValidated: Optional[bool] = Field(description="Has the unit construction been validated", default=None)
    criticalFreeHeatSinks: Optional[int] = Field(description="The amount of Critical Free Heat Sinks ", default=None)
    engine: Optional[str] = Field(description="Full Engine description", default=None)
    engineRating: Optional[int] = Field(description="Engine Rating", default=None)
    engineTechbase: Optional[str] = Field(description="Engine Technology base", default=None)
    engineType: Optional[str] = Field(description="Type of engine", default=None)
    extraOptions: Optional[Dict[str, bool]] = Field(description="Extra optional this unit has", default=None)
    gyro: Optional[str] = Field(description="Type of Gyro", default=None)
    heatSinks: Optional[int] = Field(description="Number of Heats the unit has", default=None)
    heatSinksTechbase: Optional[str] = Field(description="Heat Sinks Technology base", default=None)
    heatSinksType: Optional[int] = Field(description="Type of Heat Sink, Single, Double, Laser, Compact", default=None)
    mass: Optional[float] = Field(description="Units Mass", default=None)
    myomer: Optional[str] = Field(description="Type of Myomer", default=None)
    myomerTechbase: Optional[str] = Field(description="Myomer Technology base", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    roleId: Optional[int] = Field(description="Role Id", default=None)
    source: Optional[str] = Field(description="Source of the unit information", default=None)
    structure: Optional[str] = Field(description="Internal Structure Type", default=None)
    structureTechbase: Optional[str] = Field(description="Internal Structure Technology base", default=None)
    techbase: Optional[str] = Field(description="Overall unit Technology base", default=None)
    unitType: Optional[str] = Field(description="Unit type", default=None)
    version: Optional[float] = Field(description="Unit data version", default=None)
    weapons: Optional[int] = Field(description="Number of weapons mounted on the unit", default=None)
    unitDataSourceUri: Optional[str] = Field(description="URI of the unit's source information", default=None)
    heatSinksEngineBase: Optional[int] = Field(description="Number of heat Sinks that are based in the engine",
                                               default=None)
    heatSinksOmniBase: Optional[int] = Field(description="Number of Omnipod Heat Sinks.", default=None)
    equipmentList: Optional[List[TotalWarEquipmentItem]] = Field(description="Equipment, Weapons and Ammunition",
                                                                 default=None)
    armorLocations: Optional[List[TotalWarArmorLocation]] = Field(description="Armor locations and values",
                                                                  default=None)
    criticalLocations: List[TotalWarCriticalLocationItem] = Field(description="Critical Slot information", default=None)
    copyrightTrademark: Optional[str] = Field(description="Basic Trademark/Copyright", default=None)
    runMp: Optional[int] = Field(description="Units Run movement", default=None)
    motionType: Optional[str] = Field(description="Units motion type", default=None)
    productionYear: Optional[int] = Field(description="Year the unit was first produced", default=None)
    rulesLevel: Optional[int] = Field(description="Rule Level of the unit", default=None)
    walkMp: Optional[int] = Field(description="Units Walk movement", default=None)
    barRating: Optional[int] = Field(description="BAR Rating", default=None)
    trooperCount: Optional[int] = Field(description="Number of individuals that make up this unit", default=None)
    jumpMp: Optional[int] = Field(description="Units Jump movement", default=None)
    armorFactor: Optional[int] = Field(description="Units armor factor, the total points of armor", default=None)
    armorFactorMax: Optional[int] = Field(description="Maximum amount of armor that can be mounted on this unit",
                                          default=None)
    fireControl: Optional[str] = Field(description="Fire Control", default=None)
    unitSubtype: Optional[str] = Field(description="Unit Subtype", default=None)
    productionEra: Optional[int] = Field(description="Ear in which the unit was first produced", default=None)


# Tested and Works
class TotalWarAerospace(BaseModel):
    armor: Optional[str] = Field(description="Armor", default=None)
    bv: Optional[float] = Field(description="BV2 of the unit", default=None)
    cockpit: Optional[str] = Field(description="Type of Cockpit", default=None)
    config: Optional[str] = Field(description="Unit configuration", default=None)
    constructionInvalid: Optional[List[str]] = Field(description="List of reason the unit construction is invalid",
                                                     default=None)
    constructionValidated: Optional[bool] = Field(description="Has the unit construction been validated", default=None)
    extraOptions: Optional[Dict[str, bool]] = Field(description="Extra optional this unit has", default=None)
    engineRating: Optional[int] = Field(description="Engine Rating", default=None)
    engineTechbase: Optional[str] = Field(description="Engine Technology base", default=None)
    engineType: Optional[str] = Field(description="Type of engine", default=None)
    fuel: Optional[int] = Field(description="Fuel", default=None)
    transportSpace: Optional[Dict[str, int]] = Field(description="Types of troop carrying capacity", default=None)
    heatSinks: Optional[int] = Field(description="Number of Heats the unit has", default=None)
    heatSinksTechbase: Optional[str] = Field(description="Heat Sinks Technology base", default=None)
    heatSinksType: Optional[int] = Field(description="Type of Heat Sink, Single, Double, Laser, Compact", default=None)
    mass: Optional[float] = Field(description="Units Mass", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    roleId: Optional[int] = Field(description="Role Id", default=None)
    source: Optional[str] = Field(description="Source of the unit information", default=None)
    structure: Optional[str] = Field(description="Internal Structure Type", default=None)
    structureTechbase: Optional[str] = Field(description="Internal Structure Technology base", default=None)
    safeThrust: Optional[int] = Field(description="Safe Thrust", default=None)
    techbase: Optional[str] = Field(description="Overall unit Technology base", default=None)
    unitType: Optional[str] = Field(description="Unit type", default=None)
    version: Optional[float] = Field(description="Unit data version", default=None)
    weapons: Optional[str] = Field(description="Number of weapons mounted on the unit", default=None)
    unitDataSourceUri: Optional[str] = Field(description="URI of the unit's source information", default=None)
    heatSinksOmniBase: Optional[int] = Field(description="Number of Omnipod Heat Sinks.", default=None)
    equipmentList: Optional[List[TotalWarEquipmentItem]] = Field(description="Equipment, Weapons and Ammunition",
                                                                 default=None)
    armorLocations: Optional[List[TotalWarArmorLocation]] = Field(description="Armor locations and values",
                                                                  default=None)
    copyrightTrademark: Optional[str] = Field(description="Basic Trademark/Copyright", default=None)
    runMp: Optional[int] = Field(description="Units Run movement", default=None)
    motionType: Optional[str] = Field(description="Units motion type", default=None)
    productionYear: Optional[int] = Field(description="Year the unit was first produced", default=None)
    rulesLevel: Optional[int] = Field(description="Rule Level of the unit", default=None)
    walkMp: Optional[int] = Field(description="Units Walk movement", default=None)
    barRating: Optional[int] = Field(description="BAR Rating", default=None)
    trooperCount: Optional[int] = Field(description="Number of individuals that make up this unit", default=None)
    jumpMp: Optional[int] = Field(description="Units Jump movement", default=None)
    armorFactor: Optional[int] = Field(description="Units armor factor, the total points of armor", default=None)
    armorFactorMax: Optional[int] = Field(description="Maximum amount of armor that can be mounted on this unit",
                                          default=None)
    fireControl: Optional[str] = Field(description="Fire Control", default=None)
    unitSubtype: Optional[str] = Field(description="Unit Subtype", default=None)
    productionEra: Optional[int] = Field(description="Ear in which the unit was first produced", default=None)


# Tested and works
class TotalWarInfantry(BaseModel):
    armor: Optional[str] = Field(description="Armor", default=None)
    bv: Optional[float] = Field(description="BV2 of the unit", default=None)
    config: Optional[str] = Field(description="Unit configuration", default=None)
    constructionInvalid: Optional[List[str]] = Field(description="List of reason the unit construction is invalid",
                                                     default=None)
    constructionValidated: Optional[bool] = Field(description="Has the unit construction been validated", default=None)
    extraOptions: Optional[Dict[str, bool]] = Field(description="Extra optional this unit has", default=None)
    mass: Optional[float] = Field(description="Units Mass", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    source: Optional[str] = Field(description="Source of the unit information", default=None)
    techbase: Optional[str] = Field(description="Overall unit Technology base", default=None)
    unitType: Optional[str] = Field(description="Unit type", default=None)
    version: Optional[float] = Field(description="Unit data version", default=None)
    armorTechbase: Optional[str] = Field(description="Armor Technology base", default=None)
    structureTechbase: Optional[str] = Field(description="Internal Structure Technology base", default=None)
    equipmentList: Optional[List[TotalWarEquipmentItem]] = Field(description="Equipment, Weapons and Ammunition",
                                                                 default=None)
    armorLocations: Optional[List[TotalWarArmorLocation]] = Field(description="Armor locations and values",
                                                                  default=None)
    unitDataSourceUri: Optional[str] = Field(description="URI of the unit's source information", default=None)
    structure: Optional[str] = Field(description="Internal Structure Type", default=None)

    copyrightTrademark: Optional[str] = Field(description="Basic Trademark/Copyright", default=None)
    runMp: Optional[int] = Field(description="Units Run movement", default=None)
    motionType: Optional[str] = Field(description="Units motion type", default=None)
    productionYear: Optional[int] = Field(description="Year the unit was first produced", default=None)
    rulesLevel: Optional[int] = Field(description="Rule Level of the unit", default=None)
    walkMp: Optional[int] = Field(description="Units Walk movement", default=None)
    trooperCount: Optional[int] = Field(description="Number of individuals that make up this unit", default=None)
    jumpMp: Optional[int] = Field(description="Units Jump movement", default=None)
    weightClassId: Optional[int] = Field(description="Weight Class Id", default=None)
    armorFactor: Optional[int] = Field(description="Units armor factor, the total points of armor", default=None)
    armorFactorMax: Optional[int] = Field(description="Maximum amount of armor that can be mounted on this unit",
                                          default=None)
    unitSubtype: Optional[str] = Field(description="Unit Subtype", default=None)
    trooperMass: Optional[float] = Field(description="Mass per Trooper", default=None)
    productionEra: Optional[int] = Field(description="Ear in which the unit was first produced", default=None)
    roleId: Optional[int] = Field(description="Role Id", default=None)
    squads: Optional[int] = Field(description="Squads in the units", default=None)
    squadSize: Optional[int] = Field(description="Squad size", default=None)
    secondaryWeaponTroops: Optional[int] = Field(description="Number troopers that have secondary weapons",
                                                 default=None)
    isExoskeleton: Optional[bool] = Field(description="Is this an exoskeleton", default=None)


# Tested and Works
class TotalWarVehicle(BaseModel):
    armor: Optional[str] = Field(description="Armor", default=None)
    bv: Optional[float] = Field(description="BV of the unit", default=None)
    config: Optional[str] = Field(description="Unit configuration", default=None)
    constructionInvalid: Optional[List[str]] = Field(description="List of reason the unit construction is invalid",
                                                     default=None)
    constructionValidated: Optional[bool] = Field(description="Has the unit construction been validated",
                                                  default=None)
    engineRating: Optional[int] = Field(description="Rating of the engine", default=None)
    engineTechbase: Optional[str] = Field(description="Technology base", default=None)
    engineType: Optional[str] = Field(description="Type of the engine", default=None)
    extraOptions: Optional[Dict[str, bool]] = Field(description="Extra optional this unit has", default=None)
    mass: Optional[float] = Field(description="Units Mass", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    source: Optional[str] = Field(description="Source of the unit information", default=None)
    techbase: Optional[str] = Field(description="Internal Structure Technology base", default=None)
    unitType: Optional[str] = Field(description="Unit type", default=None)
    version: Optional[float] = Field(description="Unit data version", default=None)
    unitDataSourceUri: Optional[str] = Field(description="URI of the unit's source information", default=None)
    turretType: Optional[int] = Field(description="Type of the turret type", default=None)
    transportSpace: Optional[Dict[str, int]] = Field(description="Transport space", default=None)
    armorLocations: List[TotalWarArmorLocation]
    equipmentList: List[TotalWarEquipmentItem]
    structure: Optional[str] = Field(description="Internal Structure Type", default=None)
    structureTechbase: Optional[str] = Field(description="Internal Structure Type", default=None)
    armorTechbase: Optional[str] = Field(description="Armor Technology base", default=None)
    copyrightTrademark: Optional[str] = Field(description="Basic Trademark/Copyright", default=None)
    runMp: Optional[int] = Field(description="Units Run movement", default=None)
    motionType: Optional[str] = Field(description="Units motion type", default=None)
    productionYear: Optional[int] = Field(description="Year the unit was first produced", default=None)
    rulesLevel: Optional[int] = Field(description="Rule Level of the unit", default=None)
    walkMp: Optional[int] = Field(description="Units Walk movement", default=None)
    barRating: Optional[int] = Field(description="Rating of the bar", default=None)
    trooperCount: Optional[int] = Field(description="Number of individuals that make up this unit", default=None)
    jumpMp: Optional[int] = Field(description="Units Jump movement", default=None)
    weightClassId: Optional[int] = Field(description="Weight Class Id", default=None)
    armorFactor: Optional[int] = Field(description="Units armor factor", default=None)
    armorFactorMax: Optional[int] = Field(description="Maximum amount of armor that can be mounted on this unit",
                                          default=None)
    fireControl: Optional[str] = Field(description="Units fire control", default=None)
    unitSubtype: Optional[str] = Field(description="Units subtype", default=None)
    productionEra: Optional[int] = Field(description="Ear in which the unit was first produced", default=None)
    roleId: Optional[int] = Field(description="Role Id", default=None)
    hasControlSystems: Optional[bool] = Field(description="Has the Control systems", default=None)
    heatSinks: Optional[int] = Field(description="Heat Sinks", default=None)
    heatSinksTechbase: Optional[str] = Field(description="Technology base", default=None)
    heatSinksType: Optional[int] = Field(description="Type of the Heat Sinks", default=None)
    heatSinksEngineBase: Optional[int] = Field(description="Heat Sinks in the Engine", default=None)
    heatSinksOmniBase: Optional[int] = Field(description="Heat Sinks in the Omnipods", default=None)
    isTrailer: Optional[bool] = Field(description="Is this a trailer", default=None)
    extraCombatSeats: Optional[int] = Field(description="Extra Combat Seats", default=None)
    jumpjetType: Optional[int] = Field(description="Type of the Jumpjet type", default=None)


# Tested and works
class TotalWarDropship(BaseModel):
    armor: Optional[str] = Field(description="Armor", default=None)
    source: Optional[str] = Field(description="Source of the unit information", default=None)
    version: Optional[float] = Field(description="Unit data version", default=None)
    unitDataSourceUri: Optional[str] = Field(description="URI of the unit's source information", default=None)
    pv: Optional[int] = Field(description="Alpha Strike points value", default=None)
    armorLocations: Optional[List[TotalWarArmorLocation]] = Field(description="Armor locations and values",
                                                                  default=None)
    equipmentList: Optional[List[TotalWarEquipmentItem]] = Field(description="Equipment, Weapons and Ammunition",
                                                                 default=None)
    mass: Optional[float] = Field(description="Units Mass", default=None)
    techbase: Optional[str] = Field(description="Overall unit Technology base", default=None)
    bays: List[TotalWarBayItem] = Field(description="Bays in the unit", default=None)
    quarters: List[TotalWarBasicItem] = Field(description="Crew quarters in the unit", default=None)
    crewValues: List[TotalWarBasicItem] = Field(description="Crew values in the unit", default=None)
    armorTechbase: Optional[str] = Field(description="Armor Technology base", default=None)
    heatSinks: Optional[int] = Field(description="Number of Heats the unit has", default=None)
    heatSinksTechbase: Optional[str] = Field(description="Heat Sinks Technology base", default=None)
    heatSinksType: Optional[int] = Field(description="Type of Heat Sink, Single, Double, Laser, Compact", default=None)
    structuralIntegrity: Optional[int] = Field(description="Structural Integrity", default=None)
    engineRating: Optional[int] = Field(description="Engine Rating", default=None)
    engineTechbase: Optional[str] = Field(description="Engine Technology base", default=None)
    chassisType: Optional[int] = Field(description="Type of Cassis", default=None)
    unitType: Optional[str] = Field(description="Unit type", default=None)
    config: Optional[str] = Field(description="Unit configuration", default=None)
    bv: Optional[float] = Field(description="Battle Value 2 of the unit", default=None)
    copyrightTrademark: Optional[str] = Field(description="Basic Trademark/Copyright", default=None)
    runMp: Optional[int] = Field(description="Units Run movement", default=None)
    motionType: Optional[str] = Field(description="Units motion type", default=None)
    productionYear: Optional[int] = Field(description="Year the unit was first produced", default=None)
    rulesLevel: Optional[int] = Field(description="Rule Level of the unit", default=None)
    walkMp: Optional[int] = Field(description="Units Walk movement", default=None)
    barRating: Optional[int] = Field(description="BAR Rating", default=None)
    trooperCount: Optional[int] = Field(description="Number of individuals that make up this unit", default=None)
    jumpMp: Optional[int] = Field(description="Units Jump movement", default=None)
    weightClassId: Optional[int] = Field(description="Weight Class Id", default=None)
    armorFactor: Optional[int] = Field(description="Units armor factor, the total points of armor", default=None)
    armorFactorMax: Optional[int] = Field(description="Maximum amount of armor that can be mounted on this unit",
                                          default=None)
    fireControl: Optional[str] = Field(description="Fire Control", default=None)
    roleId: Optional[int] = Field(description="Role Id", default=None)
    fuel: Optional[int] = Field(description="Fuel", default=None)


# AlphaString BaseModels

class AlphaStrikeArcFormattedSpecialItem(BaseModel):
    name: Optional[str] = Field(description="Name of the arc", default=None)
    value: Optional[List[str]] = Field(description="List of formatted specials for the arc", default=None)


class AlphaStrikeArcDamageRecord(BaseModel):
    short: Optional[float] = Field(description="Short range damage value", default=None)
    medium: Optional[float] = Field(description="Medium range damage value", default=None)
    long: Optional[float] = Field(description="Long range damage value", default=None)
    extreme: Optional[float] = Field(description="Extreme range damage value", default=None)


class AlphaStrikeArcDamageMapItem(BaseModel):
    STD: Optional[AlphaStrikeArcDamageRecord] = Field(description="Standard Damage map for arc", default=None)
    SCAP: Optional[AlphaStrikeArcDamageRecord] = Field(description="Sub-capital Damage map for  arc",
                                                       default=None)
    MSL: Optional[AlphaStrikeArcDamageRecord] = Field(description="Capital Missile Damage map for arc", default=None)
    FLAK: Optional[AlphaStrikeArcDamageRecord] = Field(description="Flak Damage map for arc", default=None)
    PNT: Optional[AlphaStrikeArcDamageRecord] = Field(description="Point Defense Damage map for arc", default=None)
    CAP: Optional[AlphaStrikeArcDamageRecord] = Field(description="Capital Damage map for arc", default=None)


class AlphaStrikeArcDamageMap(BaseModel):
    name: Optional[str] = Field(description="Name of the arc", default=None)
    value: Optional[AlphaStrikeArcDamageMapItem] = Field(description="Damage map for the arc", default=None)


class AlphaStrikeSpecialDamageItem(BaseModel):
    name: Optional[str] = Field(description="Name of the special", default=None)
    count: Optional[int] = Field(description="Number of times the special is used", default=None)
    short: Optional[float] = Field(description="Short range damage value", default=None)
    medium: Optional[float] = Field(description="Medium range damage value", default=None)
    long: Optional[float] = Field(description="Long range damage value", default=None)
    extreme: Optional[float] = Field(description="Extreme range damage value", default=None)
    inTurret: Optional[bool] = Field(description="In Turret", default=None)


class AlphaStrike(BaseModel):
    formattedSpecials: Optional[List[str]] = Field(description="List of formatted specials in the unit", default=None)
    specials: Optional[List[str]] = Field(description="List of unformatted specials in the unit", default=None)
    specialsDamage: Optional[List[AlphaStrikeSpecialDamageItem]] = Field(
        description="List of special damage items in the unit", default=None)
    version: Optional[float] = Field(description="Version of the unit document", default=None)
    trooperCount: Optional[int] = Field(description="Number of individuals that make up this unit", default=None)
    aero: Optional[bool] = Field(description="Is this an aerospace unit", default=None)
    skill: Optional[int] = Field(description="Skill level of the pilot", default=None)
    useOfficialPoints: Optional[bool] = Field(description="Use Official Points", default=None)
    calculatedPV: Optional[int] = Field(description="Calculated Alpha Strike Points", default=None)
    officialPV: Optional[int] = Field(
        description="Official Alpha Strike Points as listed in the MUL * These are not always the correct values",
        default=None)
    armorThreshold: Optional[int] = Field(description="Armor Threshold for aerospace units", default=None)
    isLAM: Optional[bool] = Field(description="Is this a LAM unit", default=None)
    baseUnitType: Optional[str] = Field(description="Base Total War Unit Type", default=None)
    unitType: Optional[str] = Field(description="Alpha Strike Unit Type", default=None)
    size: Optional[int] = Field(description="Size value", default=None)
    walk: Optional[int] = Field(description="Regular ground movement", default=None)
    jump: Optional[int] = Field(description="Jump movement", default=None)
    movementMode: Optional[str] = Field(description="Movement mode", default=None)
    armor: Optional[int] = Field(description="Armor value", default=None)
    structure: Optional[int] = Field(description="Structure value", default=None)
    armed: Optional[bool] = Field(description="Is the unit considered armed", default=None)
    damageShort: Optional[float] = Field(description="Short range damage value", default=None)
    damageMedium: Optional[float] = Field(description="Medium range damage value", default=None)
    damageLong: Optional[float] = Field(description="Long range damage value", default=None)
    damageExtreme: Optional[float] = Field(description="Aerospace extreme range damage value", default=None)
    overheat: Optional[int] = Field(description="Overheat value", default=None)
    roleId: Optional[int] = Field(description="Role Id for the unit", default=None)
    tmm: Optional[int] = Field(description="Target Movement Modifier", default=None)
    arcversion: Optional[float] = Field(description="Arc Version", default=None)
    skillDifference: Optional[int] = Field(description="The different in skill from the base of 4", default=None)
    skillPoints: Optional[int] = Field(
        description="The additional points added to the unit because of skill adjustment", default=None)
    isLargeUnit: Optional[bool] = Field(description="Is this a large unit tht has arcs", default=None)
    arcFormatedSpecials: Optional[List[AlphaStrikeArcFormattedSpecialItem]] = Field(
        description="List of formatted arc specials for large units", default=None)
    arcDamageMaps: Optional[List[AlphaStrikeArcDamageMap]] = Field(description="The damage arcs for large units",
                                                                   default=None)


# Unit BaseModel

class UnitData(BaseModel):
    id: Optional[str] = Field(description="ID of the unit", default=None, title="ID")
    name: Optional[str] = Field(description="Name of the unit", default=None, title="Name")
    model: Optional[str] = Field(description="Model of the unit", default=None, title="Model")
    unitType: Optional[str] = Field(description="Unit type of the unit", default=None, title="Unit Type")
    productionEra: Optional[int] = Field(description="The era the unit started production", default=None)
    mass: Optional[float] = Field(description="Mass or tonnage of the unit", default=None)
    unitSubtype: Optional[str] = Field(description="Subtype of the unit", default=None)
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
    alphaStrike: Optional[AlphaStrike] = Field(description="Alpha Strike Data", default=None)
    alphaStrikeResults: Optional[Dict[str, Any]] = Field(description="Alpha Strike Calculation Data", default=None)
    totalWar: Optional[Union[
        TotalWarDropship, TotalWarInfantry, TotalWarAerospace, TotalWarBattleMech,
        TotalWarVehicle]] = Field(description="Total War Data", default=None)
    bvResults: Optional[Dict[str, Any]] = Field(description="Battle Value v2 Calculation Data", default=None)
    statistics: Optional[Dict[str, Any]] = Field(description="Different type of statistics about the unit",
                                                 default=None)

    @field_validator('totalWar', mode='before')
    def validate_totalwar_type(cls, v):
        if v['unitType'] == 'mech':
            return TotalWarBattleMech(**v)
        elif v['unitType'] == 'vehicle':
            return TotalWarVehicle(**v)
        elif v['unitType'] == 'infantry':
            return TotalWarInfantry(**v)
        elif v['unitType'] == 'aerospace':
            return TotalWarAerospace(**v)
        elif v['unitType'] == 'dropship':
            return TotalWarDropship(**v)
        else:
            raise ValueError('Invalid unit type')


# Equipment BaseModels

class EquipmentAlphaStrike(BaseModel):
    extreme: Optional[List[float]] = Field(description="Extreme range damage values", default=None)
    long: Optional[List[float]] = Field(description="Long range damage values", default=None)
    medium: Optional[List[float]] = Field(description="Medium range damage values", default=None)
    short: Optional[List[float]] = Field(description="Short range damage values", default=None)
    tc: Optional[bool] = Field(description="Can this use a Targeting Computer", default=None)
    specials: Optional[List[str]] = Field(description="List of specials abilities conferred by this equipment",
                                          default=None)


class EquipmentTypeData(BaseModel):
    isAMS: Optional[bool] = Field(description="Is the an Anti-Missile System", default=False)
    isAntiAir: Optional[bool] = Field(description="Is this Anti-Air", default=False)
    isAntiInfantry: Optional[bool] = Field(description="Is this Anti-Infantry", default=False)
    isApolloEnabled: Optional[bool] = Field(description="Can an Apollo MRM FCS be used", default=False)
    isArtemisEnabled: Optional[bool] = Field(description="Can an Artemis (IV, V) be used", default=False)
    isArtillery: Optional[bool] = Field(description="Is this an artillery piece", default=False)
    isArtilleryCannon: Optional[bool] = Field(description="Is the an artillery cannon", default=False)
    isBallistic: Optional[bool] = Field(description="Is this a Ballistic type weapon", default=False)
    isCapital: Optional[bool] = Field(description="Is this a capital weapon", default=False)
    isCluster: Optional[bool] = Field(description="Is this a cluster weapon", default=False)
    isDefensive: Optional[bool] = Field(description="Is this considered defensive equipment", default=False)
    isDirect: Optional[bool] = Field(description="Is this a Direct fire weapon", default=False)
    isDisplayed: Optional[bool] = Field(description="Show this be displayed on a record sheet", default=False)
    isEditable: Optional[bool] = Field(description="Is this an editable critical slot", default=False)
    isEnergy: Optional[bool] = Field(description="Is this an Energy weapon", default=False)
    isEquipment: Optional[bool] = Field(description="Is this a Equipment verse a weapon", default=False)
    isExplosive: Optional[bool] = Field(description="Is Explosive", default=False)
    isFixed: Optional[bool] = Field(description="Are the critical slots fixed and cannot be move around", default=False)
    isFlame: Optional[bool] = Field(description="Is Flame weapon", default=False)
    isHeatCausing: Optional[bool] = Field(description="Is Heat causing, example plasma", default=False)
    isHeavyWeapon: Optional[bool] = Field(description="Is this a heavy weapon for infantry", default=False)
    isHittable: Optional[bool] = Field(description="Are these critical slots damagable", default=False)
    isIndirect: Optional[bool] = Field(description="Is this indirect", default=False)
    isInfBurst: Optional[bool] = Field(description="Is consider burst weapon against infantry", default=False)
    isInfEncumbered: Optional[bool] = Field(description="Does this encumber infantry", default=False)
    isInfNonPen: Optional[bool] = Field(description="Does this count as non-penetrating against infantry", default=False)
    isInfantry: Optional[bool] = Field(description="Does this count as an infantry", default=False)
    isLPMEnabled: Optional[bool] = Field(description="Can a Pulse Laser Modular be used", default=False)
    isLegAttack: Optional[bool] = Field(description="Does this confer the Leg Attack ability", default=False)
    isMechanized: Optional[bool] = Field(description="Does this confer the Mechanized ability", default=False)
    isMelee: Optional[bool] = Field(description="Is this a melee verse ranged weapon", default=False)
    isMisc: Optional[bool] = Field(description="Is this miscellaneous equipment, does not count as a weapon or defensive", default=False)
    isMissile: Optional[bool] = Field(description="Is this a missile type", default=False)
    isOneShot: Optional[bool] = Field(description="Is this a one-shot weapon", default=False)
    isPPCCapacitorEnabled: Optional[bool] = Field(description="Can a PPC Capacitor be paired", default=False)
    isPair: Optional[bool] = Field(description="Does this come in pairs, like claws or talons", default=False)
    isPhysical: Optional[bool] = Field(description="Is this a physical weapon like Swords", default=False)
    isPulse: Optional[bool] = Field(description="Is this a pulse weapon", default=False)
    isRapidFire: Optional[bool] = Field(description="Does this fire multiple 'shots' like Ultra/Rotary ACs", default=False)
    isSingleHex: Optional[bool] = Field(description="Single Hex range", default=False)
    isSubCapital: Optional[bool] = Field(description="Is this Sub-capital", default=False)
    isSwarmAttack: Optional[bool] = Field(description="Does this confer the Swam Attack ability", default=False)
    isSwitchable: Optional[bool] = Field(description="", default=False)
    isTrackedEquipment: Optional[bool] = Field(description="Does this item get tracked on the record sheet", default=False)
    isTurret: Optional[bool] = Field(description="Is this a turret", default=False)
    isUnique: Optional[bool] = Field(description="Is this item limited to 1", default=False)
    isVariable: Optional[bool] = Field(description="Deos this have variable damage", default=False)
    isVariableCrit: Optional[bool] = Field(description="Does this equipment have variable critical slot count", default=False)
    isVariableMass: Optional[bool] = Field(description="Does this equipment have variable mass", default=False)
    isWeapon: Optional[bool] = Field(description="Is the considered a weapon", default=False)
    useTargetingComputer: Optional[bool] = Field(description="Can this use a targeting computer", default=False)


class EquipmentUnitTypes(BaseModel):
    battlearmor: Optional[bool] = Field(default=False, description="Can be used by Battle Armor")
    fighters: Optional[bool] = Field(default=False, description="Can be used by Fighters")
    infantry: Optional[bool] = Field(default=False, description="Can be used by Infantry")
    mech: Optional[bool] = Field(default=False, description="Can be used by Battlemech")
    protomechs: Optional[bool] = Field(default=False, description="Can be used by Protomech")
    smallcraft: Optional[bool] = Field(default=False, description="Can be used by Small Craft")
    supportvehicle: Optional[bool] = Field(default=False, description="Can be used by Support Vehicles")
    vehicles: Optional[bool] = Field(default=False, description="Can be used by Vehicles")
    combatvehicle: Optional[bool] = Field(default=False, description="Can be used by Combat Vehicles")
    dropship: Optional[bool] = Field(default=False, description="Can be used by Dropship")
    aerospace: Optional[bool] = Field(default=False, description="Can be used by Aerospace")


class WeaponItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bayType: Optional[str] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    canSplit: Optional[bool] = Field(description="", default=None)
    clusterSize: Optional[int] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    crew: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    damage: Optional[dict] = Field(description="", default=None)
    explosive: Optional[bool] = Field(description="", default=None)
    extAV: Optional[float] = Field(description="", default=None)
    heat: Optional[int] = Field(description="", default=None)
    longAV: Optional[float] = Field(description="", default=None)
    longRange: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    medAV: Optional[float] = Field(description="", default=None)
    mediumRange: Optional[int] = Field(description="", default=None)
    minimumRange: Optional[int] = Field(description="", default=None)
    shortAV: Optional[float] = Field(description="", default=None)
    shortRange: Optional[int] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)
    supportVehicleSlots: Optional[int] = Field(description="", default=None)

class OtherItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bayType: Optional[str] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)
    supportVehicleSlots: Optional[int] = Field(description="", default=None)

class CockpitItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bvModifier: Optional[float] = Field(description="", default=None)
    cockpitType: Optional[str] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)

class EnhancementItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class WeaponBayItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bayType: Optional[str] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    damage: Optional[dict] = Field(description="", default=None)
    heat: Optional[int] = Field(description="", default=None)
    longRange: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    mediumRange: Optional[int] = Field(description="", default=None)
    shortRange: Optional[int] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class ArmorItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    armorBVModifier: Optional[float] = Field(description="", default=None)
    armorPointsModifier: Optional[float] = Field(description="", default=None)
    armorType: Optional[str] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    displayOrder: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    spreadable: Optional[bool] = Field(description="", default=None)

class MyomerItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    massdivisor: Optional[int] = Field(description="", default=None)
    myomerType: Optional[str] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)

class ManipulatorItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    shortName: Optional[str] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)

class ConversionItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class StructureItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    bvModifier: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    massModifier: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    structureType: Optional[str] = Field(description="", default=None)

class EngineItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    assignedSlots: Optional[dict] = Field(description="", default=None)
    bvModifier: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    displayName: Optional[str] = Field(description="", default=None)
    engineClass: Optional[int] = Field(description="", default=None)
    engineRatingMod: Optional[float] = Field(description="", default=None)
    includedHeatSinks: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    powerAmplifierNeeded: Optional[bool] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class GyroItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bvModifier: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    displayName: Optional[str] = Field(description="", default=None)
    gyroType: Optional[str] = Field(description="", default=None)
    mass: Optional[int] = Field(description="", default=None)
    massModifier: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)

class BayItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    crew: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class HeatSinkItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class AmmoItem(BaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    ammoRatio: Optional[float] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[int] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    defensive: Optional[bool] = Field(description="", default=None)
    equipName: Optional[str] = Field(description="", default=None)
    kgPerShot: Optional[float] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    rackSize: Optional[int] = Field(description="", default=None)
    rulesRefs: Optional[str] = Field(description="", default=None)
    short: Optional[int] = Field(description="", default=None)
    shots: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)

class EquipmentItem(BaseModel):
    id: Optional[str] = Field(description="", default=None)
    equipmentType: Optional[str] = Field(description="", default=None)
    equipmentTypeId: Optional[int] = Field(description="", default=None)
    name: Optional[str] = Field(description="", default=None)
    techRating: Optional[str] = Field(description="", default=None)
    techbase: Optional[str] = Field(description="", default=None)
    techbaseId: Optional[int] = Field(description="", default=None)
    type: Optional[EquipmentTypeData] = Field(description="", default=None)
    unitTypes: Optional[EquipmentUnitTypes] = Field(description="", default=None)
    version: Optional[float] = Field(description="", default=None)
    metadata: Optional[dict] = Field(description="", default=None)
    rulesLevel: Optional[int] = Field(description="", default=None)
    item: Optional[Union[WeaponItem, OtherItem, CockpitItem, AmmoItem, HeatSinkItem, BayItem, GyroItem, EngineItem,
    StructureItem, ConversionItem, ArmorItem, ManipulatorItem, MyomerItem, WeaponBayItem,
    EnhancementItem]] = Field(description="", default=None)

    @field_validator('item', mode='before')
    def validate_item_type(cls, v):
        if v['equipmentTypeId'] == EquipmentType.weapon:
            return WeaponItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.armor:
            return ArmorItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.structure:
            return StructureItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.conversion:
            return ConversionItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.cockpit:
            return CockpitItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.gyro:
            return GyroItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.engine:
            return EngineItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.other:
            return OtherItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.ammo:
            return AmmoItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.heatsink:
            return HeatSinkItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.bay:
            return BayItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.myomer:
            return MyomerItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.weaponbay:
            return WeaponBayItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.enhancement:
            return EnhancementItem(**v)
        elif v['equipmentTypeId'] == EquipmentType.manipulator:
            return ManipulatorItem(**v)
        else:
            raise ValueError('Invalid Equipment Item Type')

# Response Item
class DataResultItem(BaseModel):
    currentPage: int = Field(description="Current page number", default=0)
    totalPages: int = Field(description="Total Pages", default=0)
    itemsPerPage: int = Field(description="Items per page", default=50, ge=10, le=200)
    totalItems: int = Field(description="Total items", default=0)
    items: List[Union[EquipmentItem, UnitData, BasicItem, Dict, MULUnitItem, BoxsetItem]] = Field(description="Returned items",
                                                                                      default=[])
    status: str = Field(description="Status of the operation", default=None)
    message: str = Field(description="Message", default=None)
