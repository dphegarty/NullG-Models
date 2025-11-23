import Foundation

public struct BasicItem: Codable, Equatable {
    public var category: String?
    public var name: String
    public var id: Int
}

public struct EraItem: Codable, Equatable {
    public var id: Int
    public var name: String
    public var yearStart: Int
    public var yearEnd: Int
}

public struct BoxsetItem: Codable, Equatable {
    public var id: String
    public var name: String
    public var completed: Bool
    public var modelCount: Int
    public var maxPoints: Int
    public var minPoints: Int
    public var maxBattleValue: Int
    public var minBattleValue: Int
}

public struct MULUnitItem: Codable, Equatable {
    public var mulTypeId: Int
    public var mulType: String
    public var name: String
    public var id: Int
    public var mass: Double
    public var bv: Int
    public var pv: Int
    public var role: String
    public var roleId: Int
    public var source: String
    public var rulesLevel: String
    public var rulesLevelId: Int
    public var era: String
    public var eraId: Int
    public var intro: Int
    public var pullDate: String
    public var availableEras: [Int]
    public var factions: [Int]
    public var nullgId: String
}

public enum TotalWarData: Codable, Equatable {
    case battleMech(TotalWarBattleMechData)
    case vehicle(TotalWarVehicleData)
    case infantry(TotalWarInfantryData)
    case aerospace(TotalWarAerospaceData)
    case dropship(TotalWarDropshipData)

    public init(from decoder: Decoder) throws {
        if let mech = try? TotalWarBattleMechData(from: decoder) {
            self = .battleMech(mech)
        } else if let vehicle = try? TotalWarVehicleData(from: decoder) {
            self = .vehicle(vehicle)
        } else if let infantry = try? TotalWarInfantryData(from: decoder) {
            self = .infantry(infantry)
        } else if let aero = try? TotalWarAerospaceData(from: decoder) {
            self = .aerospace(aero)
        } else if let drop = try? TotalWarDropshipData(from: decoder) {
            self = .dropship(drop)
        } else {
            throw DecodingError.dataCorrupted(.init(codingPath: decoder.codingPath, debugDescription: "Unknown Total War payload"))
        }
    }

    public func encode(to encoder: Encoder) throws {
        switch self {
        case .battleMech(let value):
            try value.encode(to: encoder)
        case .vehicle(let value):
            try value.encode(to: encoder)
        case .infantry(let value):
            try value.encode(to: encoder)
        case .aerospace(let value):
            try value.encode(to: encoder)
        case .dropship(let value):
            try value.encode(to: encoder)
        }
    }
}

public enum TotalWarExtendedData: Codable, Equatable {
    case battleMech(TotalWarBattleMechExtendedData)
    case vehicle(TotalWarVehicleExtendedData)
    case infantry(TotalWarInfantryExtendedData)
    case aerospace(TotalWarAerospaceExtendedData)
    case dropship(TotalWarDropshipExtendedData)

    public init(from decoder: Decoder) throws {
        if let mech = try? TotalWarBattleMechExtendedData(from: decoder) {
            self = .battleMech(mech)
        } else if let vehicle = try? TotalWarVehicleExtendedData(from: decoder) {
            self = .vehicle(vehicle)
        } else if let infantry = try? TotalWarInfantryExtendedData(from: decoder) {
            self = .infantry(infantry)
        } else if let aero = try? TotalWarAerospaceExtendedData(from: decoder) {
            self = .aerospace(aero)
        } else if let drop = try? TotalWarDropshipExtendedData(from: decoder) {
            self = .dropship(drop)
        } else {
            throw DecodingError.dataCorrupted(.init(codingPath: decoder.codingPath, debugDescription: "Unknown extended Total War payload"))
        }
    }

    public func encode(to encoder: Encoder) throws {
        switch self {
        case .battleMech(let value):
            try value.encode(to: encoder)
        case .vehicle(let value):
            try value.encode(to: encoder)
        case .infantry(let value):
            try value.encode(to: encoder)
        case .aerospace(let value):
            try value.encode(to: encoder)
        case .dropship(let value):
            try value.encode(to: encoder)
        }
    }
}

public struct UnitData: Codable, Equatable {
    public var id: String?
    public var name: String?
    public var model: String?
    public var productionEra: Int?
    public var mass: Double?
    public var version: Double?
    public var bv: Double?
    public var pv: Int?
    public var techbase: String?
    public var mulId: Int?
    public var weightClass: WeightClassType?
    public var role: RoleType?
    public var rulesLevel: RulesLevelType?
    public var barcodes: [String]?
    public var fullName: String?
    public var metadata: [String: Bool]?
    public var notes: String?
    public var unitCategory: UnitCategoryType?
    public var factions: [Int]?
    public var creationSource: String?
    public var productionYear: Int?
    public var availableEras: [Int]?
    public var alphaStrike: AlphaStrikeData?
    public var alphaStrikeResults: JSONDictionary?
    public var unitType: UnitType?
    public var unitSubtype: UnitSubtype?
    public var expanded: Bool = false
    public var totalWar: TotalWarData?
    public var bvResults: JSONDictionary?
    public var statistics: JSONDictionary?
    public var pilotData: [PilotData]? = []
}

public struct UnitDataExtended: Codable, Equatable {
    public var id: String?
    public var name: String?
    public var model: String?
    public var productionEra: Int?
    public var mass: Double?
    public var version: Double?
    public var bv: Double?
    public var pv: Int?
    public var techbase: String?
    public var mulId: Int?
    public var weightClass: WeightClassType?
    public var role: RoleType?
    public var rulesLevel: RulesLevelType?
    public var barcodes: [String]?
    public var fullName: String?
    public var metadata: [String: Bool]?
    public var notes: String?
    public var unitCategory: UnitCategoryType?
    public var factions: [Int]?
    public var creationSource: String?
    public var productionYear: Int?
    public var availableEras: [Int]?
    public var alphaStrike: AlphaStrikeData?
    public var alphaStrikeResults: JSONDictionary?
    public var unitType: UnitType?
    public var unitSubtype: UnitSubtype?
    public var expanded: Bool = true
    public var totalWar: TotalWarExtendedData?
    public var bvResults: JSONDictionary?
    public var statistics: JSONDictionary?
    public var pilotData: [PilotData]? = []
    public var mulData: MULUnitItem?
}
