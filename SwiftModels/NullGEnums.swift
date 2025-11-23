import Foundation

public enum UnitType: Int, Codable {
    case aerospace = 0
    case dropship = 1
    case mech = 2
    case infantry = 3
    case vehicle = 4
}

public enum TechbaseType: Int, Codable {
    case innerSphere = 0
    case clan = 1
    case all = 2
    case none = 3
}

public enum UnitSubtype: Int, Codable {
    case aerodyne = 0
    case aerospaceFighter = 1
    case battleArmor = 2
    case battleMech = 3
    case combatVehicle = 4
    case smallCraft = 5
    case conventionalInfantry = 6
    case conventionalFighter = 7
    case fixedWingSupport = 8
    case industrialMech = 9
    case omniFighter = 10
    case omniMech = 11
    case spheroid = 12
    case supportVehicle = 13
    case omniVehicle = 14
    case warship = 15
}

public enum RoleType: Int, Codable {
    case ambusher = 0
    case attackFighter = 1
    case brawler = 2
    case dogfighter = 3
    case fastDogfighter = 4
    case fireSupport = 5
    case interceptor = 6
    case juggernaut = 7
    case missileBoat = 8
    case scout = 9
    case skirmisher = 10
    case sniper = 11
    case striker = 12
    case transport = 13
    case undefined = 255
}

public enum WeightClassType: Int, Codable {
    case ultralight = 0
    case light = 1
    case medium = 2
    case heavy = 3
    case assault = 4
    case superHeavy = 5
}

public enum UnitCategoryType: Int, Codable {
    case official = 0
    case userCreated = 1
    case apocryphal = 2
    case illegal = 3
}

public enum RulesLevelType: Int, Codable {
    case introductory = 1
    case standard = 2
    case advanced = 3
    case experimental = 4
}

public enum TurretType: Int, Codable {
    case none = 0
    case single = 1
    case dual = 2
}

public enum JumpJetType: Int, Codable {
    case none = 0
    case regular = 1
    case improved = 2
    case umu = 3
}

public enum MotionType: String, Codable {
    case hover = "Hover"
    case hydrofoil = "Hydrofoil"
    case naval = "Naval"
    case rail = "Rail"
    case submarine = "Submarine"
    case tracked = "Tracked"
    case vtol = "VTOL"
    case wheeled = "Wheeled"
    case wiGE = "WiGE"
    case leg = "Leg"
    case umu = "UMU"
    case jump = "Jump"
    case bimodal = "Bimodal"
    case aerodyne = "Aerodyne"
    case motorized = "Motorized"
    case scuba = "SCUBA"
    case spheroid = "Spheroid"
}

public enum TotalWarEquipmentItemType: String, Codable {
    case ammo
    case equipment
    case bay
    case weaponbay
}

public enum EquipmentType: Int, Codable {
    case armor = 0
    case weapon = 1
    case ammo = 2
    case engine = 3
    case gyro = 4
    case structure = 5
    case cockpit = 6
    case other = 7
    case myomer = 8
    case manipulator = 9
    case heatsink = 10
    case conversion = 11
    case enhancement = 12
    case bay = 13
    case weaponbay = 14
}
