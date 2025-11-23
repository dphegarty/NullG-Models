import Foundation

public struct TotalWarBasicComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType?
}

public struct TotalWarArmorComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .armor
    public var barRating: Int?
}

public struct TotalWarEngineComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .engine
    public var rating: Int?
    public var type: String?
}

public struct TotalWarStructureComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .structure
}

public struct TotalWarMyomerComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .myomer
}

public struct TotalWarGyroComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .gyro
}

public struct TotalWarCockpitComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .cockpit
}

public struct TotalWarHeatSinkComponent: Codable, Equatable {
    public var name: String?
    public var id: String?
    public var techbase: String?
    public var equipmentType: EquipmentType? = .heatsink
    public var type: Int?
    public var count: Int?
    public var criticalFree: Int?
    public var engineBase: Int?
    public var omniBase: Int?
}

public struct TotalWarBayBaseItem: Codable, Equatable {
    public var name: String?
    public var value: Double?
}

public struct TotalWarBayExtendedItem: Codable, Equatable {
    public var name: String?
    public var value: Double?
    public var id: String?
    public var doors: Int?
}

public struct TotalWarArmorLocation: Codable, Equatable {
    public var armor: String?
    public var location: String?
    public var value: Int?
}

public struct TotalWarEquipmentItem: Codable, Equatable {
    public var id: String?
    public var name: String?
    public var location: String?
    public var options: String?
    public var type: TotalWarEquipmentItemType?
}

public struct TotalWarCriticalLocationItem: Codable, Equatable {
    public var location: String?
    public var slots: [String]?
}

public struct TotalWarUnitDataBase: Codable, Equatable {
    public var armor: TotalWarArmorComponent?
    public var bv: Double?
    public var config: String?
    public var constructionInvalid: [String]?
    public var constructionValidated: Bool?
    public var mass: Double?
    public var pv: Int?
    public var source: String?
    public var techbase: String?
    public var version: Double?
    public var unitDataSourceUri: String?
    public var equipmentList: [TotalWarEquipmentItem]?
    public var armorLocations: [TotalWarArmorLocation]?
    public var copyrightTrademark: String?
    public var runMp: Int?
    public var motionType: MotionType?
    public var productionYear: Int?
    public var rulesLevel: RulesLevelType?
    public var walkMp: Int?
    public var trooperCount: Int?
    public var jumpMp: Int?
    public var armorFactor: Int?
    public var armorFactorMax: Int?
    public var extraOptions: [String: Bool]?
    public var fireControl: String?
}

public struct TotalWarBattleMechData: Codable, Equatable {
    public var armor: TotalWarArmorComponent?
    public var bv: Double?
    public var config: String?
    public var constructionInvalid: [String]?
    public var constructionValidated: Bool?
    public var mass: Double?
    public var pv: Int?
    public var source: String?
    public var techbase: String?
    public var version: Double?
    public var unitDataSourceUri: String?
    public var equipmentList: [TotalWarEquipmentItem]?
    public var armorLocations: [TotalWarArmorLocation]?
    public var copyrightTrademark: String?
    public var runMp: Int?
    public var motionType: MotionType?
    public var productionYear: Int?
    public var rulesLevel: RulesLevelType?
    public var walkMp: Int?
    public var trooperCount: Int?
    public var jumpMp: Int?
    public var armorFactor: Int?
    public var armorFactorMax: Int?
    public var extraOptions: [String: Bool]?
    public var fireControl: String?

    public var cockpit: TotalWarCockpitComponent?
    public var engine: TotalWarEngineComponent? = TotalWarEngineComponent()
    public var gyro: TotalWarGyroComponent?
    public var heatSinks: TotalWarHeatSinkComponent?
    public var myomer: TotalWarMyomerComponent?
    public var structure: TotalWarStructureComponent?
    public var weapons: Int?
    public var criticalLocations: [TotalWarCriticalLocationItem]?
    public var productionEra: Int?
    public var jumpjetType: JumpJetType?
}

public struct TotalWarAerospaceData: Codable, Equatable {
    public var armor: TotalWarArmorComponent?
    public var bv: Double?
    public var config: String?
    public var constructionInvalid: [String]?
    public var constructionValidated: Bool?
    public var mass: Double?
    public var pv: Int?
    public var source: String?
    public var techbase: String?
    public var version: Double?
    public var unitDataSourceUri: String?
    public var equipmentList: [TotalWarEquipmentItem]?
    public var armorLocations: [TotalWarArmorLocation]?
    public var copyrightTrademark: String?
    public var runMp: Int?
    public var motionType: MotionType?
    public var productionYear: Int?
    public var rulesLevel: RulesLevelType?
    public var walkMp: Int?
    public var trooperCount: Int?
    public var jumpMp: Int?
    public var armorFactor: Int?
    public var armorFactorMax: Int?
    public var extraOptions: [String: Bool]?
    public var fireControl: String?

