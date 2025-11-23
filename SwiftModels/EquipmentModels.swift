import Foundation

public struct EquipmentItem: Codable, Equatable {
    public var id: String?
    public var equipmentType: EquipmentType?
    public var name: String?
    public var techRating: String?
    public var techbase: TechbaseType?
    public var type: JSONValue?
    public var unitSubtypes: [UnitSubtype] = []
    public var version: Double?
    public var metadata: JSONDictionary?
    public var rulesLevel: Int?
    public var item: JSONValue?
}
