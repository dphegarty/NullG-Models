"""Data models for Total Warfare classic Battletech game system.

This module defines Pydantic models for the Total Warfare (also known as
Classic Battletech) tactical tabletop wargame. Total Warfare is the full,
detailed ruleset with turn-by-turn combat resolution, hit locations,
critical hits, and heat management.

These models represent complete construction data for units including:
- Equipment lists and locations
- Armor distribution and internal structure
- Critical slot allocations
- Engine, gyro, cockpit, and other systems
- Movement capabilities and heat management

Total Warfare uses hexagonal maps and detailed record sheets for
unit management during gameplay.

For more information on Total Warfare rules, see:
https://bg.battletech.com/books/total-warfare/
"""

from typing import Optional, List, Dict, Literal, Union
from pydantic import Field

from NullgModels.EquipmentModels import EquipmentItem
from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import TurretType, JumpJetType, TotalWarEquipmentItemType, MotionType, WeightClassType, \
    RoleType


class TotalWarBasicComponent(NullGBaseModel):
    """Basic component representation for Total Warfare units.

    Attributes:
        name: Name of the Components, e.g., Standard, Stealth,.
        id: Unique identifier for the item.
        techbase: Technology base for the item.
        equipmentTypeId: Equipment type Id

    Examples:
        >>> TotalWarBasicComponent(
        ...     name="Standard",
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     equipmentTypeId=0
        ... )

    """
    name: Optional[str] = Field(
        description="Name of the item.",
        default=None,
        examples=["Standard", "Stealth"]
    )
    id: Optional[str] = Field(
        description="Unique identifier for the item.",
        default=None,
        examples=["", ""]
    )
    techbase: Optional[str] = Field(
        description="Technology base for the item.",
        default=None,
        examples=["Inner Sphere", "Clan", "Mixed"]
    )
    equipmentTypeId: Optional[Literal[0, 3, 5, 6, 8, 4]] = Field(
        description="Equipment type Id",
        default=None,
        examples=[0, 3, 5, 6, 8, 4]
    )

class TotalWarArmorComponent(TotalWarBasicComponent):
    """Armor item representation for Total Warfare units.

        Represents an armor component of a unit in Total Warfare.

    Examples:
        >>> TotalWarArmorComponent(
        ...     name="Stealth",
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     barRating=10,
        ...     equipmentTypeId=0
        ... )
    """
    barRating: Optional[int] = Field(
        description="Barrier Armor Rating, military grade armor has a BAR of 10, "
                    "commercial and industrial armor has a BAR between 0 and 9",
        default=10,
        ge=0,
        le=10,
        examples=[10, 5]
    )
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=0
    )

class TotalWarEngineComponent(TotalWarBasicComponent):
    """Engine item representation for Total Warfare units.

    Represents an engine component of a unit in Total Warfare. Engine
    items have specific properties like type and rating.

    Examples:
        >>> TotalWarEngineComponent(
        ...     name="Fusion",
        ...     rating=310,
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     equipmentTypeId=3
        ... )
    """
    rating: Optional[int] = Field(
        description="Engine rating, this is generally based on desired movement X unit mass",
        default=None,
        examples=[275, 310]
    )
    type: Optional[str] = Field(
        description="Engine type",
        default=None,
        examples=["Standard", "XL", "Compact"]
    )
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=3
    )

class TotalWarStructureComponent(TotalWarBasicComponent):
    """Structure item representation for Total Warfare units.

    Represents a structural component of a unit in Total Warfare. Structure
    items have specific properties like type, techbase

    Examples:
        >>> TotalWarStructureComponent(
        ...     name="Endo Steel",
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     equipmentTypeId=5
        ... )

    """
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=5
    )

class TotalWarMyomerComponent(TotalWarBasicComponent):
    """Myomer item representation for Total Warfare units.

    Represents a myomer component of a unit in Total Warfare.

    Examples:
        >>> TotalWarMyomerComponent(
        ...     name="Triple Strength",
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     equipmentTypeId=8
        ... )

    """
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=8
    )

class TotalWarGyroComponent(TotalWarBasicComponent):
    """Gyro item representation for Total Warfare units.

    Represents a gyro component of a unit in Total Warfare.

    Examples:
        >>> TotalWarGyroComponent(
        ...     name="Heavy Duty",
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     equipmentTypeId=4
        ... )

    """
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=4
    )

class TotalWarCockpitComponent(TotalWarBasicComponent):
    """Cockpit item representation for Total Warfare units.

    Represents a Cockpit component of a unit in Total Warfare.

    Examples:
        >>> TotalWarCockpitComponent(
        ...     name="Small",
        ...     id="abc123...",
        ...     techbase="Inner Sphere",
        ...     equipmentTypeId=6
        ... )

    """
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=6
    )

