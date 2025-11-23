import Foundation

public struct AlphaStrikeArcFormattedSpecialItem: Codable, Equatable {
    public var name: String?
    public var value: [String]?
}

public struct AlphaStrikeDamageRecord: Codable, Equatable {
    public var short: Double?
    public var medium: Double?
    public var long: Double?
    public var extreme: Double?
}

public struct AlphaStrikeArcDamageMapItem: Codable, Equatable {
    public var STD: AlphaStrikeDamageRecord?
    public var SCAP: AlphaStrikeDamageRecord?
    public var MSL: AlphaStrikeDamageRecord?
    public var FLAK: AlphaStrikeDamageRecord?
    public var PNT: AlphaStrikeDamageRecord?
    public var CAP: AlphaStrikeDamageRecord?
}

public struct AlphaStrikeArcDamageMap: Codable, Equatable {
    public var name: String?
    public var value: AlphaStrikeArcDamageMapItem?
}

public struct AlphaStrikeSpecialDamageItem: Codable, Equatable {
    public var name: String?
    public var count: Int?
    public var short: Double?
    public var medium: Double?
    public var long: Double?
    public var extreme: Double?
    public var inTurret: Bool?
    public var isSSW: Bool?
}

public struct AlphaStrikeData: Codable, Equatable {
    public var formattedSpecials: [String] = []
    public var specials: [String] = []
    public var specialsDamage: [AlphaStrikeSpecialDamageItem] = []
    public var version: Double?
    public var trooperCount: Int?
    public var isAero: Bool?
    public var skill: Int?
    public var useOfficialPoints: Bool?
    public var calculatedPV: Int?
    public var officialPV: Int?
    public var armorThreshold: Int?
    public var isLAM: Bool?
    public var baseUnitType: UnitType?
    public var unitType: String?
    public var size: Int?
    public var walk: Int?
    public var jump: Int?
    public var movementMode: String?
    public var armor: Int?
    public var structure: Int?
    public var isArmed: Bool?
    public var damage: AlphaStrikeDamageRecord? = AlphaStrikeDamageRecord()
    public var overheat: Int?
    public var tmm: Int?
    public var arcversion: Double?
    public var skillDifference: Int?
    public var skillPoints: Int?
    public var isLargeUnit: Bool?
    public var arcFormatedSpecials: [AlphaStrikeArcFormattedSpecialItem] = []
    public var arcDamageMaps: [AlphaStrikeArcDamageMap] = []
    public var hasArtillerySystem: Bool?
    public var hasC3System: Bool?
}