    public var cockpit: TotalWarCockpitComponent?
    public var engine: TotalWarEngineComponent? = TotalWarEngineComponent()
    public var fuel: Int?
    public var transportSpace: [TotalWarBayBaseItem]?
    public var heatSinks: TotalWarHeatSinkComponent?
    public var structure: TotalWarStructureComponent?
    public var safeThrust: Int?
    public var weapons: Int?
    public var productionEra: Int?
    public var extraHardPoints: Int?
    public var externalStores: Int?
    public var structuralIntegrity: Int?
}

public struct TotalWarInfantryData: Codable, Equatable {
    public var armor: TotalWarArmorComponent?
    public var bv: Double?
    public var config: String?
    public var constructionInvalid: [String]?
    public var constructionValidated: Bool?
    public var mass: Double?
    public var pv: Int?
    public var source: String?
    public var techbase: String?
    public var version: Double?
    public var unitDataSourceUri: String?
    public var equipmentList: [TotalWarEquipmentItem]?
    public var armorLocations: [TotalWarArmorLocation]?
    public var copyrightTrademark: String?
    public var runMp: Int?
    public var motionType: MotionType?
    public var productionYear: Int?
    public var rulesLevel: RulesLevelType?
    public var walkMp: Int?
    public var trooperCount: Int?
    public var jumpMp: Int?
    public var armorFactor: Int?
    public var armorFactorMax: Int?
    public var extraOptions: [String: Bool]?
    public var fireControl: String?

    public var structure: TotalWarStructureComponent?
    public var trooperMass: Double?
    public var productionEra: Int?
    public var squads: Int?
    public var squadSize: Int?
    public var secondaryWeaponTroops: Int?
    public var isExoskeleton: Bool?
    public var antiMechSkill: Int?
    public var augmentation: [String]?
}

public struct TotalWarVehicleData: Codable, Equatable {
    public var armor: TotalWarArmorComponent?
    public var bv: Double?
    public var config: String?
    public var constructionInvalid: [String]?
    public var constructionValidated: Bool?
    public var mass: Double?
    public var pv: Int?
    public var source: String?
    public var techbase: String?
    public var version: Double?
    public var unitDataSourceUri: String?
    public var equipmentList: [TotalWarEquipmentItem]?
    public var armorLocations: [TotalWarArmorLocation]?
    public var copyrightTrademark: String?
    public var runMp: Int?
    public var motionType: MotionType?
    public var productionYear: Int?
    public var rulesLevel: RulesLevelType?
    public var walkMp: Int?
    public var trooperCount: Int?
    public var jumpMp: Int?
    public var armorFactor: Int?
    public var armorFactorMax: Int?
    public var extraOptions: [String: Bool]?
    public var fireControl: String?

    public var engine: TotalWarEngineComponent? = TotalWarEngineComponent()
    public var turretType: TurretType?
    public var transportSpace: [TotalWarBayBaseItem]?
    public var structure: TotalWarStructureComponent?
    public var productionEra: Int?
    public var hasControlSystems: Bool?
    public var heatSinks: TotalWarHeatSinkComponent?
    public var isTrailer: Bool?
    public var extraCombatSeats: Int?
    public var jumpjetType: JumpJetType?
}

public struct TotalWarDropshipData: Codable, Equatable {
    public var armor: TotalWarArmorComponent?
    public var bv: Double?
    public var config: String?
    public var constructionInvalid: [String]?
    public var constructionValidated: Bool?
    public var mass: Double?
    public var pv: Int?
    public var source: String?
    public var techbase: String?
    public var version: Double?
    public var unitDataSourceUri: String?
    public var equipmentList: [TotalWarEquipmentItem]?
    public var armorLocations: [TotalWarArmorLocation]?
    public var copyrightTrademark: String?
    public var runMp: Int?
    public var motionType: MotionType?
    public var productionYear: Int?
    public var rulesLevel: RulesLevelType?
    public var walkMp: Int?
    public var trooperCount: Int?
    public var jumpMp: Int?
    public var armorFactor: Int?
    public var armorFactorMax: Int?
    public var extraOptions: [String: Bool]?
    public var fireControl: String?

    public var bays: [TotalWarBayExtendedItem]?
    public var quarters: [TotalWarBayBaseItem]?
    public var crewValues: [TotalWarBayBaseItem]?
    public var heatSinks: TotalWarHeatSinkComponent?
    public var structuralIntegrity: Int?
    public var engine: TotalWarEngineComponent? = TotalWarEngineComponent()
    public var chassisType: Int?
    public var fuel: Int?
}

public struct TotalWarBattleMechExtendedData: Codable, Equatable {
    public var base: TotalWarBattleMechData
    public var equipmentItems: [EquipmentItem]?
}

public struct TotalWarVehicleExtendedData: Codable, Equatable {
    public var base: TotalWarVehicleData
    public var equipmentItems: [EquipmentItem]?
}

public struct TotalWarAerospaceExtendedData: Codable, Equatable {
    public var base: TotalWarAerospaceData
    public var equipmentItems: [EquipmentItem]?
}

public struct TotalWarInfantryExtendedData: Codable, Equatable {
    public var base: TotalWarInfantryData
    public var equipmentItems: [EquipmentItem]?
}

public struct TotalWarDropshipExtendedData: Codable, Equatable {
    public var base: TotalWarDropshipData
    public var equipmentItems: [EquipmentItem]?
}