class TotalWarHeatSinkComponent(TotalWarBasicComponent):
    """Gyro item representation for Total Warfare units.

    Represents a gyro component of a unit in Total Warfare. Gyro
    items have specific properties like type, material, and durability."""
    equipmentTypeId: Optional[int] = Field(
        description="Equipment type Id",
        default=10
    )
    type: Optional[int] = Field(
        description="Heat Sink type Id",
        default=1,
        examples=[1, 2, 3]
    )
    count: Optional[int] = Field(
        description="Number of heat sinks",
        default=0,
        examples=[1, 24, 13]
    )
    criticalFree: Optional[int] = Field(
        description="Critical Free Heat Sinks",
        default=0,
        examples=[5, 10]
    )
    engineBase: Optional[int] = Field(
        description="Included in the Engin, this is based on the engine and unit weight",
        default=0,
        examples=[1, 2, 3]
    )
    omniBase: Optional[int] = Field(
        description="Included in Omni Pods, this is used in OmniMech only",
        default=0,
        examples=[5, 8]
    )


class TotalWarBayBaseItem(NullGBaseModel):
    """Basic cargo bay or unit bay information.

    Represents a bay on a DropShip or transport unit that can carry
    cargo, units, or other equipment. Bays have specific capacities
    and configurations.

    Attributes:
        name: Name/type of the bay (e.g., "Mech Bay", "Vehicle Bay", "Infantry Bay").
        value: Capacity or size value for the bay.

    Examples:
        >>> first_class = TotalWarBayBaseItem(name="1stClass", value=10.0)
        >>> second_class = TotalWarBayBaseItem(name="2ndClass", value=5.0)
    """
    name: Optional[str] = Field(
        description="Name or type of the bay. Common types: 1st Class, 2nd Class, "
                    "Crew, Steerage",
        default=None,
        examples=["2ndClass", "1stClass", "Crew", "Steerage"]
    )
    value: Optional[float] = Field(
        description="Capacity or configuration value for this bay. "
                    "May be unit count, tonnage, or other capacity measure.",
        default=None,
        examples=[1, 5, 50]
    )

class TotalWarBayExtendedItem(TotalWarBayBaseItem):
    """Extended bay information with door configuration.

    Enhanced bay information including the number of bay doors,
    which affects loading/unloading speed and tactical deployment.
    This is used for Cargo, Mech and Infantry bays.

    Attributes:
        id: Unique identifier for this bay.
        doors: Number of doors for this bay (affects deployment speed).

    Examples:
        >>> extended_bay = TotalWarBayExtendedItem(
        ...     name="Mech Bay",
        ...     value=4.0,
        ...     doors=2
        ... )
    """
    id: Optional[str] = Field(
        description="Unique identifier (UUID) for this bay.",
        default=None,
        examples=["6b6369f2-bcee-4a08-bd11-171d90cab87c"]
    )
    doors: Optional[int] = Field(
        description="Number of bay doors. More doors allow faster deployment. "
                    "Each door can deploy one unit per turn.",
        default=None,
        examples=[1, 2, 3, 4]
    )


class TotalWarArmorLocation(NullGBaseModel):
    """Armor points for a specific location on a unit.

    Armor is distributed across different hit locations on a unit
    (head, torso, arms, legs for mechs; front, sides, rear for vehicles).
    Each location has a specific armor value that absorbs damage.

    Attributes:
        armor: Armor points for this location (damage absorption).
        location: The body location (e.g., "head", "center_torso", "front").
        value: Alternative/additional armor value (legacy field).

    Examples:
        >>> head_armor = TotalWarArmorLocation(
        ...     location="head",
        ...     armor="",
        ...     value=9
        ... )
        >>> front_armor = TotalWarArmorLocation(
        ...     location="front",
        ...     armor="",
        ...     value=31
        ... )
    """
    armor: Optional[str] = Field(
        description="Armor points for this location. Absorbs damage before "
                    "internal structure is damaged. 0 means no armor.",
        default=None,
        examples=[9, 32, 45, 64, 80]
    )
    location: Optional[str] = Field(
        description="Body location name. BattleMechs: head, center_torso, "
                    "left_torso, right_torso, left_arm, right_arm, left_leg, right_leg. "
                    "Vehicles: front, left_side, right_side, rear, turret. "
                    "Aerospace: nose, left_wing, right_wing, aft.",
        default=None,
        examples=["head", "center_torso", "front", "turret", "nose"]
    )
    value: Optional[int] = Field(
        description="Alternative armor value field (legacy compatibility). "
                    "Typically same as 'armor' field.",
        default=None,
        examples=[9, 32, 45]
    )


