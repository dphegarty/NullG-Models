"""Data models for Alpha Strike game system.

This module defines Pydantic models for the Alpha Strike fast-play variant
of Battletech. Alpha Strike simplifies the classic Battletech rules for
faster gameplay while maintaining tactical depth.

Alpha Strike uses simplified unit cards with consolidated damage values,
special abilities, and streamlined movement. These models represent the
data needed for Alpha Strike unit cards, including damage arcs for large
units, special abilities, and point values.

For more information on Alpha Strike rules, see:
https://bg.battletech.com/books/alpha-strike/
"""

from typing import Optional, List
from pydantic import Field
from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import UnitType, RoleType


class AlphaStrikeArcFormattedSpecialItem(NullGBaseModel):
    """Formatted special abilities for a specific firing arc on large units.
    
    Large units (DropShips, WarShips, etc.) have different special abilities
    available in different firing arcs (Front, Left, Right, Rear, etc.).
    This model groups formatted special ability strings by arc.
    
    Attributes:
        name: The firing arc name (e.g., "Front", "Left Side", "Rear", "Turret").
        value: List of formatted special ability codes for this arc
              (e.g., ["AC2/2/2", "LRM2/2/2", "CASE"]).
              
    Examples:
        >>> arc_special = AlphaStrikeArcFormattedSpecialItem(
        ...     name="Front",
        ...     value=["AC2/2/2", "LRM1/1/1", "AMS"]
        ... )
        >>> print(f"{arc_special.name}: {', '.join(arc_special.value)}")
        Front: AC2/2/2, LRM1/1/1, AMS
    """
    name: Optional[str] = Field(
        description="Name of the firing arc (Front, Left Side, Right Side, Rear, Turret, etc.)",
        default=None,
        examples=["Front", "Left Side", "Rear", "Turret"]
    )
    value: Optional[List[str]] = Field(
        description="List of formatted special ability codes for this arc. "
                   "Each string represents a special ability with its values "
                   "(e.g., 'AC2/2/2' for Autocannon with 2 damage at each range).",
        default=None,
        examples=[
            ["AC2/2/2", "LRM1/1/1"],
            ["CASE", "AMS", "PNT1/1/1"],
            ["SCAP2/2/2/2"]
        ]
    )


class AlphaStrikeDamageRecord(NullGBaseModel):
    """Damage values at different range bands.
    
    Alpha Strike uses four range bands: Short, Medium, Long, and Extreme.
    This model records the damage a weapon or arc can deal at each range.
    
    Attributes:
        short: Damage at short range (0-6 inches).
        medium: Damage at medium range (7-12 inches).
        long: Damage at long range (13-24 inches).
        extreme: Damage at extreme range (25-48 inches, aerospace only).
        
    Examples:
        >>> damage = AlphaStrikeDamageRecord(
        ...     short=4.0,
        ...     medium=4.0,
        ...     long=2.0,
        ...     extreme=0.0
        ... )
        >>> print(f"Damage: {damage.short}/{damage.medium}/{damage.long}")
        Damage: 4.0/4.0/2.0
    """
    short: Optional[float] = Field(
        description="Damage value at short range (0-6 inches in Alpha Strike)",
        default=None,
        examples=[4.0, 2.5, 0.0]
    )
    medium: Optional[float] = Field(
        description="Damage value at medium range (7-12 inches in Alpha Strike)",
        default=None,
        examples=[4.0, 2.0, 0.0]
    )
    long: Optional[float] = Field(
        description="Damage value at long range (13-24 inches in Alpha Strike)",
        default=None,
        examples=[2.0, 1.0, 0.0]
    )
    extreme: Optional[float] = Field(
        description="Damage value at extreme range (25-48 inches, aerospace units only)",
        default=None,
        examples=[1.0, 0.5, 0.0]
    )


