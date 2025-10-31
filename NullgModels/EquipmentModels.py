## Equipment BaseModels
from typing import Optional, List, Union, Dict

from pydantic import Field, field_validator, ValidationInfo

from NullgModels.Constants import FIELD_EQUIPMENT_TYPE_ID
from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import EquipmentType


class EquipmentAlphaStrike(NullGBaseModel):
    extreme: Optional[List[float]] = Field(description="Extreme range damage values", default=None)
    long: Optional[List[float]] = Field(description="Long range damage values", default=None)
    medium: Optional[List[float]] = Field(description="Medium range damage values", default=None)
    short: Optional[List[float]] = Field(description="Short range damage values", default=None)
    tc: Optional[bool] = Field(description="Can this use a Targeting Computer", default=None)
    specials: Optional[List[str]] = Field(description="List of specials abilities conferred by this equipment",
                                          default=None)


class EquipmentTypeData(NullGBaseModel):
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
    isInfNonPen: Optional[bool] = Field(description="Does this count as non-penetrating against infantry",
                                        default=False)
    isInfantry: Optional[bool] = Field(description="Does this count as an infantry", default=False)
    isLPMEnabled: Optional[bool] = Field(description="Can a Pulse Laser Modular be used", default=False)
    isLegAttack: Optional[bool] = Field(description="Does this confer the Leg Attack ability", default=False)
    isMechanized: Optional[bool] = Field(description="Does this confer the Mechanized ability", default=False)
    isMelee: Optional[bool] = Field(description="Is this a melee verse ranged weapon", default=False)
    isMisc: Optional[bool] = Field(
        description="Is this miscellaneous equipment, does not count as a weapon or defensive", default=False)
    isMissile: Optional[bool] = Field(description="Is this a missile type", default=False)
    isOneShot: Optional[bool] = Field(description="Is this a one-shot weapon", default=False)
    isPPCCapacitorEnabled: Optional[bool] = Field(description="Can a PPC Capacitor be paired", default=False)
    isPair: Optional[bool] = Field(description="Does this come in pairs, like claws or talons", default=False)
    isPhysical: Optional[bool] = Field(description="Is this a physical weapon like Swords", default=False)
    isPulse: Optional[bool] = Field(description="Is this a pulse weapon", default=False)
    isRapidFire: Optional[bool] = Field(description="Does this fire multiple 'shots' like Ultra/Rotary ACs",
                                        default=False)
    isSingleHex: Optional[bool] = Field(description="Single Hex range", default=False)
    isSubCapital: Optional[bool] = Field(description="Is this Sub-capital", default=False)
    isSwarmAttack: Optional[bool] = Field(description="Does this confer the Swam Attack ability", default=False)
    isSwitchable: Optional[bool] = Field(description="", default=False)
    isTrackedEquipment: Optional[bool] = Field(description="Does this item get tracked on the record sheet",
                                               default=False)
    isTurret: Optional[bool] = Field(description="Is this a turret", default=False)
    isUnique: Optional[bool] = Field(description="Is this item limited to 1", default=False)
    isVariable: Optional[bool] = Field(description="Deos this have variable damage", default=False)
    isVariableCrit: Optional[bool] = Field(description="Does this equipment have variable critical slot count",
                                           default=False)
    isVariableMass: Optional[bool] = Field(description="Does this equipment have variable mass", default=False)
    isWeapon: Optional[bool] = Field(description="Is the considered a weapon", default=False)
    useTargetingComputer: Optional[bool] = Field(description="Can this use a targeting computer", default=False)


class EquipmentUnitTypes(NullGBaseModel):
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


class BaseEquipmentItem(NullGBaseModel):
    alphaStrike: Optional[EquipmentAlphaStrike] = Field(description="", default=None)
    bv: Optional[float] = Field(description="", default=None)
    cost: Optional[float] = Field(description="", default=None)
    criticalSlots: Optional[int] = Field(description="", default=None)
    mass: Optional[float] = Field(description="", default=None)
    slots: Optional[int] = Field(description="", default=None)
    sortOrder: Optional[int] = Field(description="", default=None)
    vehicleSlots: Optional[int] = Field(description="", default=None)
    supportVehicleSlots: Optional[int] = Field(description="", default=None)


class WeaponItem(BaseEquipmentItem):
    canSplit: Optional[bool] = Field(description="", default=None)
    clusterSize: Optional[int] = Field(description="", default=None)
    bayType: Optional[str] = Field(description="", default=None)
    crew: Optional[int] = Field(description="", default=None)
    damage: Optional[dict] = Field(description="", default=None)
    explosive: Optional[bool] = Field(description="", default=None)
    extAV: Optional[float] = Field(description="", default=None)
    heat: Optional[int] = Field(description="", default=None)
    longAV: Optional[float] = Field(description="", default=None)
    longRange: Optional[int] = Field(description="", default=None)
    medAV: Optional[float] = Field(description="", default=None)
    mediumRange: Optional[int] = Field(description="", default=None)
    minimumRange: Optional[int] = Field(description="", default=None)
    shortAV: Optional[float] = Field(description="", default=None)
    shortRange: Optional[int] = Field(description="", default=None)