class TotalWarEquipmentItem(NullGBaseModel):
    """Equipment item mounted on a unit.

    Represents a single piece of equipment (weapon, ammunition, heat sink,
    etc.) installed on a unit. Includes the equipment's identity, location,
    type, and any configuration options.

    Equipment must be placed in valid locations and may occupy critical
    slots. Some equipment has special mounting requirements or restrictions.

    Attributes:
        id: Unique identifier for this equipment type.
        name: Display name of the equipment.
        location: Where on the unit this equipment is mounted.
        options: Special options or modifiers for this equipment.
        type: Category of equipment (weapon, ammo, equipment, etc.).

    Examples:
        >>> ppc = TotalWarEquipmentItem(
        ...     id="6b6369f2-bcee-4a08-bd11-171d90cab87c",
        ...     name="PPC",
        ...     location="right_arm",
        ...     options="",
        ...     type="weapon"
        ... )
        >>> ammo = TotalWarEquipmentItem(
        ...     id="abc123...",
        ...     name="SRM 6 Ammo",
        ...     location="center_torso",
        ...     options="(CASE)",
        ...     type="ammo"
        ... )
    """
    id: str = Field(
        description="UUID of the equipment type in the equipment database. "
                    "Used to look up full equipment statistics and rules.",
        default=None,
        examples=["6b6369f2-bcee-4a08-bd11-171d90cab87c"]
    )
    name: str = Field(
        description="Display name of the equipment. May include modifiers or size. "
                    "Examples: 'PPC', 'Medium Laser', 'LRM 20', 'XL Engine', 'Double Heat Sink'.",
        default=None,
        examples=["PPC", "Medium Laser", "XL Engine", "SRM 6 Ammo", "CASE"]
    )
    location: str = Field(
        description="Body location where this equipment is mounted. "
                    "Must be a valid location for the unit type. "
                    "BattleMechs: head, center_torso, left_torso, right_torso, left_arm, "
                    "right_arm, left_leg, right_leg. "
                    "Vehicles: front, left_side, right_side, rear, turret, body. "
                    "Special locations: None (engine-integrated), Body (internal systems).",
        default=None,
        examples=["center_torso", "right_arm", "turret", "front", "body"]
    )
    options: str = Field(
        description="Special options, modifiers, or configuration for this equipment. "
                    "Common options: (TC)=Targeting Computer, (CL)=Clan, (OS)=One-Shot, "
                    "(R)=Rear-Facing, (CASE)=Protected by CASE, (Artemis IV), (Apollo).",
        default=None,
        examples=["(TC)", "(CL)", "(OS)", "(R)", "(CASE)", "(Artemis IV)", ""]
    )
    type: TotalWarEquipmentItemType = Field(
        description="Equipment category type. "
                    "Common types: weaponbay, equipment, ammo."
                    "This can be used to determine the type of equipment and how it interacts with the mech or vehicle.",
        default=None,
        examples=["weaponbay", "equipment", "ammo"]
    )


class TotalWarCriticalLocationItem(NullGBaseModel):
    """Critical slot allocation for a body location.

    Each body location on a BattleMech or vehicle has a limited number
    of critical slots. Equipment is allocated to these slots. This model
    tracks which slots are occupied and by what equipment.

    Attributes:
        location: The body location these critical slots belong to.
        slots: List of slot allocations (equipment names or empty markers).

    Examples:
        >>> arm_crits = TotalWarCriticalLocationItem(
        ...     location="right_arm",
        ...     slots=[
        ...         "Shoulder",
        ...         "Upper Arm Actuator",
        ...         "Lower Arm Actuator", 
        ...         "PPC",
        ...         "PPC",
        ...         "PPC",
        ...         "-Empty-",
        ...         "-Empty-",
        ...         "-Empty-",
        ...         "-Empty-",
        ...         "-Empty-",
        ...         "Hand Actuator"
        ...     ]
        ... )
    """
    location: Optional[str] = Field(
        description="Body location name for these critical slots. "
                    "Standard BattleMech has 12 locations with varying slot counts. "
                    "Center Torso: 12 slots, Side Torsos: 12 slots, Head: 6 slots, "
                    "Arms: 12 slots, Legs: 6 slots.",
        default=None,
        examples=["head", "center_torso", "right_arm", "left_leg"]
    )
    slots: Optional[List[Union[str, None]]] = Field(
        description="Ordered list of critical slot contents. "
                    "Each entry is equipment name occupying that slot, or '-Empty-' for unused slots. "
                    "Some equipment takes multiple slots (e.g., PPC = 3 slots). "
                    "Fixed equipment: Shoulder, Upper Arm Actuator, Lower Arm Actuator, "
                    "Hip, Upper Leg Actuator, Lower Leg Actuator, Foot Actuator.",
        default=None,
        examples=[
            ["Engine", "Engine", "Gyro"],
            ["PPC", "PPC", "PPC", "-Empty-"],
            ["Shoulder", "Upper Arm Actuator", "Lower Arm Actuator", "Hand Actuator"]
        ]
    )


