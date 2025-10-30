"""Enumeration types for NullG Battletech database models.

This module defines all enumeration classes used throughout the NullG system
for categorizing and classifying Battletech units, equipment, and game systems.
These enums provide type-safe integer and string constants for database queries
and model validation.

All enums inherit from IntEnum or str/Enum to provide both integer values
(for database storage) and readable names (for API responses and UI display).
"""

from enum import Enum, IntEnum


class GameSystem(Enum):
    """Supported Battletech game systems.
    
    Identifies which game ruleset a unit or data belongs to. Used to
    differentiate between Total Warfare tactical rules and Alpha Strike
    fast-play rules, or other game variants.
    
    Attributes:
        none: No specific game system assigned.
        totalWar: Total Warfare tactical game system (classic Battletech).
        alphaStrike: Alpha Strike fast-play game system.
        hardWar: HardWar game system (separate game, not Battletech).
        
    Examples:
        >>> GameSystem.totalWar.value
        1
        >>> GameSystem.alphaStrike.name
        'alphaStrike'
    """
    none = 0
    totalWar = 1
    alphaStrike = 2
    hardWar = 3


class OperationStatus(str, Enum):
    """Status indicators for API operation results.
    
    String-based enum for indicating whether an API operation completed
    successfully or encountered an error. Used in DataResultItem responses
    to communicate operation outcomes to clients.
    
    Attributes:
        success: Operation completed successfully.
        failure: Operation failed due to an error.
        
    Examples:
        >>> OperationStatus.success
        'success'
        >>> result.status = OperationStatus.failure
    """
    success = "success"
    failure = "failure"


class TechbaseType(IntEnum):
    """Technology base classifications for units and equipment.
    
    Identifies whether a unit or piece of equipment uses Inner Sphere
    technology, Clan technology, or a mixture of both. This affects
    construction rules, availability, and game balance.
    
    Attributes:
        inner_sphere: Inner Sphere technology (ID: 0).
        clan: Clan technology (ID: 1).
        all: Mixed technology or available to both (ID: 2).
        none: No technology base assigned (ID: 3).
        
    Usage:
        Use in queries to filter units by technology:
        >>> {"techbaseId": TechbaseType.clan}  # Find Clan units
        
    Examples:
        >>> TechbaseType.inner_sphere
        0
        >>> TechbaseType.clan.name
        'clan'
    """
    inner_sphere = 0
    clan = 1
    all = 2
    none = 3


class EquipmentType(IntEnum):
    """Categories of equipment and components.
    
    Classifies equipment items into functional categories for filtering
    and organization. Used to group similar equipment types together
    in searches and UI displays.
    
    Attributes:
        armor: Armor plating (ID: 0).
        weapon: Weapon systems (ID: 1).
        ammo: Ammunition (ID: 2).
        engine: Engine types (ID: 3).
        gyro: Gyroscope systems (ID: 4).
        structure: Internal structure types (ID: 5).
        cockpit: Cockpit and control systems (ID: 6).
        other: Miscellaneous equipment (ID: 7).
        myomer: Muscle enhancement systems (ID: 8).
        manipulator: Hands and manipulator systems (ID: 9).
        heatsink: Heat dissipation systems (ID: 10).
        conversion: Equipment conversion systems (ID: 11).
        enhancement: Performance enhancement systems (ID: 12).
        bay: Cargo and equipment bays (ID: 13).
        weaponbay: Weapon mounting bays (ID: 14).
        
    Usage:
        Filter equipment by type:
        >>> {"equipmentTypeId": EquipmentType.weapon}  # Find all weapons
        
    Examples:
        >>> EquipmentType.weapon
        1
        >>> EquipmentType.heatsink.name
        'heatsink'
    """
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
    """Unit weight classifications by tonnage.
    
    Categorizes units into weight classes based on their mass/tonnage.
    Weight class affects movement, armor capacity, firepower, and tactical
    role in the game.
    
    Attributes:
        ultralight: Ultra-light units, typically under 20 tons (ID: 0).
        light: Light units, 20-35 tons (ID: 1).
        medium: Medium units, 40-55 tons (ID: 2).
        heavy: Heavy units, 60-75 tons (ID: 3).
        assault: Assault units, 80-100 tons (ID: 4).
        superHeavy: Super-heavy units, over 100 tons (ID: 5).
        
    Usage:
        Filter units by weight class:
        >>> {"weightClassId": WeightClass.assault}  # Find assault mechs
        >>> {"weightClassId": {"$in": [3, 4]}}  # Heavy and assault
        
    Examples:
        >>> WeightClass.assault
        4
        >>> WeightClass.light.name
        'light'
    """
    ultralight = 0
    light = 1
    medium = 2
    heavy = 3
    assault = 4
    superHeavy = 5


