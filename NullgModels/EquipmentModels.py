## Equipment BaseModels
from typing import Optional, List, Union, Dict

from pydantic import Field, field_validator, ValidationInfo, BaseModel

from NullgModels.Constants import FIELD_EQUIPMENT_TYPE
from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import EquipmentType, TechbaseType, UnitSubtype


class EquipmentWeaponDamage(NullGBaseModel):
    """
    Defines damage values for weapons across standard BattleTech range brackets
    and against infantry targets.

    Attributes:
        short: Short range damage value
        medium: Medium range damage value
        long: Long range damage value
        infantry: Infantry damage value
        infantryBurst: Infantry burst damage value
    """
    short: Optional[float] = Field(description="Short range damage value", default=0, examples=[10, 5, 0])
    medium: Optional[float] = Field(description="Medium range damage value", default=0, examples=[25, 10, 0])
    long: Optional[float] = Field(description="Long range damage value", default=0, examples=[5, 15, 0])
    infantry: Optional[float] = Field(description="Infantry damage value", default=0, examples=[0.71, 0.55, 0.16])
    infantryBurst: Optional[float] = Field(description="Infantry burst damage value", default=0, examples=[0.71, 0.55, 0.16])

class EquipmentWeaponRanges(NullGBaseModel):
    """
    Specifies the range brackets (in hexes) for a weapon or piece of equipment.

    Attributes:
        minimum: Minimum range value
        short: Short range value
        medium: Medium range value
        long: Long range value
        infantry: Infantry range value
    """
    minimum: Optional[int] = Field(description="Minimum range value", default=0, examples=[1, 3, 5])
    short: Optional[int] = Field(description="Short range value", default=0, examples=[10, 5, 0])
    medium: Optional[int] = Field(description="Medium range value", default=0, examples=[25, 10, 0])
    long: Optional[int] = Field(description="Long range value", default=0, examples=[5, 15, 0])
    infantry: Optional[int] = Field(description="Infantry range value", default=0, examples=[1, 3, 4])

class EquipmentAlphaStrike(NullGBaseModel):
    """
    Contains statistical data and special abilities for converting this equipment
    to Alpha Strike gameplay mechanics.

    Attributes:
        extreme: Extreme range damage values
        long: Long range damage values
        medium: Medium range damage values
        short: Short range damage values
        artillery: Artillery damage values
        radius: Radius of artillery damage values
        tc: Can this use a Targeting Computer
        specials: List of special abilities conferred by this equipment
    """
    extreme: Optional[List[float]] = Field(description="Extreme range damage values", default=[0.0,0.0,0.0])
    long: Optional[List[float]] = Field(description="Long range damage values", default=[0.0,0.0,0.0])
    medium: Optional[List[float]] = Field(description="Medium range damage values", default=[0.0,0.0,0.0])
    short: Optional[List[float]] = Field(description="Short range damage values", default=[0.0,0.0,0.0])
    artillery: Optional[List[float]] = Field(description="Artillery damage values", default=[0.0,0.0,0.0])
    radius: Optional[int] = Field(description="Radius of artillery damage values", default=0)
    tc: Optional[bool] = Field(description="Can this use a Targeting Computer", default=False)
    specials: Optional[List[str]] = Field(
        description="List of specials abilities conferred by this equipment",
        default=[]
    )


class EquipmentTypeData(BaseModel):
    """
    Data class for equipment type information.

    Key characteristics about the equipment.
    """
    isBeagleActiveProbe: bool = Field(description="is function as a Beagle Active Probe", default=False, examples=[True, False])
    isInfantryEncumbered: bool = Field(description="Does this encumber infantry", default=False, examples=[True, False])
    isECM: bool = Field(description="Does this function as an ECM device", default=False, examples=[True, False])
    isAngelECM: bool = Field(description="Does this function as an Angel ECM", default=False, examples=[True, False])
    isWatchdog: bool = Field(description="Does this function as a Watch dog device", default=False, examples=[True, False])
    isNOVA: bool = Field(description="does this function as a NOVA device", default=False, examples=[True, False])
    isBloodhound: bool = Field(description="does this function as a Bloodhound device", default=False, examples=[True, False])
    isEWEquipment: bool = Field(description="does this function as a Electronic Warfare equipment, not a full ECM suite", default=False, examples=[True, False])
    isMiscType: bool = Field(description="is this a Miscellaneous device", default=False, examples=[True, False])
    isBAManipulator: bool = Field(description="is this a Battle Armor Manipulator", default=False, examples=[True, False])
    isTAG: bool = Field(description="does this item provide TAG functionality", default=False, examples=[True, False])
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
    """
    A collection of boolean flags categorizing weapons by their type (Ballistic, Energy, Missile),
    technology base (Pulse, Ultra, Streak), and special rules (Indirect, Rapid Fire).

    Attributes:
    """
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