class AlphaStrikeArcDamageMapItem(NullGBaseModel):
    """Damage records categorized by weapon type for a firing arc.
    
    Large units can have multiple weapon systems with different damage types.
    This model organizes damage by weapon category (Standard, Capital,
    Sub-Capital, etc.) for a single firing arc.
    
    Attributes:
        STD: Standard weapon damage (conventional weapons, lasers, PPCs, etc.).
        SCAP: Sub-capital weapon damage (light capital weapons).
        MSL: Capital missile damage (missile-based capital weapons).
        FLAK: Anti-aircraft flak damage (for engaging aerospace targets).
        PNT: Point defense damage (for intercepting missiles and fighters).
        CAP: Capital weapon damage (heavy ship-killer weapons).
        
    Note:
        Not all weapon types are present on every unit. Capital weapons
        are only found on WarShips and some large DropShips.
        
    Examples:
        >>> arc_damage = AlphaStrikeArcDamageMapItem(
        ...     STD=AlphaStrikeDamageRecord(short=4.0, medium=4.0, long=2.0),
        ...     PNT=AlphaStrikeDamageRecord(short=1.0, medium=1.0, long=1.0)
        ... )
    """
    STD: Optional[AlphaStrikeDamageRecord] = Field(
        description="Standard weapon damage map for this arc. "
                   "Includes conventional weapons like autocannons, lasers, and PPCs.",
        default=None
    )
    SCAP: Optional[AlphaStrikeDamageRecord] = Field(
        description="Sub-capital weapon damage map for this arc. "
                   "Light capital-scale weapons for engaging smaller capital ships.",
        default=None
    )
    MSL: Optional[AlphaStrikeDamageRecord] = Field(
        description="Capital missile damage map for this arc. "
                   "Includes Barracuda, White Shark, and Killer Whale missiles.",
        default=None
    )
    FLAK: Optional[AlphaStrikeDamageRecord] = Field(
        description="Anti-aircraft flak damage map for this arc. "
                   "Used to engage aerospace fighters and other flying units.",
        default=None
    )
    PNT: Optional[AlphaStrikeDamageRecord] = Field(
        description="Point defense damage map for this arc. "
                   "Used to intercept incoming missiles and aerospace fighters.",
        default=None
    )
    CAP: Optional[AlphaStrikeDamageRecord] = Field(
        description="Capital weapon damage map for this arc. "
                   "Heavy ship-to-ship weapons like Naval Autocannons and Gauss.",
        default=None
    )


class AlphaStrikeArcDamageMap(NullGBaseModel):
    """Complete damage mapping for a single firing arc on a large unit.
    
    Combines the arc name with its categorized damage values. Large units
    have multiple instances of this model, one for each firing arc.
    
    Attributes:
        name: The firing arc name.
        value: Damage map item containing all weapon type damage records for this arc.
        
    Examples:
        >>> front_arc = AlphaStrikeArcDamageMap(
        ...     name="Front",
        ...     value=AlphaStrikeArcDamageMapItem(
        ...         STD=AlphaStrikeDamageRecord(short=6.0, medium=6.0, long=4.0),
        ...         PNT=AlphaStrikeDamageRecord(short=2.0, medium=2.0, long=2.0)
        ...     )
        ... )
    """
    name: Optional[str] = Field(
        description="Name of the firing arc this damage map represents. "
                   "Common arcs: Front, Left Side, Right Side, Rear, Turret.",
        default=None,
        examples=["Front", "Left Side", "Right Side", "Rear", "Turret"]
    )
    value: Optional[AlphaStrikeArcDamageMapItem] = Field(
        description="Complete damage map for this arc, categorized by weapon type.",
        default=None
    )


class AlphaStrikeSpecialDamageItem(AlphaStrikeDamageRecord):
    """Special ability with associated damage values.
    
    Some Alpha Strike special abilities deal damage (like Artillery, Air-to-Ground,
    etc.). This model records both the special ability name and its damage
    values at different ranges.
    
    Attributes:
        name: Special ability name code (e.g., "AC", "LRM", "ARTS", "AMS").
        count: Number of instances of this special (for multiples).
        short: Damage at short range for this special.
        medium: Damage at medium range for this special.
        long: Damage at long range for this special.
        extreme: Damage at extreme range (aerospace) for this special.
        inTurret: Whether this special is mounted in a turret (can fire in any direction).
        
    Examples:
        >>> autocannon = AlphaStrikeSpecialDamageItem(
        ...     name="AC",
        ...     count=2,
        ...     short=2.0,
        ...     medium=2.0,
        ...     long=2.0,
        ...     inTurret=False
        ... )
        >>> print(f"{autocannon.name}{autocannon.count}: {autocannon.short}/{autocannon.medium}/{autocannon.long}")
        AC2: 2.0/2.0/2.0
    """
    name: Optional[str] = Field(
        description="Special ability code name (AC=Autocannon, LRM=Long Range Missiles, "
                   "ARTS=Artillery, AMS=Anti-Missile System, etc.)",
        default="",
        examples=["AC", "LRM", "ARTS", "AMS", "ATM", "SRM"]
    )
    count: Optional[int] = Field(
        description="Number of instances of this special ability on the unit. "
                   "Used when the same special appears multiple times.",
        default=0,
        examples=[1, 2, 3]
    )
    inTurret: Optional[bool] = Field(
        description="Whether this special is mounted in a turret. "
                   "Turret weapons can fire in any direction regardless of unit facing.",
        default=False,
        examples = [True, False]
    )
    isSSW: Optional[bool] = Field(
        description="Whether this special is mounted in a Squad Support Weapon."
                    "This is only for Battle Armor units.",
        default=False,
        examples=[True, False]
    )


