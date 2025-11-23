import Foundation

public struct Skills: Codable, Equatable {
    public var piloting: Int? = 5
    public var gunnery: Int? = 4
}

public struct PilotData: Codable, Equatable {
    public var id: String?
    public var firstName: String?
    public var lastName: String?
    public var skills: Skills?
    public var bio: String?
    public var organizationId: String?
    public var kills: Int?
    public var deaths: Int?
    public var imageUrl: String?
}