class TotalWarUnitDataBase(NullGBaseModel):
    """Base class for all Total Warfare unit data.

    Contains common fields shared across all unit types (BattleMechs,
    Vehicles, Aerospace, Infantry, DropShips). Specific unit types
    extend this base with their unique attributes.

    This is an abstract base class - use the specific unit type classes
    for actual units.

    Attributes:
        armor: Total armor points across all locations.
        bv: Battle Value (game balance/cost metric).
        config: Configuration type (Standard, Omni, etc.).
        mass: Unit mass/tonnage.
        pv: Point Value (Alpha Strike compatibility).
        source: Source book or publication reference.
        techbase: Technology base (Inner Sphere, Clan, Mixed).
        version: Data version number.
        unitDataSourceUri: URI to original source file.
        equipmentList: List of all equipment on the unit.
        armorLocations: Armor distribution by location.
        copyrightTrademark: Copyright and trademark information.
        runMp: Running movement points.
        motionType: Type of movement (Biped, Quad, Wheeled, etc.).
        productionYear: In-universe year of first production.
        rulesLevel: Rules complexity level.
        walkMp: Walking movement points.
        trooperCount: Number of troopers (infantry/BA only).
        jumpMp: Jump movement points.
        armorFactor: Actual armor tonnage.
        armorFactorMax: Maximum possible armor.
        fireControl: Fire control system rating.
    """
    armor: Optional[TotalWarArmorComponent] = Field(
        description="An object that decodes the armor component of the unit.",
        default=None,
        examples=[""]
    )
    bv: Optional[float] = Field(
        description="Battle Value. Unit's game balance value for scenario design. "
                    "Used to create balanced forces. Accounts for weapons, armor, speed, etc.",
        default=None,
        examples=[1234, 1568, 2145, 3012]
    )
    config: Optional[str] = Field(
        description="Configuration type. Standard=fixed equipment, Omni=modular pods. "
                    "OmniMechs can swap weapons between battles.",
        default=None,
        examples=["Standard", "Omni", "ProtoMech"]
    )
    mass: Optional[float] = Field(
        description="Unit mass in tons. Affects movement, armor capacity, and weapon load. "
                    "BattleMechs: 20-100 tons. Vehicles: 5-100+ tons. Infantry: per trooper.",
        default=None,
        examples=[25, 50, 75, 100]
    )
    pv: Optional[int] = Field(
        description="Point Value for Alpha Strike game system. "
                    "Alternative to Battle Value for fast-play rules.",
        default=None,
        examples=[25, 35, 42, 58]
    )
    source: Optional[str] = Field(
        description="Source book or publication where this unit appears. "
                    "Format: 'Book Name, page XX' or 'Book Abbreviation'.",
        default=None,
        examples=["TechManual", "TRO:3025", "TRO:3050U, p.123", "Rec Guide:12"]
    )
    techbase: Optional[str] = Field(
        description="Technology base: 'Inner Sphere', 'Clan', or 'Mixed'. "
                    "Determines construction rules and equipment availability.",
        default=None,
        examples=["Inner Sphere", "Clan", "Mixed"]
    )
    version: Optional[float] = Field(
        description="Data schema version number. Tracks format changes over time.",
        default=None,
        examples=[1.0, 2.0, 2.5]
    )
    unitDataSourceUri: Optional[str] = Field(
        description="URI or path to original source data file (MTF, BLK, etc.). "
                    "Used for data provenance and validation.",
        default=None,
        examples=["units/mechs/atlas_as7-d.mtf", "http://example.com/unit.blk"]
    )
    equipmentList: Optional[List[TotalWarEquipmentItem]] = Field(
        description="Complete list of equipment installed on this unit. "
                    "Includes weapons, ammunition, heat sinks, and all other components.",
        default=None
    )
    armorLocations: Optional[List[TotalWarArmorLocation]] = Field(
        description="Armor distribution across all body locations. "
                    "Each location has specific armor value and facing.",
        default=None
    )
    copyrightTrademark: Optional[str] = Field(
        description="Copyright and trademark information for this unit design. "
                    "Legal attribution for intellectual property.",
        default=None,
        examples=["©2024 The Topps Company, Inc. All Rights Reserved."]
    )
    runMp: Optional[int] = Field(
        description="Running movement points. Distance unit can run in hexes per turn. "
                    "Typically 1.5x walking speed (rounded up). Running generates heat.",
        default=None,
        examples=[4, 6, 9, 12]
    )
    motionType: Optional[MotionType] = Field(
        description="Movement type/locomotion method. "
                    "BattleMechs: Biped, Quad. Vehicles: Wheeled, Tracked, Hover, VTOL, "
                    "Naval (Displacement), Naval (Hydrofoil), WiGE. Aerospace: Aerodyne, Spheroid.",
        default=None,
        examples=["Biped", "Quad", "Wheeled", "Tracked", "Hover", "VTOL", "Aerodyne"]
    )
    productionYear: Optional[int] = Field(
        description="In-universe year when this unit variant first entered production. "
                    "Used for era-appropriate gameplay and campaigns.",
        default=None,
        examples=[2750, 3025, 3050, 3067, 3145]
    )
    rulesLevel: Optional[int] = Field(
        description="Rules complexity level. 0=Intro, 1=Standard, 2=Advanced, 3=Experimental. "
                    "Higher levels add complexity and unusual equipment.",
        default=None,
        examples=[0, 1, 2, 3]
    )
    walkMp: Optional[int] = Field(
        description="Walking movement points. Base movement speed in hexes per turn. "
                    "Fundamental mobility stat affecting tactical options.",
        default=None,
        examples=[3, 4, 5, 6, 8]
    )
    trooperCount: Optional[int] = Field(
        description="Number of individual troopers in unit. "
                    "Infantry: 21-28 soldiers. Battle Armor: 4-6 suits. "
                    "1 for single-pilot units (mechs, vehicles).",
        default=None,
        examples=[1, 4, 5, 21, 28]
    )
    jumpMp: Optional[int] = Field(
        description="Jump movement points. Distance unit can jump in hexes. "
                    "Jump ignores terrain but may generate heat. 0=no jump capability.",
        default=None,
        examples=[0, 3, 5, 6, 8]
    )
    armorFactor: Optional[int] = Field(
        description="Actual armor tonnage on the unit. Armor weight in tons or points. "
                    "Must not exceed armorFactorMax.",
        default=None,
        examples=[5.0, 10.5, 15.0, 19.0]
    )
    armorFactorMax: Optional[int] = Field(
        description="Maximum possible armor for this unit's chassis and mass. "
                    "Defined by construction rules and unit type.",
        default=None,
        examples=[120, 168, 256, 384]
    )
    extraOptions: Optional[Dict[str, bool]] = Field(
        description="Additional construction options as flag dictionary. "
                    "Keys are option names, values are True if present. "
                    "Examples: MASC, TSM, Partial Wing, etc.",
        default=None,
        examples=[
            {"MASC": True, "TSM": True},
            {"Partial Wing": True},
            {}
        ]
    )
    fireControl: Optional[str] = Field(
        description="Fire control system. "
                    "Affects weapon accuracy and targeting.",
        default=None,
        examples=["Basic", "Advanced"]
    )


