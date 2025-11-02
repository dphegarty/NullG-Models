## Equipment BaseModels
from typing import Optional, List, Union, Dict

from pydantic import Field, field_validator, ValidationInfo, BaseModel

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


class EquipmentTypeData(BaseModel):
    """
    Data class for equipment type information.

    Key characteristics about the equipment.
    """
    isBeagleActiveProbe: bool = Field(description="", default=False, examples=[True, False])
    isInfantryEncumbered: bool = Field(description="Does this encumber infantry", default=False, examples=[True, False])
    isECM: bool = Field(description="", default=False, examples=[True, False])
    isAngelECM: bool = Field(description="", default=False, examples=[True, False])
    isWatchdog: bool = Field(description="", default=False, examples=[True, False])
    isNOVA: bool = Field(description="", default=False, examples=[True, False])
    isBloodhound: bool = Field(description="", default=False, examples=[True, False])
    isEWEquipment: bool = Field(description="", default=False, examples=[True, False])
    isMiscType: bool = Field(description="", default=False, examples=[True, False])
    isBAManipulator: bool = Field(description="", default=False, examples=[True, False])
    isTAG: bool = Field(description="", default=False, examples=[True, False])
    isDefensive: bool = Field(description="Is this considered defensive equipment", default=False, examples=[True, False])
    isDisplayed: bool = Field(description="Show this be displayed on a record sheet", default=False, examples=[True, False])
    isEditable: bool = Field(description="Is this an editable critical slot", default=False, examples=[True, False])
    isEquipment: bool = Field(description="Is this a Equipment verse a weapon", default=False, examples=[True, False])
    isExplosive: bool = Field(description="Is Explosive", default=False, examples=[True, False])
    isFixed: bool = Field(description="Are the critical slots fixed and cannot be move around", default=False, examples=[True, False])
    isHittable: bool = Field(description="Are these critical slots damagable", default=False, examples=[True, False])
    isLPMEnabled: bool = Field(description="Can a Pulse Laser Modular be used", default=False, examples=[True, False])
    isLegAttack: bool = Field(description="Does this confer the Leg Attack ability", default=False, examples=[True, False])
    isMechanized: bool = Field(description="Does this confer the Mechanized ability", default=False, examples=[True, False])
    isMelee: bool = Field(description="Is this a melee verse ranged weapon", default=False, examples=[True, False])
    isMisc: bool = Field(
        description="Is this miscellaneous equipment, does not count as a weapon or defensive", default=False, examples=[True, False])
    isPair: bool = Field(description="Does this come in pairs, like claws or talons", default=False, examples=[True, False])
    isSingleHex: bool = Field(description="Single Hex range", default=False, examples=[True, False])
    isSwarmAttack: bool = Field(description="Does this confer the Swam Attack ability", default=False, examples=[True, False])
    isTrackedEquipment: bool = Field(description="Does this item get tracked on the record sheet",
                                               default=False, examples=[True, False])
    isTurret: bool = Field(description="Is this a turret", default=False, examples=[True, False])
    isUnique: bool = Field(description="Is this item limited to 1", default=False, examples=[True, False])
    isVariable: bool = Field(description="Deos this have variable damage", default=False, examples=[True, False])
    isVariableCrit: bool = Field(description="Does this equipment have variable critical slot count",
                                           default=False, examples=[True, False])
    isVariableMass: bool = Field(description="Does this equipment have variable mass", default=False, examples=[True, False])
    isWeapon: bool = Field(description="Is the considered a weapon", default=False, examples=[True, False])


