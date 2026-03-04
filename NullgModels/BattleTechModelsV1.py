from __future__ import annotations

from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


# ----------------------------
# Shared / utility models
# ----------------------------

class MongoObjectId(BaseModel):
    """Mongo-style object id wrapper: {'$oid': '...'}"""
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    oid: str = Field(alias="$oid")


class ArmorLocationEntry(BaseModel):
    model_config = ConfigDict(extra="allow")

    armor: str = ""
    location: str
    value: int


class CriticalLocationEntry(BaseModel):
    model_config = ConfigDict(extra="allow")

    location: str
    slots: List[str]


class EquipmentEntry(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: Union[UUID, str]
    location: str
    name: str
    options: str = ""
    type: str  # e.g. "equipment", "ammo"


class Metadata(BaseModel):
    model_config = ConfigDict(extra="allow")

    searchable: Optional[bool] = None


class SummaryData(BaseModel):
    """
    Seen as:
      "summary_data": { "ammo": { "LRM 15": 48 } }
    """
    model_config = ConfigDict(extra="allow")

    ammo: Optional[Dict[str, int]] = None


class ExtraOptions(BaseModel):
    """
    Many boolean flags under totalWar.extraOptions
    """
    model_config = ConfigDict(extra="allow")

    hasArmoredMotiveSystem: Optional[bool] = None
    hasCamoSystem: Optional[bool] = None
    hasDroneOperatingSystem: Optional[bool] = None
    hasDuneBuggy: Optional[bool] = None
    hasEnvironmentalSealing: Optional[bool] = None
    hasFullyAmphibious: Optional[bool] = None
    hasImprovedJumpJets: Optional[bool] = None
    hasIndustrialTripleStrength: Optional[bool] = None
    hasJumpBooster: Optional[bool] = None
    hasLimitedAmphibious: Optional[bool] = None
    hasMagneticClamp: Optional[bool] = None
    hasMASC: Optional[bool] = None
    hasMechanicalJumpBooster: Optional[bool] = None
    hasMyomerBooster: Optional[bool] = None
    hasPartialWing: Optional[bool] = None
    hasRadicalHeatSystem: Optional[bool] = None
    hasStealthArmor: Optional[bool] = None
    hasSuperCharger: Optional[bool] = None
    hasTripleStrength: Optional[bool] = None
    hasVoidSignature: Optional[bool] = None
    isAirborne: Optional[bool] = None
    isVTOL: Optional[bool] = None


# ----------------------------
# TotalWar model group
# ----------------------------

class TotalWar(BaseModel):
    """
    Consolidates the Total War / Classic BT sheet block.

    Notes:
    - dataset includes both snake_case and camelCase duplicates
      e.g. armorlocations (dict) and armorLocations (list).
    - same for criticallocations vs criticalLocations, unit_type vs unitType vs unittype, etc.
    """
    model_config = ConfigDict(extra="allow")

    Add: Optional[str] = None

    armor: Optional[str] = None
    armorfactor: Optional[int] = None
    armorfactormax: Optional[int] = None

    # Duplicate representations
    armorlocations: Optional[Dict[str, int]] = None
    armorLocations: Optional[List[ArmorLocationEntry]] = None

    armorTechbase: Optional[str] = None
    available_era: Optional[List[int]] = None

    barrating: Optional[int] = None
    bv: Optional[int] = None

    cockpit: Optional[str] = None
    config: Optional[str] = None

    constructionInvalid: Optional[List[Any]] = None
    constructionValidated: Optional[bool] = None

    copyright_trademark: Optional[str] = None

    criticalFreeHeatSinks: Optional[int] = None

    criticallocations: Optional[Dict[str, List[str]]] = None
    criticalLocations: Optional[List[CriticalLocationEntry]] = None

    engine: Optional[str] = None
    engineRating: Optional[int] = None
    engineTechbase: Optional[str] = None
    engineType: Optional[str] = None

    # equipment_data is a dict keyed by location -> list[str]
    equipment_data: Optional[Dict[str, List[str]]] = None
    equipmentList: Optional[List[EquipmentEntry]] = None

    era: Optional[int] = None
    extraOptions: Optional[ExtraOptions] = None

    fire_control: Optional[str] = None
    gyro: Optional[str] = None

    heat_sinks: Optional[str] = None
    heatSinks: Optional[int] = None
    heatSinksEngineBase: Optional[int] = None
    heatSinksOmniBase: Optional[int] = None
    heatSinksTechbase: Optional[str] = None
    heatSinksType: Optional[int] = None

    id: Optional[Union[UUID, str]] = None

    intro: Optional[int] = None
    into: Optional[int] = None  # observed typo variant

    jump_mp: Optional[int] = None
    jumpjetType: Optional[int] = None

    mass: Optional[int] = None
    metadata: Optional[Metadata] = None
    model: Optional[str] = None

    motion_type: Optional[str] = None

    myomer: Optional[str] = None
    myomerTechbase: Optional[str] = None

    name: Optional[str] = None
    pv: Optional[int] = None
    role: Optional[int] = None
    rules_level: Optional[int] = None
    rules_levels: Optional[List[Any]] = None

    source: Optional[str] = None
    sourceUri: Optional[str] = None

    structure: Optional[str] = None
    structureTechbase: Optional[str] = None

    summary_data: Optional[SummaryData] = None

    techbase: Optional[str] = None
    trooper_count: Optional[int] = None

    unitCategory: Optional[int] = None

    unit_data_source: Optional[str] = None
    unit_data_source_uri: Optional[str] = None
    unitDataSourceUri: Optional[str] = None

    unit_type: Optional[str] = None
    unitType: Optional[str] = None
    unittype: Optional[str] = None

    unitSubType: Optional[str] = None
    version: Optional[int] = None

    walk_mp: Optional[int] = None
    run_mp: Optional[int] = None

    weapons: Optional[int] = None

    # weapons_data is a dict keyed by location -> list of rows; rows are lists of strings/numbers-as-strings
    weapons_data: Optional[Dict[str, List[List[Any]]]] = None

    weightclass: Optional[int] = None


# ----------------------------
# BV (Battle Value) model group
# ----------------------------

class CostItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    cost: Union[int, float]
    name: str


class BVResults(BaseModel):
    """
    BV / construction math details. Includes mixed naming (Name vs name, Mass vs modified_mass, etc.)
    and mixed-type lists like equipmentCostTable.
    """
    model_config = ConfigDict(extra="allow")

    aesLocations: Optional[List[Any]] = None
    AESModifier: Optional[Union[int, float]] = None

    ammoCost: Optional[Union[int, float]] = None
    armorBV: Optional[Union[int, float]] = None
    ArmorData: Optional[Union[int, float]] = None
    ArmorFactor: Optional[Union[int, float]] = None
    ArmorTypeModifier: Optional[Union[int, float]] = None

    armoredComponents: Optional[int] = None
    armoredComponentsBV: Optional[Union[int, float]] = None

    BattleValue: Optional[Union[int, float]] = None
    bpods: Optional[int] = None
    bv_inaccurate: Optional[bool] = None

    CockpitModifier: Optional[Union[int, float]] = None
    coolantPods: Optional[int] = None

    DefensiveBattleRating: Optional[Union[int, float]] = None
    DefensiveEquipmentData: Optional[Union[int, float]] = None
    defensiveEquipmentValue: Optional[Union[int, float]] = None
    DefensiveFactor: Optional[Union[int, float]] = None
    defensiveModifier: Optional[Union[int, float]] = None

    Diff: Optional[Union[int, float]] = None
    EngineModifier: Optional[Union[int, float]] = None

    era: Optional[int] = None
    explosiveAmmoFactor: Optional[Union[int, float]] = None
    fireControlModifier: Optional[Union[int, float]] = None

    GyroCost: Optional[Union[int, float]] = None
    GyroModifier: Optional[Union[int, float]] = None

    hasArmoredGloves: Optional[Union[int, float]] = None
    hasBasicManipulators: Optional[Union[int, float]] = None
    hasBattleClaws: Optional[Union[int, float]] = None
    hasProtoDoubleHeatSinks: Optional[Union[int, float]] = None

    heatEfficiency: Optional[Union[int, float]] = None

    id: Optional[Union[UUID, str]] = None
    internalStructureBV: Optional[Union[int, float]] = None
    InternalStructureData: Optional[Union[int, float]] = None
    InternalStructureFactor: Optional[Union[int, float]] = None
    InternalStructureModifier: Optional[Union[int, float]] = None

    longrangedamage: Optional[Union[int, float]] = None
    mediumrangedamage: Optional[Union[int, float]] = None
    shortrangedamage: Optional[Union[int, float]] = None

    miscOffensiveCosts: Optional[Union[int, float]] = None

    model: Optional[str] = None
    modified_mass: Optional[Union[int, float]] = None

    name: Optional[str] = None
    Name: Optional[str] = None
    Mass: Optional[Union[int, float]] = None

    OffensiveBattleRating: Optional[Union[int, float]] = None
    offensiveModifier: Optional[Union[int, float]] = None

    OfficalBV: Optional[Union[int, float]] = None  # spelling in dataset
    rules_level: Optional[int] = None

    speedFactor: Optional[Union[int, float]] = None
    targetModifier: Optional[Union[int, float]] = None
    tsmModifier: Optional[Union[int, float]] = None

    turretCostTable: Optional[Dict[str, Any]] = None

    unit_type: Optional[str] = None
    UnitTypeModifier: Optional[Union[int, float]] = None

    validated: Optional[bool] = None

    weaponCount: Optional[int] = None
    weaponsCost: Optional[Union[int, float]] = None
    weaponsHeat: Optional[Union[int, float]] = None
    weightclass: Optional[int] = None

    # Mixed: ["UUID", {"cost":..., "name":...}, "UUID", {"cost":..., "name":...}, ...]
    equipmentCostTable: Optional[List[Union[str, CostItem]]] = None


# ----------------------------
# Alpha Strike model group
# ----------------------------

class SpecialDamageEntry(BaseModel):
    """
    Note: dataset has an occasional typo key like 'medium:' in one record,
    so we allow extra keys here.
    """
    model_config = ConfigDict(extra="allow")

    name: str
    count: Union[int, float]
    short: Union[int, float]
    medium: Union[int, float]
    long: Union[int, float]
    extreme: Union[int, float]
    inTurret: bool = False


class AlphaStrike(BaseModel):
    model_config = ConfigDict(extra="allow")

    formattedSpecials: Optional[List[str]] = None
    specials: Optional[List[str]] = None
    specialsDamage: Optional[List[SpecialDamageEntry]] = None

    arcFormatedSpecials: Optional[List[Any]] = None
    arcDamageMaps: Optional[List[Any]] = None
    arcversion: Optional[int] = None

    aero: Optional[bool] = None
    trooperCount: Optional[int] = None
    skill: Optional[int] = None
    useOfficialPoints: Optional[bool] = None

    calculatedPV: Optional[int] = None
    officialPV: Optional[int] = None

    armorThreshold: Optional[int] = None
    isLAM: Optional[bool] = None
    isLargeUnit: Optional[bool] = None

    damage_short: Optional[Union[int, float]] = None
    damage_medium: Optional[Union[int, float]] = None
    damage_long: Optional[Union[int, float]] = None
    damage_extreme: Optional[Union[int, float]] = None

    # sometimes present (seen in keys list)
    damageSpecial_extreme: Optional[Union[int, float]] = None

    overheat: Optional[Union[int, float]] = None
    movementMode: Optional[str] = None

    skillDifference: Optional[Union[int, float]] = None
    skillPoints: Optional[Union[int, float]] = None

    id: Optional[Union[UUID, str]] = None
    name: Optional[str] = None
    model: Optional[str] = None

    baseUnitType: Optional[str] = None
    unitType: Optional[str] = None

    size: Optional[int] = None
    walk: Optional[int] = None
    jump: Optional[int] = None

    armor: Optional[Union[int, float]] = None
    structure: Optional[Union[int, float]] = None

    armed: Optional[bool] = None
    hasC3System: Optional[bool] = None

    role: Optional[int] = None
    ttm: Optional[Union[int, float]] = None
    version: Optional[int] = None


class AlphaStrikeResults(BaseModel):
    model_config = ConfigDict(extra="allow")

    turretSpecials: Optional[List[Any]] = None

    id: Optional[Union[UUID, str]] = None
    baseUnitType: Optional[str] = None

    armorFactor: Optional[Union[int, float]] = None
    structureMod: Optional[Union[int, float]] = None
    rawASStructure: Optional[Union[int, float]] = None
    asStructure: Optional[Union[int, float]] = None

    heatGenerated: Optional[Union[int, float]] = None
    longHeatGenerated: Optional[Union[int, float]] = None

    subtotalDamageMap: Optional[Dict[str, Union[int, float]]] = None
    damageMap: Optional[Dict[str, Union[int, float]]] = None

    weaponsTracking: Optional[List[Any]] = None

    rawMovementHeat: Optional[Union[int, float]] = None
    heatDissipation: Optional[Union[int, float]] = None
    additionalHeat: Optional[Union[int, float]] = None
    movementHeat: Optional[Union[int, float]] = None

    troopFactor: Optional[Union[int, float]] = None

    heatModifiedDamage: Optional[Dict[str, Union[int, float]]] = None
    adjustedDamageMap: Optional[Dict[str, Union[int, float]]] = None

    overheatValue: Optional[Union[int, float]] = None
    overHeatRange: Optional[str] = None
    overHeatDiff: Optional[Union[int, float]] = None

    attackDamageFactor: Optional[Union[int, float]] = None
    sizeFactor: Optional[Union[int, float]] = None
    overheatFactor: Optional[Union[int, float]] = None

    offensiveSpecialAbilityFactor: Optional[Union[int, float]] = None
    blanketOffensiveModifier: Optional[Union[int, float]] = None
    offensiveValue: Optional[Union[int, float]] = None

    movementFactor: Optional[Union[int, float]] = None

    groundUnitArmorRatingModifier: Optional[Union[int, float]] = None
    defensiveArmorFactor: Optional[Union[int, float]] = None
    defensiveArmorModifier: Optional[Union[int, float]] = None

    groundUnitStructureRatingModifier: Optional[Union[int, float]] = None
    defensiveStructureFactor: Optional[Union[int, float]] = None

    movementModifier: Optional[Union[int, float]] = None
    additionalDefensiveModifiers: Optional[Union[int, float]] = None
    defensiveFactor: Optional[Union[int, float]] = None

    rawDefensiveInteractionRating: Optional[Union[int, float]] = None
    defensiveInteractionRating: Optional[Union[int, float]] = None

    defensiveSpecialAbilityFactor: Optional[Union[int, float]] = None
    defensiveValue: Optional[Union[int, float]] = None

    agilePoints: Optional[Union[int, float]] = None
    unitForceBonuses: Optional[Union[int, float]] = None
    adjustmentPoints: Optional[Union[int, float]] = None
    skillDifference: Optional[Union[int, float]] = None
    totalPointsAdjustment: Optional[Union[int, float]] = None

    calculationStartTime: Optional[Union[int, float]] = None
    calculationEndTime: Optional[Union[int, float]] = None
    calculationDuration: Optional[Union[int, float]] = None

    # seen in keys list
    ttmDiff: Optional[Union[int, float]] = None


# ----------------------------
# Statistics model group
# ----------------------------

class Statistics(BaseModel):
    model_config = ConfigDict(extra="allow")

    ArmorDataAvg: Optional[Union[int, float]] = None
    ArmorDataMax: Optional[Union[int, float]] = None
    armordatascale: Optional[Union[int, float]] = None

    ArmorFactorAvg: Optional[Union[int, float]] = None
    ArmorFactorMax: Optional[Union[int, float]] = None
    armorfactorscale: Optional[Union[int, float]] = None

    DefensiveBattleRatingAvg: Optional[Union[int, float]] = None
    DefensiveBattleRatingMax: Optional[Union[int, float]] = None
    defscale: Optional[Union[int, float]] = None

    OffensiveBattleRatingAvg: Optional[Union[int, float]] = None
    OffensiveBattleRatingMax: Optional[Union[int, float]] = None
    offscale: Optional[Union[int, float]] = None

    heatEfficiencyAvg: Optional[Union[int, float]] = None
    heatEfficiencyMax: Optional[Union[int, float]] = None
    heatscale: Optional[Union[int, float]] = None

    speedFactorAvg: Optional[Union[int, float]] = None
    speedFactorMax: Optional[Union[int, float]] = None
    speedscale: Optional[Union[int, float]] = None

    weaponsCostAvg: Optional[Union[int, float]] = None
    weaponsCostMax: Optional[Union[int, float]] = None
    weaponscostscale: Optional[Union[int, float]] = None


# ----------------------------
# Root unit document
# ----------------------------

class MigrationUnit(BaseModel):
    """
    Top-level record representing a unit in the dataset.
    """
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mongo_id: MongoObjectId = Field(alias="_id")

    isMap: bool
    appEnabled: bool

    id: Union[UUID, str]
    name: str
    model: str
    fullName: str

    mulId: int
    unitType: str

    era: int
    available_era: List[int]

    rules_level: int
    mass: int

    unitSubType: str
    version: int

    bv: int
    pv: Union[int, float]

    techbase: str
    weightclass: int
    role: int

    # Optional top-level extras
    barcodes: Optional[List[Any]] = None
    notes: Optional[str] = None

    totalWar: TotalWar
    bvResults: BVResults

    alphaStrike: AlphaStrike
    alphaStrikeResults: AlphaStrikeResults

    statistics: Statistics


class MigrationUnitDataset(BaseModel):
    """
    If you want to validate the entire file as one object:
      MigrationUnitDataset(units=data)
    """
    model_config = ConfigDict(extra="allow")

    units: List[MigrationUnit]