class TotalWarBattleMechData(TotalWarUnitDataBase):
    """Complete construction data for a BattleMech.

    BattleMechs are the iconic combat units of Battletech - bipedal or
    quadrupedal armored fighting vehicles with fusion engines, weapons,
    and sophisticated systems. This model includes all data needed for
    mech construction, validation, and gameplay.

    Extends TotalWarUnitDataBase with mech-specific systems like
    engine rating, heat sinks, gyro, cockpit, myomer, and critical slots.

    Attributes:
        cockpit: Cockpit type (Standard, Small, Command, etc.).
        constructionInvalid: List of construction rule violations.
        constructionValidated: Whether construction has been validated.
        engine: Full engine description string.
        extraOptions: Additional construction options flags.
        gyro: Gyroscope type (Standard, XL, Compact, Heavy-Duty).
        heatSinks: Total number of heat sinks.
        myomer: Myomer/muscle type (Standard, TSM, MASC, etc.).
        structure: Internal structure type.
        weapons: Total count of weapons..
        criticalLocations: Critical slot allocation data.
        productionEra: Era when variant was introduced.
        jumpjetType: Type of jump jets (Standard, Improved, etc.).

    Examples:
        >>> atlas = TotalWarBattleMechData(
        ...     mass=100,
        ...     walkMp=3,
        ...     runMp=5,
        ...     jumpMp=0,
        ...     armor=307,
        ...     structure="standard",
        ...     engineRating=300,
        ...     engineType="Fusion",
        ...     heatSinks=20,
        ...     heatSinksType=1,  # Double
        ...     weapons=8,
        ...     techbase="Inner Sphere",
        ...     config="Standard"
        ... )
    """
    cockpit: Optional[TotalWarCockpitComponent] = Field(
        description="Cockpit type. Affects head slot usage and pilot protection. "
                    "Standard (1 slot), Small (1 slot), Command Console (2 slots), "
                    "Torso-Mounted, Interface, etc.",
        default=None,
        examples=["Standard", "Small", "Command Console", "Torso-Mounted"]
    )
    constructionInvalid: Optional[List[str]] = Field(
        description="List of construction rule violations if unit is invalid. "
                    "Empty list or None means unit is valid. "
                    "Common issues: overweight, insufficient heat sinks, invalid equipment.",
        default=None,
        examples=[
            ["Unit exceeds maximum tonnage"],
            ["Insufficient heat dissipation", "Armor exceeds maximum"],
            []
        ]
    )
    constructionValidated: Optional[bool] = Field(
        description="Whether the unit has undergone construction validation. "
                    "True=validated (may still be invalid), False/None=not validated.",
        default=None
    )
    engine: Optional[TotalWarEngineComponent] = Field(
        description="Full engine description string combining rating and type. "
                    "Format: '[Rating] [Type] Engine' (e.g., '300 XL Engine').",
        default_factory=TotalWarEngineComponent,
        examples=["300 Fusion Engine", "375 XL Engine", "400 Light Engine"]
    )
    gyro: Optional[TotalWarGyroComponent] = Field(
        description="Gyroscope type. Affects critical slots and weight. "
                    "Standard (4 slots, 3-4 tons), XL (6 slots, 2 tons), "
                    "Compact (2 slots, 6 tons), Heavy-Duty (4 slots, 6 tons).",
        default=None,
        examples=[""]
    )
    heatSinks: Optional[TotalWarHeatSinkComponent] = Field(
        description="Total number of heat sinks on the unit. "
                    "Includes engine-integrated and additional heat sinks. "
                    "Each single heat sink dissipates 1 heat, double sinks = 2.",
        default=None,
        examples=[TotalWarHeatSinkComponent()]
    )
    myomer: Optional[TotalWarMyomerComponent] = Field(
        description="Myomer (artificial muscle) type. Affects performance. "
                    "Standard (normal), TSM (Triple-Strength, +2 damage in melee), "
                    "MASC (speed boost), Industrial (cheaper but weaker).",
        default=None,
        examples=["Standard", "TSM", "MASC", "Industrial"]
    )
    structure: Optional[TotalWarStructureComponent] = Field(
        description="Internal structure type. Affects weight and durability. "
                    "Standard (1 point per ton), Endo Steel (lighter), "
                    "Composite (lighter but more slots), Reinforced (heavier but tougher).",
        default=None,
        examples=["Standard", "Endo Steel", "Composite", "Reinforced"]
    )
    weapons: Optional[int] = Field(
        description="Total count of weapon systems mounted on the mech. "
                    "Includes all direct-fire and missile weapons.",
        default=None,
        examples=[4, 6, 8, 12]
    )
    criticalLocations: Optional[List[TotalWarCriticalLocationItem]] = Field(
        description="Complete critical slot allocation for all body locations. "
                    "Shows what equipment is in each slot of each location.",
        default=None
    )
    productionEra: Optional[int] = Field(
        description="Era ID when this variant entered production (see era list).",
        default=None,
        examples=[1, 5, 9, 10, 13]
    )
    jumpjetType: Optional[JumpJetType] = Field(
        description="Jump jet type code. "
                    "0=Standard, 1=Improved (more MP), 2=Prototype, etc.",
        default=None,
        examples=[0, 1, 2]
    )