class WeaponClassification(BaseModel):
    isInfantryBurst: bool = Field(description="Is consider burst weapon against infantry", default=False, examples=[True, False])
    isInfantryNonPen: bool = Field(description="Does this count as non-penetrating against infantry", default=False, examples=[True, False])
    isInfantryWeapon: bool = Field(description="Does this count as an infantry", default=False, examples=[True, False])
    isMML: bool = Field(description="", default=False, examples=[True, False])
    isATM: bool = Field(description="", default=False, examples=[True, False])
    isISCenturionWeaponSystem: bool = Field(description="", default=False, examples=[True, False])
    isLRT: bool = Field(description="", default=False, examples=[True, False])
    isSRT: bool = Field(description="", default=False, examples=[True, False])
    isSRM: bool = Field(description="", default=False, examples=[True, False])
    isLRM: bool = Field(description="", default=False, examples=[True, False])
    isMRM: bool = Field(description="", default=False, examples=[True, False])
    isLBX: bool = Field(description="", default=False, examples=[True, False])
    isUltra: bool = Field(description="", default=False, examples=[True, False])
    isRotary: bool = Field(description="", default=False, examples=[True, False])
    isRocketLauncher: bool = Field(description="", default=False, examples=[True, False])
    isAERO: bool = Field(description="", default=False, examples=[True, False])
    isStreak: bool = Field(description="", default=False, examples=[True, False])
    isiATM: bool = Field(description="", default=False, examples=[True, False])
    isAMS: bool = Field(description="Is the an Anti-Missile System", default=False, examples=[True, False])
    isAntiAir: bool = Field(description="Is this Anti-Air", default=False, examples=[True, False])
    isAntiInfantry: bool = Field(description="Is this Anti-Infantry", default=False, examples=[True, False])
    isApolloEnabled: bool = Field(description="Can an Apollo MRM FCS be used", default=False, examples=[True, False])
    isArtemisEnabled: bool = Field(description="Can an Artemis (IV, V) be used", default=False, examples=[True, False])
    isArtillery: bool = Field(description="Is this an artillery piece", default=False, examples=[True, False])
    isArtilleryCannon: bool = Field(description="Is the an artillery cannon", default=False, examples=[True, False])
    isBallistic: bool = Field(description="Is this a Ballistic type weapon", default=False, examples=[True, False])
    isCapital: bool = Field(description="Is this a capital weapon", default=False, examples=[True, False])
    isCluster: bool = Field(description="Is this a cluster weapon", default=False, examples=[True, False])
    isDirect: bool = Field(description="Is this a Direct fire weapon", default=False, examples=[True, False])
    isEnergy: bool = Field(description="Is this an Energy weapon", default=False, examples=[True, False])
    isFlame: bool = Field(description="Is Flame weapon", default=False, examples=[True, False])
    isHeatCausing: bool = Field(description="Is Heat causing, example plasma", default=False, examples=[True, False])
    isHeavyWeapon: bool = Field(description="Is this a heavy weapon for infantry", default=False, examples=[True, False])
    isIndirect: bool = Field(description="Is this indirect", default=False, examples=[True, False])
    isPhysical: bool = Field(description="Is this a physical weapon like Swords", default=False, examples=[True, False])
    isPulse: bool = Field(description="Is this a pulse weapon", default=False, examples=[True, False])
    isRapidFire: bool = Field(description="Does this fire multiple 'shots' like Ultra/Rotary ACs",
                                        default=False, examples=[True, False])
    isMissile: bool = Field(description="Is this a missile type", default=False, examples=[True, False])
    isOneShot: bool = Field(description="Is this a one-shot weapon", default=False, examples=[True, False])
    isPPCCapacitorEnabled: bool = Field(description="Can a PPC Capacitor be paired", default=False, examples=[True, False])
    isSubCapital: bool = Field(description="Is this Sub-capital", default=False, examples=[True, False])
    isSwitchable: bool = Field(description="", default=False, examples=[True, False])
    useTargetingComputer: bool = Field(description="Can this use a targeting computer", default=False, examples=[True, False])


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
    capacitorBv: Optional[int] = Field(
        description="Unique to Inner Sphere PPCs. This is the additional BV cost for"
                    "attaching a capacitor to the PPC.",
        default=0,
        examples=[0, 1, 2]
    )
    capacitorDamage: Optional[int] = Field(
        description="Unique to Inner Sphere PPCs. This is the damage when a"
                    "capacitor attached to a PPC is destroyed by a critical hit",
        default=0,
        examples=[0, 1, 2]
    )
    classification: WeaponClassification = Field(description="Weapon classification data", default_factory=WeaponClassification)

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

    @field_validator('item', mode='before')
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