class UnitCategory(IntEnum):
    """Source and validation status of unit data.
    
    Indicates the origin and validation status of a unit entry in the
    database. Helps users determine data quality and canonical status.
    
    Attributes:
        official: Official unit from published Battletech sources (ID: 0).
        userCreated: User-generated custom unit design (ID: 1).
        apocryphal: Unofficial or non-canonical unit (ID: 2).
        illegal: Unit violates construction rules or game balance (ID: 3).
        
    Usage:
        Filter for official units only:
        >>> {"unitCategory": UnitCategory.official}
        
    Examples:
        >>> UnitCategory.official
        0
        >>> UnitCategory.userCreated.name
        'userCreated'
    """
    official = 0
    userCreated = 1
    apocryphal = 2
    illegal = 3


class UnitType(IntEnum):
    """Primary unit type categories.
    
    High-level classification of unit types by their fundamental nature
    and role on the battlefield. This is the broadest categorization
    of combat units.
    
    Attributes:
        aerospace: Aerospace fighters and spacecraft (ID: 0).
        dropship: DropShips and transport vessels (ID: 1).
        mech: BattleMechs and IndustrialMechs (ID: 2).
        infantry: Infantry and Battle Armor (ID: 3).
        vehicle: Ground and naval vehicles (ID: 4).
        
    Usage:
        Filter by unit type:
        >>> {"unitTypeId": UnitType.mech}  # Find all mechs
        >>> {"unitTypeId": {"$in": [2, 4]}}  # Mechs and vehicles
        
    Examples:
        >>> UnitType.mech
        2
        >>> UnitType.aerospace.name
        'aerospace'
    """
    aerospace = 0
    dropship = 1
    mech = 2
    infantry = 3
    vehicle = 4


class UnitSubtype(IntEnum):
    """Detailed unit subtype classifications.
    
    Provides granular categorization within each unit type for more
    specific filtering and classification. Subtypes define special
    characteristics and construction rules.
    
    Attributes:
        Aerodyne: Aerodyne DropShip (streamlined) (ID: 0).
        AerospaceFighter: Standard aerospace fighter (ID: 1).
        BattleArmor: Powered battle armor infantry (ID: 2).
        BattleMech: Standard BattleMech (ID: 3).
        CombatVehicle: Military combat vehicle (ID: 4).
        ConvFighter: Conventional fighter aircraft (ID: 5).
        Conventional: Conventional infantry (ID: 6).
        ConventionalFighter: Conventional atmospheric fighter (ID: 7).
        FixedWingSupport: Fixed-wing support aircraft (ID: 8).
        IndustrialMech: Industrial work mech (ID: 9).
        OmniFighter: Omni-configuration fighter (ID: 10).
        OmniMech: Omni-configuration BattleMech (ID: 11).
        Spheroid: Spheroid DropShip (egg-shaped) (ID: 12).
        SupportVehicle: Non-combat support vehicle (ID: 13).
        
    Usage:
        Filter for specific subtypes:
        >>> {"unitSubtypeId": UnitSubtype.OmniMech}  # Find OmniMechs
        >>> {"unitSubtypeId": {"$in": [3, 11]}}  # BattleMechs and OmniMechs
        
    Examples:
        >>> UnitSubtype.BattleMech
        3
        >>> UnitSubtype.OmniMech.name
        'OmniMech'
    """
    Aerodyne = 0
    AerospaceFighter = 1
    BattleArmor = 2
    BattleMech = 3
    CombatVehicle = 4
    ConvFighter = 5
    Conventional = 6
    ConventionalFighter = 7
    FixedWingSupport = 8
    IndustrialMech = 9
    OmniFighter = 10
    OmniMech = 11
    Spheroid = 12
    SupportVehicle = 13


class InventoryStorageType(Enum):
    """Storage types for user inventory and collections.
    
    Categorizes how units are stored in user collections, whether as
    physical inventory, bookmarks for later reference, or temporary
    search results.
    
    Attributes:
        inventory: Physical inventory of owned units (ID: 0).
        bookmark: Saved/bookmarked units for reference (ID: 1).
        searchResults: Temporary search result storage (ID: 3).
        formationMember: Unit as part of a formation (ID: 4).
        
    Note:
        ID 2 is skipped in the sequence (legacy reasons).
        
    Examples:
        >>> InventoryStorageType.inventory
        0
        >>> InventoryStorageType.bookmark.name
        'bookmark'
    """
    inventory = 0
    bookmark = 1
    searchResults = 3
    formationMember = 4


class UnitExperienceLevels(IntEnum):
    """Pilot/crew experience and skill levels.
    
    Defines experience levels for unit crews and pilots, affecting
    their combat effectiveness, target numbers, and special abilities.
    Lower IDs represent higher experience levels.
    
    Attributes:
        legendary: Legendary elite pilots (ID: 0).
        heroic: Heroic veteran pilots (ID: 1).
        elite: Elite professional pilots (ID: 2).
        veteran: Veteran experienced pilots (ID: 3).
        regular: Regular trained pilots (ID: 4).
        green: Green rookie pilots (ID: 5).
        veryGreen: Very inexperienced pilots (ID: 6).
        wetBehindTheEars: Minimally trained pilots (ID: 7).
        
    Usage:
        Track unit crew quality:
        >>> unit.experienceLevel = UnitExperienceLevels.veteran
        >>> {"experience": {"$lte": UnitExperienceLevels.elite}}  # Elite or better
        
    Examples:
        >>> UnitExperienceLevels.elite
        2
        >>> UnitExperienceLevels.green.name
        'green'
    """
    legendary = 0
    heroic = 1
    elite = 2
    veteran = 3
    regular = 4
    green = 5
    veryGreen = 6
    wetBehindTheEars = 7