class TotalWarAerospaceData(TotalWarUnitDataBase):
    """Complete construction data for Aerospace Fighters.

    Aerospace fighters are spacecraft designed for space and atmospheric
    combat. They use different movement and combat rules than ground units.

    Attributes:
        cockpit: Cockpit type for aerospace.
        constructionInvalid: Construction validation errors.
        constructionValidated: Validation status.
        extraOptions: Additional options dictionary.
        fuel: Fuel capacity in points.
        transportSpace: Cargo/transport capacity.
        heatSinks: Total heat sinks.
        structure: Structure type.
        safeThrust: Safe thrust rating (movement).
        weapons: Weapon count.
        productionEra: Production era ID.
    """
    cockpit: Optional[TotalWarCockpitComponent] = Field(
        description="Cockpit type for aerospace fighters.",
        default=None,
        examples=[""]
    )
    constructionInvalid: Optional[List[str]] = Field(
        description="List of construction rule violations.",
        default=None
    )
    constructionValidated: Optional[bool] = Field(
        description="Whether construction has been validated.",
        default=None
    )
    engine: Optional[TotalWarEngineComponent] = Field(
        description="Engine description string. Format: '[Rating] [Type] Engine'.",
        default_factory=TotalWarEngineComponent,
        examples=[TotalWarEngineComponent()]
    )
    fuel: Optional[int] = Field(
        description="Fuel capacity in points. Each point allows strategic movement.",
        default=None,
        examples=[400, 800, 1600]
    )
    transportSpace: Optional[Dict] = Field(
        description="Cargo or transport capacity in tons.",
        default=None,
        examples=[]
    )
    heatSinks: Optional[TotalWarHeatSinkComponent] = Field(
        description="Total number of heat sinks.",
        default=None,
        examples=[TotalWarHeatSinkComponent()]
    )
    structure: Optional[TotalWarStructureComponent] = Field(
        description="Aerospace structure type.",
        default=None,
        examples=["Standard", "Endo Steel"]
    )
    safeThrust: Optional[int] = Field(
        description="Safe thrust rating. Base movement speed for aerospace units.",
        default=None,
        examples=[4, 6, 8, 10]
    )
    weapons: Optional[int] = Field(
        description="Total weapon count.",
        default=None,
        examples=[4, 6, 8]
    )
    productionEra: Optional[int] = Field(
        description="Production era ID.",
        default=None
    )


