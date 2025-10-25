from NullgModels.BattletechModels import *

from pydantic import BaseModel, Field, field_validator

from NullgModels.TotalWarModels import TotalWarEquipmentItem, TotalWarArmorLocation, TotalWarCriticalLocationItem, \
    TotalWarBayExtendedItem, TotalWarBayBaseItem


# TotalWar BaseModels

class UploadTotalWarBaseData(BaseModel):
    # Common across TotalWar variants
    id: str = Field(description="ID of the unit")
    armor: str = Field(description="Armor")
    bv: float = Field(description="Battle Value 2 of the unit")
    config: str = Field(description="Unit configuration")
    constructionInvalid: List[str] = Field(description="List of reason the unit construction is invalid")
    constructionValidated: bool = Field(description="Has the unit construction been validated")
    extraOptions: Dict[str, bool] = Field(description="Extra optional this unit has")
    mass: float = Field(description="Units Mass")
    pv: int = Field(description="Alpha Strike points value")
    source: str = Field(description="Source of the unit information")
    techbase: str = Field(description="Overall unit Technology base")
    version: float = Field(description="Unit data version")
    equipmentList: List[TotalWarEquipmentItem] = Field(description="Equipment, Weapons and Ammunition")
    armorLocations: List[TotalWarArmorLocation] = Field(description="Armor locations and values")
    unitDataSourceUri: str = Field(description="URI of the unit's source information")
    structure: str = Field(description="Internal Structure Type")
    # Shared game/stats metadata
    copyrightTrademark: str = Field(description="Basic Trademark/Copyright")
    runMp: int = Field(description="Units Run movement")
    motionType: str = Field(description="Units motion type")
    productionYear: int = Field(description="Year the unit was first produced")
    rulesLevel: int = Field(description="Rule Level of the unit")
    walkMp: int = Field(description="Units Walk movement")
    productionEra: int = Field(description="Era in which the unit was first produced")
    unitTypeId: int = Field(description="Type of unit")
    unitSubtypeId: int = Field(description="Subtype of unit")
    weightClassId: int = Field(description="Weight Class Id")
    armorFactor: int = Field(description="Units armor factor, the total points of armor")
    armorFactorMax: int = Field(description="Maximum amount of armor that can be mounted on this unit", default=None)


# Tested and Works
class UploadTotalWarBattleMechDataData(UploadTotalWarBaseData):
    armorTechbase: str = Field(description="Armor Technology base")
    cockpit: str = Field(description="Type of Cockpit")
    criticalFreeHeatSinks: int = Field(description="The amount of Critical Free Heat Sinks ")
    engine: str = Field(description="Full Engine description")
    engineRating: int = Field(description="Engine Rating")
    engineTechbase: str = Field(description="Engine Technology base")
    engineType: str = Field(description="Type of engine")
    gyro: str = Field(description="Type of Gyro")
    heatSinks: int = Field(description="Number of Heats the unit has")
    heatSinksTechbase: str = Field(description="Heat Sinks Technology base")
    heatSinksType: int = Field(description="Type of Heat Sink, Single, Double, Laser, Compact")
    myomer: str = Field(description="Type of Myomer")
    myomerTechbase: str = Field(description="Myomer Technology base")
    weapons: int = Field(description="Number of weapons mounted on the unit")
    heatSinksEngineBase: int = Field(description="Number of heat Sinks that are based in the engine")
    heatSinksOmniBase: int = Field(description="Number of Omnipod Heat Sinks.")
    criticalLocations: List[TotalWarCriticalLocationItem] = Field(description="Critical Slot information")
    barRating: int = Field(description="BAR Rating")
    trooperCount: int = Field(description="Number of individuals that make up this unit")
    jumpMp: int = Field(description="Units Jump movement")
    fireControl: str = Field(description="Fire Control")
    jumpjetType: int = Field(description="Jumpjets type")
    roleId: int = Field(description="Role Id")

class UploadTotalWarAerospaceData(UploadTotalWarBaseData):
    cockpit: str = Field(description="Type of Cockpit")
    engineRating: int = Field(description="Engine Rating")
    engineTechbase: str = Field(description="Engine Technology base")
    engineType: str = Field(description="Type of engine")
    fuel: int = Field(description="Fuel")
    transportSpace: Dict[str, int] = Field(description="Types of troop carrying capacity")
    heatSinks: int = Field(description="Number of Heats the unit has")
    heatSinksTechbase: str = Field(description="Heat Sinks Technology base")
    heatSinksType: int = Field(description="Type of Heat Sink, Single, Double, Laser, Compact")
    safeThrust: int = Field(description="Safe Thrust")
    weapons: str = Field(description="Number of weapons mounted on the unit")
    heatSinksOmniBase: int = Field(description="Number of Omnipod Heat Sinks.")
    barRating: int = Field(description="BAR Rating")
    trooperCount: int = Field(description="Number of individuals that make up this unit")
    jumpMp: int = Field(description="Units Jump movement")
    fireControl: str = Field(description="Fire Control")
    roleId: int = Field(description="Role Id")

class UploadTotalWarInfantryData(UploadTotalWarBaseData):
    armorTechbase: str = Field(description="Armor Technology base")
    structureTechbase: str = Field(description="Internal Structure Technology base")
    trooperCount: int = Field(description="Number of individuals that make up this unit")
    jumpMp: int = Field(description="Units Jump movement")
    trooperMass: float = Field(description="Mass per Trooper")
    roleId: int = Field(description="Role Id")
    squads: int = Field(description="Squads in the units")
    squadSize: int = Field(description="Squad size")
    secondaryWeaponTroops: int = Field(description="Number troopers that have secondary weapons")
    isExoskeleton: bool = Field(description="Is this an exoskeleton")