class BaseEquipmentItem(NullGBaseModel):
    """
    Base class for all specific equipment item data, containing shared physical
    and economic attributes like mass, cost, and Battle Value.
    """
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
    """
    Represents a weapon system, including its damage profile, heat generation,
    range brackets, and classification rules.

    Attributes:
        canSplit: Can this weapon be split into multiple locations
        clusterSize: The number of units that can be split into multiple locations
        bayType: The type of bay (Infantry, Battle Armor).
        crew: Number of crew to operate the weapon
    """
    canSplit: Optional[bool] = Field(description="", default=None)
    clusterSize: Optional[int] = Field(description="", default=None)
    bayType: Optional[str] = Field(description="", default=None)
    crew: Optional[int] = Field(description="", default=None)
    damage: Optional[EquipmentWeaponDamage] = Field(description="", default=None)
    ranges: Optional[EquipmentWeaponRanges] = Field(description="", default=None)
    extAV: Optional[float] = Field(description="", default=None)
    heat: Optional[int] = Field(description="", default=None)
    longAV: Optional[float] = Field(description="", default=None)
    medAV: Optional[float] = Field(description="", default=None)
    shortAV: Optional[float] = Field(description="", default=None)
    massDivisor: Optional[float] = Field(description="", default=None)
    bviModifier: Optional[float] = Field(description="", default=None)
    additionalDamage: Optional[int] = Field(description="", default=None)
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
    """
    Represents miscellaneous equipment that does not fit into standard categories
    like weapons, ammo, or engines.

    Attributes:
        bayType: The type of bay.
    """
    bayType: Optional[str] = Field(description="", default=None)


class CockpitItem(BaseEquipmentItem):
    """
    Represents cockpit systems and command consoles, including their specific
    modifiers and types.

    Attributes:
        bv
        cockpitType: The type of cockpit (Standard, Advanced, Expert).
    """
    bvModifier: Optional[float] = Field(description="", default=None)
    cockpitType: Optional[str] = Field(description="", default=None)


class EnhancementItem(BaseEquipmentItem):
    """
    Represents equipment that enhances unit performance or existing systems.
    """
    pass


class WeaponBayItem(BaseEquipmentItem):
    """
    Represents mounting bays for weapons, typically used on infantry or battle armor
    to carry support weaponry.

    Attributes:
        bayType: The type of bay (Infantry, Battle Armor).
        damage: The damage distribution rules for the bay.
        heat: The maximum heat generation for the bay.
        longRange: The maximum range for the bay.
        mediumRange: The maximum medium range for the bay.
        shortRange: The maximum short range for the bay.
    """
    bayType: Optional[str] = Field(description="", default=None)
    damage: Optional[dict] = Field(description="", default=None)
    heat: Optional[int] = Field(description="", default=None)
    longRange: Optional[int] = Field(description="", default=None)
    mediumRange: Optional[int] = Field(description="", default=None)
    shortRange: Optional[int] = Field(description="", default=None)


class ArmorItem(BaseEquipmentItem):
    """
    Represents armor plating, defining protection per ton, type (Standard, Ferro-Fibrous),
    and damage distribution rules.

    Atributes:
        bvModifier: The modifier to apply to the BV cost of the armor.
        armorPointsModifier: The modifier to apply to the armor points of the armor.
        armorType: The type of armor (Standard, Ferro-Fibrous).
        displayOrder: The display order of the armor.
        spreadable: Whether the armor can be spread across multiple locations.
        damageDivisor: The modifier to apply to the damage of the armor.
    """
    bvModifier: Optional[float] = Field(description="", default=1.0, examples=[1.0, 1.5, 2.0])
    armorPointsModifier: Optional[float] = Field(description="", default=1.0, examples=[1.0, 1.5, 2.0])
    armorType: Optional[str] = Field(description="", default="standard", examples=["standard", "special"])
    displayOrder: Optional[int] = Field(description="", default=0, examples=[1, 2, 4])
    spreadable: Optional[bool] = Field(description="", default=False, examples=[True, False])
    damageDivisor: Optional[float] = Field(description="", default=1.0, examples=[1.0, 1.5, 2.0])


class MyomerItem(BaseEquipmentItem):
    """
    Represents musculature enhancements like MASC or Triple Strength Myomer (TSM).

    Attributes:
        massDivisor: The modifier to apply to the mass of the myomer.
        myomerType: The type of myomer (MASC, TSM).
    """
    massDivisor: Optional[int] = Field(description="", default=None)
    myomerType: Optional[str] = Field(description="", default=None)


class ManipulatorItem(BaseEquipmentItem):
    """
    Represents physical manipulators such as hands, claws, or mining drills.

    Attributes:
        shortName: The short name of the manipulator.
    """
    shortName: Optional[str] = Field(description="", default=None)


class ConversionItem(BaseEquipmentItem):
    """
    Represents equipment used for converting or adapting other systems.
    """
    pass