class OtherItem(BaseEquipmentItem):
    bayType: Optional[str] = Field(description="", default=None)


class CockpitItem(BaseEquipmentItem):
    bvModifier: Optional[float] = Field(description="", default=None)
    cockpitType: Optional[str] = Field(description="", default=None)


class EnhancementItem(BaseEquipmentItem):
    pass


class WeaponBayItem(BaseEquipmentItem):
    bayType: Optional[str] = Field(description="", default=None)
    damage: Optional[dict] = Field(description="", default=None)
    heat: Optional[int] = Field(description="", default=None)
    longRange: Optional[int] = Field(description="", default=None)
    mediumRange: Optional[int] = Field(description="", default=None)
    shortRange: Optional[int] = Field(description="", default=None)


class ArmorItem(BaseEquipmentItem):
    armorBVModifier: Optional[float] = Field(description="", default=None)
    armorPointsModifier: Optional[float] = Field(description="", default=None)
    armorType: Optional[str] = Field(description="", default=None)
    displayOrder: Optional[int] = Field(description="", default=None)
    spreadable: Optional[bool] = Field(description="", default=None)


class MyomerItem(BaseEquipmentItem):
    massdivisor: Optional[int] = Field(description="", default=None)
    myomerType: Optional[str] = Field(description="", default=None)


class ManipulatorItem(BaseEquipmentItem):
    shortName: Optional[str] = Field(description="", default=None)


class ConversionItem(BaseEquipmentItem):
    pass


class StructureItem(BaseEquipmentItem):
    bvModifier: Optional[float] = Field(description="", default=None)
    massModifier: Optional[float] = Field(description="", default=None)
    structureType: Optional[str] = Field(description="", default=None)


class EngineItem(BaseEquipmentItem):
    assignedSlots: Optional[Dict[str, int]] = Field(description="", default=None)
    bvModifier: Optional[float] = Field(description="", default=None)
    displayName: Optional[str] = Field(description="", default=None)
    engineClass: Optional[int] = Field(description="", default=None)
    engineRatingMod: Optional[float] = Field(description="", default=None)
    includedHeatSinks: Optional[int] = Field(description="", default=None)
    powerAmplifierNeeded: Optional[bool] = Field(description="", default=None)


class GyroItem(BaseEquipmentItem):
    bvModifier: Optional[float] = Field(description="", default=None)
    displayName: Optional[str] = Field(description="", default=None)
    gyroType: Optional[str] = Field(description="", default=None)
    massModifier: Optional[float] = Field(description="", default=None)


class BayItem(BaseEquipmentItem):
    crew: Optional[int] = Field(description="", default=None)


class HeatSinkItem(BaseEquipmentItem):
    pass


class AmmoItem(BaseEquipmentItem):
    ammoRatio: Optional[float] = Field(description="", default=None)
    defensive: Optional[bool] = Field(description="", default=None)
    equipName: Optional[str] = Field(description="", default=None)
    kgPerShot: Optional[float] = Field(description="", default=None)
    rackSize: Optional[int] = Field(description="", default=None)
    rulesRefs: Optional[str] = Field(description="", default=None)
    short: Optional[int] = Field(description="", default=None)
    shots: Optional[float] = Field(description="", default=None)


class EquipmentItem(NullGBaseModel):
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

    @field_validator('item', mode='after')
    @classmethod
    def validate_item_type(cls, v: Dict, info: ValidationInfo):
        if v is not None and isinstance(v, dict):
            if FIELD_EQUIPMENT_TYPE_ID in info.data and isinstance(info.data[FIELD_EQUIPMENT_TYPE_ID], int):
                try:
                    thisEquipmentType = EquipmentType(info.data[FIELD_EQUIPMENT_TYPE_ID])
                except ValueError as e:
                    raise e

                equipmentTypesMap = {
                    EquipmentType.weapon: WeaponItem,
                    EquipmentType.other: OtherItem,
                    EquipmentType.armor: ArmorItem,
                    EquipmentType.cockpit: CockpitItem,
                    EquipmentType.structure: StructureItem,
                    EquipmentType.engine: EngineItem,
                    EquipmentType.conversion: ConversionItem,
                    EquipmentType.manipulator: ManipulatorItem,
                    EquipmentType.gyro: GyroItem,
                    EquipmentType.ammo: AmmoItem,
                    EquipmentType.heatsink: HeatSinkItem,
                    EquipmentType.bay: BayItem,
                    EquipmentType.myomer: MyomerItem,
                    EquipmentType.enhancement: EnhancementItem,
                    EquipmentType.weaponbay: WeaponBayItem,
                }

                try:
                    return equipmentTypesMap[thisEquipmentType](**v)
                except KeyError:
                    raise ValueError('Invalid equipment type')
            else:
                raise ValueError('Equipment Item Type does not exist')
        else:
            return v