class TotalWarInfantryData(TotalWarUnitDataBase):
    """Complete construction data for Infantry units.

    Infantry includes conventional soldiers and battle armor (power-armored
    infantry). They use different rules than vehicle/mech units.

    Attributes:
        constructionInvalid: Construction validation errors.
        constructionValidated: Validation status.
        extraOptions: Additional options.
        structure: Structure type.
        trooperMass: Mass per individual trooper.
        productionEra: Production era ID.
        squads: Number of squads in the unit.
        squadSize: Troopers per squad.
        secondaryWeaponTroops: Troopers with secondary weapons.
        isExoskeleton: Whether this is exoskeleton infantry.
    """
    constructionInvalid: Optional[List[str]] = Field(
        description="List of construction rule violations.",
        default=None
    )
    constructionValidated: Optional[bool] = Field(
        description="Whether construction has been validated.",
        default=None
    )
    structure: Optional[TotalWarStructureComponent] = Field(
        description="Structure type (battle armor).",
        default=None,
        deprecated=True,
        exclude=True,
        examples=["Standard", "Endo Steel"]
    )
    trooperMass: Optional[float] = Field(
        description="Mass of each individual trooper in tons. "
                    "Battle armor typically 0.4-2.0 tons per suit.",
        default=None,
        examples=[0.08, 0.4, 1.0, 2.0]
    )
    productionEra: Optional[int] = Field(
        description="Production era ID.",
        default=None
    )
    squads: Optional[int] = Field(
        description="Number of squads in the platoon/company.",
        default=None,
        examples=[4, 5, 6]
    )
    squadSize: Optional[int] = Field(
        description="Number of troopers per squad.",
        default=None,
        examples=[4, 5, 6, 7]
    )
    secondaryWeaponTroops: Optional[int] = Field(
        description="Number of troopers equipped with secondary weapons.",
        default=None,
        examples=[0, 4, 8]
    )
    isExoskeleton: Optional[bool] = Field(
        description="Whether this is exoskeleton-equipped infantry (light power armor).",
        default=False
    )


class TotalWarVehicleData(TotalWarUnitDataBase):
    """Complete construction data for Combat Vehicles.

    Combat vehicles include tanks, hovercraft, VTOLs, naval vessels, and
    other ground/naval combat units.

    Attributes:
        constructionInvalid: Construction validation errors.
        constructionValidated: Validation status.
        extraOptions: Additional options.
        turretType: Turret configuration.
        transportSpace: Cargo capacity.
        structure: Structure type.
        productionEra: Production era ID.
        hasControlSystems: Whether vehicle has control systems.
        heatSinks: Heat sink count (if equipped).
        isTrailer: Whether this is a trailer unit.
        extraCombatSeats: Additional crew/passenger seats.
        jumpjetType: Jump jet type (for jump-capable vehicles).
    """
    constructionInvalid: Optional[List[str]] = Field(
        description="List of construction rule violations.",
        default=None
    )
    constructionValidated: Optional[bool] = Field(
        description="Whether construction has been validated.",
        default=None
    )
    engine: Optional[TotalWarEngineComponent] = Field(
        description="Engine type and rating.",
        default_factory=TotalWarEngineComponent,
        examples=["300 Fusion Engine", "375 XL Engine", "400 Light Engine"]
    )
    turretType: Optional[TurretType] = Field(
        description="Turret configuration (None, Single, Dual, Chin, Sponson).",
        default=None,
        examples=[0, 1, 2]
    )
    transportSpace: Optional[TotalWarBayBaseItem] = Field(
        description="Cargo or infantry transport capacity in tons.",
        default=None,
        examples=[0, 2.5, 5.0, 10.0]
    )
    structure: Optional[TotalWarStructureComponent] = Field(
        description="Vehicle structure type.",
        default=None,
        examples=["Standard", "Endo Steel"]
    )
    productionEra: Optional[int] = Field(
        description="Production era ID.",
        default=None
    )
    hasControlSystems: Optional[bool] = Field(
        description="Whether vehicle has advanced control systems.",
        default=None
    )
    heatSinks: Optional[TotalWarHeatSinkComponent] = Field(
        description="Heat sinks (for energy-weapon equipped vehicles).",
        default=None
    )
    isTrailer: Optional[bool] = Field(
        description="Whether this is a towed trailer unit.",
        default=None
    )
    extraCombatSeats: Optional[int] = Field(
        description="Additional crew or passenger combat seats.",
        default=None
    )
    jumpjetType: Optional[JumpJetType] = Field(
        description="Jump jet type (for jump-capable vehicles).",
        default=None
    )