class UploadTotalWarVehicleData(UploadTotalWarBaseData):
    engineRating: int = Field(description="Rating of the engine")
    engineTechbase: str = Field(description="Technology base")
    engineType: str = Field(description="Type of the engine")
    turretType: int = Field(description="Type of the turret type")
    transportSpace: Dict[str, int] = Field(description="Transport space")
    structureTechbase: str = Field(description="Internal Structure Type")
    armorTechbase: str = Field(description="Armor Technology base")
    barRating: int = Field(description="Rating of the bar")
    trooperCount: int = Field(description="Number of individuals that make up this unit")
    jumpMp: int = Field(description="Units Jump movement")
    fireControl: str = Field(description="Units fire control")
    hasControlSystems: bool = Field(description="Has the Control systems")
    heatSinks: int = Field(description="Heat Sinks")
    heatSinksTechbase: str = Field(description="Technology base")
    heatSinksType: int = Field(description="Type of the Heat Sinks")
    heatSinksEngineBase: int = Field(description="Heat Sinks in the Engine")
    heatSinksOmniBase: int = Field(description="Heat Sinks in the Omnipods")
    isTrailer: bool = Field(description="Is this a trailer")
    extraCombatSeats: int = Field(description="Extra Combat Seats")
    jumpjetType: int = Field(description="Type of the Jumpjet type")
    roleId: int = Field(description="Role Id")

class UploadTotalWarDropshipData(UploadTotalWarBaseData):
    bays: List[TotalWarBayExtendedItem] = Field(description="Bays in the unit")
    quarters: List[TotalWarBayBaseItem] = Field(description="Crew quarters in the unit")
    crewValues: List[TotalWarBayBaseItem] = Field(description="Crew values in the unit")
    armorTechbase: str = Field(description="Armor Technology base")
    heatSinks: int = Field(description="Number of Heats the unit has")
    heatSinksTechbase: str = Field(description="Heat Sinks Technology base")
    heatSinksType: int = Field(description="Type of Heat Sink, Single, Double, Laser, Compact")
    structuralIntegrity: int = Field(description="Structural Integrity")
    engineRating: int = Field(description="Engine Rating")
    engineTechbase: str = Field(description="Engine Technology base")
    chassisType: int = Field(description="Type of Cassis")
    cockpit: str = Field(description="Type of Cockpit")
    fuel: int = Field(description="Fuel")
    barRating: int = Field(description="BAR Rating")
    trooperCount: int = Field(description="Number of individuals that make up this unit")
    jumpMp: int = Field(description="Units Jump movement")
    fireControl: str = Field(description="Fire Control")
    roleId: int = Field(description="Role Id")


# Unit BaseModel

class UploadUnitData(BaseModel):
    id: str = Field(description="ID of the unit", title="ID")
    name: str = Field(description="Name of the unit", title="Name")
    model: str = Field(description="Model of the unit", title="Model")
    productionEra: int = Field(description="The era the unit started production")
    mass: float = Field(description="Mass or tonnage of the unit")
    version: float = Field(description="Version of the unit document")
    bv: float = Field(description="Battle Value v2")
    pv: int = Field(description="Alpha Strike points value")
    techbase: str = Field(description="Unit overall technology base")
    mulId: int = Field(description="The corresponding Master Unit List Id")
    weightClassId: int = Field(description="Weight Class Id")
    roleId: int = Field(description="Unit role Id")
    rulesLevel: int = Field(description="Rules Level the unit is part of")
    barcodes: List[str] = Field(description="Barcodes of any boxsets the unit miniature is part of",
                                default=None)
    fullName: str = Field(description="Units full name")
    metadata: Dict[str, bool] = Field(description="Metadata")
    notes: str = Field(description="Any extra notes")
    unitCategory: int = Field(description="Unit category: Official, User Created..")
    factions: List[int] = Field(description="List of Faction Ids that the unit is available to")
    creationSource: str = Field(description="How was the created")
    productionYear: int = Field(description="The year the unit went into production")
    availableEras: List[int] = Field(description="Eras the unit is available in")
    totalWar: Optional[Union[
        UploadTotalWarDropshipData, UploadTotalWarInfantryData, UploadTotalWarAerospaceData, UploadTotalWarBattleMechDataData,
        UploadTotalWarVehicleData]] = Field(description="Total War Data")
    bvResults: Dict[str, Any] = Field(description="Battle Value v2 Calculation Data")
    unitTypeId: int = Field(description="Type of unit")
    unitSubtypeId: int = Field(description="Subtype of unit")

    @field_validator(FIELD_TOTAL_WAR, mode='before')
    def validate_totalwar_type(cls, v: Dict):
        if v is not None and isinstance(v, dict):
            if FIELD_UNIT_TYPE_ID in v and isinstance(v[FIELD_UNIT_TYPE_ID], int):
                try:
                    thisUnitType = UnitType(v[FIELD_UNIT_TYPE_ID])
                except ValueError:
                    raise ValueError('Invalid unit type')

                unitTypesMap = {
                    UnitType.mech: UploadTotalWarBattleMechDataData,
                    UnitType.vehicle: UploadTotalWarVehicleData,
                    UnitType.infantry: UploadTotalWarInfantryData,
                    UnitType.aerospace: UploadTotalWarAerospaceData,
                    UnitType.dropship: UploadTotalWarDropshipData,
                }

                try:
                    return unitTypesMap[thisUnitType](**v)
                except KeyError:
                    raise ValueError('Invalid unit type')
            else:
                raise ValueError('Unit type id field does not exist')
        else:
            return v