class OrganizationType(IntEnum):
    """Types of military organizations and unit groupings.
    
    Classifies organizational structures for grouping units together
    into formations, army lists, and command hierarchies.
    
    Attributes:
        organization: General military organization (ID: 0).
        armyList: Specific army list or force composition (ID: 1).
        
    Examples:
        >>> OrganizationType.armyList
        1
        >>> OrganizationType.organization.name
        'organization'
    """
    organization = 0
    armyList = 1


class RecordSheetType(IntEnum):
    """Types of unit record sheets for gameplay.
    
    Identifies which game system's record sheet format should be used
    for a unit. Different game systems have different data requirements
    and presentation formats.
    
    Attributes:
        none: No record sheet type specified (ID: 0).
        totalWar: Total Warfare record sheet format (ID: 1).
        alphaStrike: Alpha Strike card format (ID: 2).
        
    Usage:
        Determine which record sheet to generate:
        >>> if unit.recordSheetType == RecordSheetType.totalWar:
        ...     generate_classic_sheet(unit)
        
    Examples:
        >>> RecordSheetType.totalWar
        1
        >>> RecordSheetType.alphaStrike.name
        'alphaStrike'
    """
    none = 0
    totalWar = 1
    alphaStrike = 2

class HeatSinkType(IntEnum):
    single = 1
    double = 2
    compact = 3
    laser = 4
    freezer = 5
    prototype = 6

class TurretType(IntEnum):
    """
    Turret configuration types for vehicles and ships.

    Identifies the configuration of a turret on a vehicle or ship.

    Attributes:
        none: No turret configuration (ID: 0).
        single: Single turret (ID: 1).
        duel: Dual turret (ID: 2).

    Examples:
        >>> TurretType.single
        1
        >>> TurretType.duel.name
        'duel'
    """
    none = 0
    single = 1
    duel = 2

class JumpJetType(IntEnum):
    """
    Jump Jet configuration types for units

    Describes what type of jump jet a unit has.

    Attributes:
        none: No jump jet (ID: 0).
        regular: Regular jump jet (ID: 1).
        improved: Improved jump jet (ID: 2).
        umu: UMU jump jet (ID: 3).

    Examples:
        >>> JumpJetType.regular
        1
        >>> JumpJetType.improved.name
        'improved'
    """
    none = 0
    regular = 1
    improved = 2
    umu = 3

class RoleType(IntEnum):
    """
    Describes the role assigned to the unit

    Attributes:
        ambusher: Ambusher role (ID: 0).
        attack_fighter: Attack fighter role (ID: 1).
        brawler: Brawler role (ID: 2).
        dogfighter: Dogfighter role (ID: 3).
        fast_dogfighter: Fast dogfighter role (ID: 4).
        fire_support: Fire support role (ID: 5).
        interceptor: Interceptor role (ID: 6).
        juggernaut: Juggernaut role (ID: 7).
        missile_boat: Missile boat role (ID: 8).
        scout: Scout role (ID: 9).
        skirmisher: Skirmisher role (ID: 10).
        sniper: Sniper role (ID: 11).
        striker: Striker role (ID: 12).
        transport: Transport role (ID: 13).

        Examples:
            >>> RoleType.ambusher
            0
            >>> RoleType.attack_fighter.name
            'attack_fighter'
    """
    ambusher = 0
    attack_fighter = 1
    brawler = 2
    dogfighter = 3
    fast_dogfighter = 4
    fire_support = 5
    interceptor = 6
    juggernaut = 7
    missile_boat = 8
    scout = 9
    skirmisher = 10
    sniper = 11
    striker = 12
    transport = 13

class TotalWarEquipmentItemType(Enum):
    """
    Describes the type of equipment item in the Total War Equipment item record

    Attributes:
        ammo: Ammo item
        equipment: Equipment item
        bay: Bay item
        weaponbay: Weapons Bay (used on Dropships and other large craft)

    Examples:
        >>> TotalWarEquipmentItemType.ammo
        'ammo'
        >>> TotalWarEquipmentItemType.equipment
        'equipment'
        >>> TotalWarEquipmentItemType.bay
        'bay'
        >>> TotalWarEquipmentItemType.weaponbay
        'weaponbay'
    """
    ammo = "ammo"
    equipment = "equipment"
    bay = "bay"
    weaponbay = "weaponbay"