class StructureItem(BaseEquipmentItem):
    """
    Represents internal structure components (e.g., Endo-Steel, Composite), including
    mass saving modifiers.

    Attributes:
        bvModifier: The modifier to apply to the BV cost of the structure.
        massModifier: The modifier to apply to the mass of the structure.
        structureType: The type of structure (e.g., Endo-Steel, Composite).

    """
    bvModifier: Optional[float] = Field(description="", default=None)
    massModifier: Optional[float] = Field(description="", default=None)
    structureType: Optional[str] = Field(description="", default=None)


class EngineItem(BaseEquipmentItem):
    """
    Represents power plant systems (Fusion, ICE, Fuel Cell), detailing rating modifiers,
    weight classes, and integral heat sinks.

    Attributes:
        assignedSlots: The number of slots assigned to the engine.
        bvModifier: The modifier to apply to the BV cost of the engine.
        displayName: The display name of the engine.
        engineClass: The class of engine (Fusion, ICE, Fuel Cell).
        engineRatingMod: The modifier to apply to the engine rating.
        includedHeatSinks: The number of heat sinks included in the engine.
        powerAmplifierNeeded: Whether a power amplifier is needed for the engine.
    """
    assignedSlots: Optional[Dict[str, int]] = Field(description="", default=None)
    bvModifier: Optional[float] = Field(description="", default=None)
    displayName: Optional[str] = Field(description="", default=None)
    engineClass: Optional[int] = Field(description="", default=None)
    engineRatingMod: Optional[float] = Field(description="", default=None)
    includedHeatSinks: Optional[int] = Field(description="", default=None)
    powerAmplifierNeeded: Optional[bool] = Field(description="", default=None)


class GyroItem(BaseEquipmentItem):
    """
    Represents gyroscope systems, including standard, extra-light, and heavy-duty variants.

    Attributes:
        bvModifier: The modifier to apply to the BV cost of the gyro.
        displayName: The display name of the gyro.
        gyroType: The type of gyro (standard, extra-light, heavy-duty).
        massModifier: The modifier to apply to the mass of the gyro.
    """
    bvModifier: Optional[float] = Field(description="", default=None)
    displayName: Optional[str] = Field(description="", default=None)
    gyroType: Optional[str] = Field(description="", default=None)
    massModifier: Optional[float] = Field(description="", default=None)


class BayItem(BaseEquipmentItem):
    """
    Represents transport and cargo bays, detailing capacity for personnel or goods.

    Attributes:
        crew: The number of crew members that can be mounted on the bay.
    """
    crew: Optional[int] = Field(description="", default=None)


class HeatSinkItem(BaseEquipmentItem):
    """
    Represents heat dissipation systems, distinguishing between Single and Double heat sinks.
    """
    pass


class AmmoItem(BaseEquipmentItem):
    """
    Represents ammunition bins, detailing shots per ton, projectile weight, and
    associated weapon compatibility.
    """
    ammoRatio: Optional[float] = Field(description="", default=None)
    defensive: Optional[bool] = Field(description="", default=None)
    equipName: Optional[str] = Field(description="", default=None)
    kgPerShot: Optional[float] = Field(description="", default=None)
    rackSize: Optional[int] = Field(description="", default=None)
    rulesRefs: Optional[str] = Field(description="", default=None)
    short: Optional[int] = Field(description="", default=None)
    shots: Optional[float] = Field(description="", default=None)


class EquipmentItem(NullGBaseModel):
    """
    The primary container for an equipment entry, aggregating metadata, classification flags,
    applicability rules, and the specific item data model.
    """
    id: Optional[str] = Field(description="", default=None)
    equipmentType: Optional[EquipmentType] = Field(description="", default=None)
    name: Optional[str] = Field(description="", default=None)
    techRating: Optional[str] = Field(description="", default=None)
    techbase: Optional[TechbaseType] = Field(description="", default=None)
    type: Optional[EquipmentTypeData] = Field(description="", default=None)
    unitSubtypes: Optional[List[UnitSubtype]] = Field(
        description="A list of unit subtypes this item is for",
        default_factory=list,
        examples=[0,5]
    )
    version: Optional[float] = Field(
        description="Version of this items data",
        default=0.01,
        examples=[1.0, 1.45, 2.0]
    )
    metadata: Optional[dict] = Field(description="", default=None)
    rulesLevel: Optional[int] = Field(description="", default=None)
    item: Optional[Union[WeaponItem, OtherItem, CockpitItem, AmmoItem, HeatSinkItem, BayItem, GyroItem, EngineItem,
    StructureItem, ConversionItem, ArmorItem, ManipulatorItem, MyomerItem, WeaponBayItem,
    EnhancementItem]] = Field(description="", default=None)

    @field_validator('item', mode='before')
    @classmethod
    def validate_item_type(cls, v: Dict, info: ValidationInfo):
        if v is not None and isinstance(v, dict):
            if FIELD_EQUIPMENT_TYPE in info.data and isinstance(info.data[FIELD_EQUIPMENT_TYPE], int):
                try:
                    thisEquipmentType = EquipmentType(info.data[FIELD_EQUIPMENT_TYPE])
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