class TotalWarDropshipData(TotalWarUnitDataBase):
    """Complete construction data for DropShips.

    DropShips are spacecraft that transport units and cargo between
    JumpShips and planetary surfaces.

    Attributes:
        bays: List of cargo/unit bays.
        quarters: Crew quarters information.
        crewValues: Crew requirements.
        heatSinks: Heat sink count.
        structuralIntegrity: Hull integrity value.
        chassisType: Hull configuration.
        fuel: Fuel capacity.
    """
    bays: Optional[List[TotalWarBayExtendedItem]] = Field(
        description="List of cargo and unit bays on the DropShip.",
        default=None
    )
    quarters: Optional[List[TotalWarBayBaseItem]] = Field(
        description="Crew quarters allocation (officers, enlisted, passengers, etc.).",
        default=None,
        examples=[{"officers": 8, "enlisted": 24, "passengers": 12}]
    )
    crewValues: Optional[List[TotalWarBayBaseItem]] = Field(
        description="Crew requirements (pilots, gunners, engineers, etc.).",
        default=None,
        examples=[{"pilots": 2, "gunners": 8, "crew": 16}]
    )
    heatSinks: Optional[TotalWarHeatSinkComponent] = Field(
        description="Total heat sinks.",
        default=None
    )
    structuralIntegrity: Optional[int] = Field(
        description="Hull structural integrity value. Affects critical hit resistance.",
        default=None,
        examples=[10, 15, 20, 30]
    )
    engine: Optional[TotalWarEngineComponent] = Field(
        description="Engine type and rating.",
        default_factory=TotalWarEngineComponent,
        examples=["300 Fusion Engine", "375 XL Engine", "400 Light Engine"]
    )
    chassisType: Optional[int] = Field(
        description="Hull configuration (Aerodyne, Spheroid).",
        default=None,
        examples=[0, 1]
    )
    fuel: Optional[int] = Field(
        description="Fuel capacity in points.",
        default=None
    )


# Extended classes with full equipment data

class TotalWarBattleMechExtendedData(TotalWarBattleMechData):
    """BattleMech data with full equipment details expanded.

    Extends TotalWarBattleMechData by replacing equipment IDs with
    complete EquipmentItem objects containing full statistics.
    """
    equipmentItems: Optional[List[EquipmentItem]] = Field(
        description="Complete equipment list with full item data instead of just IDs.",
        default=None
    )


class TotalWarVehicleExtendedData(TotalWarVehicleData):
    """Vehicle data with full equipment details expanded."""
    equipmentItems: Optional[List[EquipmentItem]] = Field(
        description="Complete equipment list with full item data.",
        default=None
    )


class TotalWarAerospaceExtendedData(TotalWarAerospaceData):
    """Aerospace data with full equipment details expanded."""
    equipmentItems: Optional[List[EquipmentItem]] = Field(
        description="Complete equipment list with full item data.",
        default=None
    )


class TotalWarInfantryExtendedData(TotalWarInfantryData):
    """Infantry data with full equipment details expanded."""
    equipmentItems: Optional[List[EquipmentItem]] = Field(
        description="Complete equipment list with full item data.",
        default=None
    )


class TotalWarDropshipExtendedData(TotalWarDropshipData):
    """DropShip data with full equipment details expanded."""
    equipmentItems: Optional[List[EquipmentItem]] = Field(
        description="Complete equipment list with full item data.",
        default=None
    )