class AlphaStrikeData(NullGBaseModel):
    """Complete Alpha Strike game data for a unit.
    
    This model contains all the information needed to play a unit in the
    Alpha Strike fast-play game system. It includes movement, damage,
    armor, special abilities, and point values.
    
    Alpha Strike simplifies classic Battletech by:
    - Consolidating all weapons into single damage values per range
    - Using special ability codes instead of individual equipment
    - Streamlining movement and combat resolution
    - Using point values (PV) instead of Battle Value (BV)
    
    Attributes:
        formattedSpecials: List of special ability strings formatted for display
                          (e.g., "AC2/2/2", "LRM1/1/1", "CASE").
        specials: List of raw special ability codes (e.g., ["AC", "LRM", "CASE"]).
        specialsDamage: List of special abilities that deal damage with their values.
        version: Version number of the Alpha Strike data schema.
        trooperCount: Number of individual soldiers (for infantry/battle armor units).
        isAero: Whether this is an aerospace unit (uses aerospace rules).
        skill: Pilot/crew skill rating (typically 2-7, lower is better).
        useOfficialPoints: Whether to use official PV or calculated PV.
        calculatedPV: Calculated point value based on unit stats.
        officialPV: Official point value from Master Unit List (may differ from calculated).
        armorThreshold: Armor threshold for aerospace units (damage reduction).
        isLAM: Whether this is a Land-Air Mech (can transform between modes).
        baseUnitType: Base unit type from Total Warfare (see UnitType enum).
        unitType: Alpha Strike unit type classification string.
        size: Unit size category (affects terrain interactions and targeting).
        walk: Ground movement rate in inches per turn.
        jump: Jump movement rate in inches per turn (0 if no jump capability).
        movementMode: Primary movement type (e.g., "Ground", "VTOL", "Hover", "Wheeled").
        armor: Total armor points (damage capacity before destruction).
        structure: Internal structure points (additional damage capacity for some units).
        isArmed: Whether the unit has weapons (false for unarmed support units).
        damage: Daamge values for the unit at ranges.
        overheat: Overheat value (heat threshold for energy weapons).
        role: Tactical role identifier (see Master Unit List roles).
        tmm: Target Movement Modifier (defensive bonus from speed).
        arcversion: Version number for arc-based damage system (large units).
        skillDifference: Difference from standard skill rating of 4.
        skillPoints: Point value adjustment for non-standard skill.
        isLargeUnit: Whether this is a large unit with firing arcs (DropShip, WarShip).
        arcFormatedSpecials: Special abilities organized by firing arc (large units only).
        arcDamageMaps: Damage values organized by firing arc (large units only).
        hasArtillerySystem: Whether the unit has artillery capability (ARTS special).
        hasC3System: Whether the unit has C3 computer networking (C3 specials).
        
    Examples:
        >>> # Standard BattleMech
        >>> mech_data = AlphaStrikeData(
        ...     unitType="BM",
        ...     size=2,
        ...     walk=8,
        ...     jump=0,
        ...     armor=6,
        ...     structure=3,
        ...     damageShort=3.0,
        ...     damageMedium=3.0,
        ...     damageLong=1.0,
        ...     overheat=1,
        ...     tmm=2,
        ...     calculatedPV=35,
        ...     specials=["CASE"],
        ...     formattedSpecials=["CASE"]
        ... )
        
        >>> # Large DropShip with arcs
        >>> dropship_data = AlphaStrikeData(
        ...     unitType="DS",
        ...     size=4,
        ...     aero=True,
        ...     isLargeUnit=True,
        ...     armor=20,
        ...     structure=10,
        ...     armorThreshold=4,
        ...     arcDamageMaps=[
        ...         AlphaStrikeArcDamageMap(name="Front", value=...),
        ...         AlphaStrikeArcDamageMap(name="Left Side", value=...),
        ...         # ... more arcs
        ...     ]
        ... )
    """
    formattedSpecials: Optional[List[str]] = Field(
        description="List of formatted special ability strings ready for display on unit cards. "
                   "Format: 'ABILITY#/#/#' where numbers are damage at S/M/L ranges. "
                   "Examples: 'AC2/2/2', 'LRM1/1/1', 'CASE', 'AMS'.",
        default_factory=list,
        examples=[
            ["AC2/2/2", "LRM1/1/1", "CASE"],
            ["AMS", "ECM", "PRB"],
            ["ARTS-BA", "CASE", "SRM1/1/0"]
        ]
    )
    specials: Optional[List[str]] = Field(
        description="List of unformatted special ability codes. "
                   "Raw ability names without damage values or formatting. "
                   "See Alpha Strike rules for complete special abilities list.",
        default_factory=list,
        examples=[
            ["AC", "LRM", "CASE"],
            ["AMS", "ECM", "PRB"],
            ["ARTS", "CASE", "SRM"]
        ]
    )
    specialsDamage: Optional[List[AlphaStrikeSpecialDamageItem]] = Field(
        description="List of special abilities that deal damage with their specific damage values. "
                   "Used for abilities that have variable damage not included in main damage values.",
        default_factory=list
    )
    version: Optional[float] = Field(
        description="Schema version number for this Alpha Strike data structure. "
                   "Used to track data model changes over time.",
        default=0.0,
        examples=[1.0, 2.0, 2.5]
    )
    trooperCount: Optional[int] = Field(
        description="Number of individual soldiers or troopers in this unit. "
                   "Used for infantry squads and battle armor points. "
                   "Typically 1-5 for battle armor, higher for conventional infantry.",
        default=1,
        examples=[4, 5, 28]
    )
    isAero: Optional[bool] = Field(
        description="Whether this unit uses aerospace movement and combat rules. "
                   "True for fighters, DropShips, and other spacecraft.",
        default=False,
        examples=[True, False]
    )
    skill: Optional[int] = Field(
        description="Pilot/crew skill rating. Standard skill is 4. "
                   "Lower numbers are better (more skilled). Range: 2-7. "
                   "Affects to-hit rolls and point value.",
        default=0,
        examples=[2, 3, 4, 5, 6]
    )
    useOfficialPoints: Optional[bool] = Field(
        description="Whether to use official PV from Master Unit List or calculated PV. "
                   "Official values are sometimes outdated or incorrect.",
        default=False,
        examples=[True, False]
    )
    calculatedPV: Optional[int] = Field(
        description="Point Value calculated from unit stats using Alpha Strike formula. "
                   "Used for force balancing and scenario design.",
        default=0,
        examples=[25, 35, 42, 58]
    )
    officialPV: Optional[int] = Field(
        description="Official Point Value as published in Master Unit List. "
                   "Note: These values are not always accurate or up-to-date. "
                   "calculatedPV is often more reliable.",
        default=0,
        examples=[24, 36, 41, 57]
    )
    armorThreshold: Optional[int] = Field(
        description="Armor Threshold for aerospace units. "
                   "Damage below this value is ignored. Only on large aerospace units.",
        default=0,
        examples=[2, 4, 6]
    )
    isLAM: Optional[bool] = Field(
        description="Whether this is a Land-Air Mech (LAM). "
                   "LAMs can transform between mech, fighter, and hybrid modes.",
        default=False,
        examples=[True, False]
    )
    baseUnitType: Optional[UnitType] = Field(
        description="Base unit type from Total Warfare system (see UnitType enum). "
                   "Maps to: 0=aerospace, 1=dropship, 2=mech, 3=infantry, 4=vehicle.",
        default=None,
        examples=[0, 1, 2, 3, 4]
    )
    unitType: Optional[str] = Field(
        description="Alpha Strike unit type code. "
                   "Common types: BM=BattleMech, CV=Combat Vehicle, AF=Aerospace Fighter, "
                   "BA=Battle Armor, IM=IndustrialMech, SV=Support Vehicle, DS=DropShip.",
        default=None,
        examples=["BM", "CV", "AF", "BA", "IM", "DS", "SV"]
    )
    size: Optional[int] = Field(
        description="Unit size category. Affects terrain interactions and to-hit modifiers. "
                   "1=small (infantry, light mech), 2=medium (medium vehicles), 3=large (heavy mechs), "
                   "4=very large (DropShips, assault mech).",
        default=0,
        examples=[1, 2, 3, 4]
    )
    walk: Optional[int] = Field(
        description="Ground movement rate in inches per turn. "
                   "Standard movement without running or jumping. "
                   "0 means immobile or aerospace-only movement.",
        default=0,
        examples=[0, 4, 6, 8, 10, 12]
    )
    jump: Optional[int] = Field(
        description="Jump movement rate in inches per turn. "
                   "Movement using jump jets, ignoring terrain. "
                   "0 or None means no jump capability.",
        default=0,
        examples=[0, 4, 6, 8]
    )
    movementMode: Optional[str] = Field(
        description="Primary movement mode/type. "
                   "Ground=standard ground movement, VTOL=vertical takeoff/landing, "
                   "Hover=hovering over terrain, Wheeled=wheeled vehicle, etc.",
        default="",
        examples=["", "v", "h", "Ww", "t", "j"]
    )
    armor: Optional[int] = Field(
        description="Total armor points. This is the unit's damage capacity. "
                   "When reduced to 0, the unit is destroyed. "
                   "Can be reduced by enemy fire during combat.",
        default=0,
        examples=[3, 6, 8, 12, 20]
    )
    structure: Optional[int] = Field(
        description="Internal structure points. "
                   "Additional damage capacity after armor is depleted. "
                   "Not all units have structure (mainly mechs and vehicles).",
        default=0,
        examples=[0, 2, 3, 4, 6]
    )
    isArmed: Optional[bool] = Field(
        description="Whether the unit is considered armed/combat-capable. "
                   "False for unarmed support vehicles and transport units.",
        default=False,
        examples=[True, False]
    )
    damage: Optional[AlphaStrikeDamageRecord] = Field(
        description="Complete damage record for this unit. "
                   "Includes damage at short, medium, and long ranges. "
                   "Can be used to calculate point value.",
        default_factory=AlphaStrikeDamageRecord
    )
    overheat: Optional[int] = Field(
        description="Overheat value. Number of heat points generated by firing all weapons. "
                   "If unit fires, it takes this much damage to itself. "
                   "0 or None means no overheat (no energy weapons or has sufficient heat sinks).",
        default=0,
        examples=[0, 1, 2, 3]
    )
    role: Optional[RoleType] = Field(
        description="Tactical role identifier from Master Unit List. "
                   "Defines the unit's intended battlefield function. "
                   "Common roles: Scout, Striker, Skirmisher, Brawler, Juggernaut, Missile Boat, Sniper.",
        default=0,
        examples=[0, 1, 2, 3, 4, 5, 6]
    )
    tmm: Optional[int] = Field(
        description="Target Movement Modifier. Defensive bonus from unit speed. "
                   "Added to opponent's to-hit roll. Higher is better for defense. "
                   "Based on movement rate: 0=immobile, 1-4+ based on speed.",
        default=0,
        examples=[0, 1, 2, 3, 4]
    )
    arcversion: Optional[float] = Field(
        description="Version number for firing arc damage system. "
                   "Used by large units with directional firing arcs (DropShips, WarShips).",
        default=0.0,
        examples=[1.0, 2.0]
    )
    skillDifference: Optional[int] = Field(
        description="Difference between unit's skill rating and standard skill (4). "
                   "Positive means worse than standard, negative means better. "
                   "Used in point value calculations.",
        default=0,
        examples=[-2, -1, 0, 1, 2]
    )
    skillPoints: Optional[int] = Field(
        description="Point value adjustment for non-standard pilot skill. "
                   "Better pilots cost more points, worse pilots reduce cost. "
                   "Applied to calculatedPV to get final point value.",
        default=0,
        examples=[-10, -5, 0, 5, 10]
    )
    isLargeUnit: Optional[bool] = Field(
        description="Whether this is a large unit with firing arcs. "
                   "True for DropShips, WarShips, and some large support vehicles. "
                   "Large units use arcDamageMaps instead of simple damage values.",
        default=False,
        examples=[True, False]
    )
    arcFormatedSpecials: Optional[List[AlphaStrikeArcFormattedSpecialItem]] = Field(
        description="Special abilities organized by firing arc for large units. "
                   "Each arc (Front, Left, Right, Rear, etc.) has its own list of specials. "
                   "Only used when isLargeUnit is True.",
        default_factory=list
    )
    arcDamageMaps: Optional[List[AlphaStrikeArcDamageMap]] = Field(
        description="Damage values organized by firing arc for large units. "
                   "Each arc has separate damage values for different weapon types. "
                   "Only used when isLargeUnit is True.",
        default_factory=list
    )
    hasArtillerySystem: Optional[bool] = Field(
        description="Whether the unit has artillery capability (ARTS special ability). "
                   "Artillery can perform indirect fire attacks and barrage attacks.",
        default=False,
        examples=[True, False]
    )
    hasC3System: Optional[bool] = Field(
        description="Whether the unit has C3 computer networking (C3 family of specials). "
                   "C3 allows sharing targeting data between linked units for accuracy bonuses.",
        default=False,
        examples=[True, False]
    )
