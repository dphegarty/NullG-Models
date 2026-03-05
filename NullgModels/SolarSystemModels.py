from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union, Literal, Dict

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


# ----------------------------
# Shared / helpers
# ----------------------------

class FrozenModel(BaseModel):
    """Read-only / immutable models."""
    model_config = ConfigDict(
        frozen=True,
        populate_by_name=True,
        extra="ignore",   # safer for forward-compat; switch to "forbid" if you want strict
    )


class IntClosedRange(FrozenModel):
    # Swift ClosedRange<Int> encodes as {"lowerBound": x, "upperBound": y}
    lowerBound: int
    upperBound: int


def _parse_swift_single_key_enum(value: Any) -> tuple[str, Any]:
    """
    Swift Codable associated-value enum often encodes as:
      { "caseName": <payload> }
    """
    if not isinstance(value, dict) or len(value) != 1:
        raise ValueError("Expected a single-key object like {\"case\": payload}.")
    (k, v), = value.items()
    return k, v


# ----------------------------
# Enums from Models.swift / ColonyModels.swift
# ----------------------------
class SatelliteObjectType(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"
    giant = "giant"
    rings = "rings"

class OrbitalRegion(str, Enum):
    hotZone = "hotZone"
    habitableZone = "habitableZone"
    outerZone = "outerZone"


class AtmosphericPressure(str, Enum):
    vacuum = "vacuum"
    trace = "trace"
    low = "low"
    normal = "normal"
    high = "high"
    veryHigh = "veryHigh"


class AtmosphericComposition(str, Enum):
    toxic = "toxic"
    tainted = "tainted"
    breathable = "breathable"


class PlanetaryTemperature(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    veryHigh = "veryHigh"


class PlanetaryHighestLifeForm(str, Enum):
    none = "none"
    microbes = "microbes"
    plants = "plants"
    insects = "insects"
    fish = "fish"
    amphibians = "amphibians"
    reptiles = "reptiles"
    birds = "birds"
    mammals = "mammals"


class DistanceZoneFromSol(str, Enum):
    coreInnerSphere = "coreInnerSphere"
    interiorInnerSphere = "interiorInnerSphere"
    frontierInnerSphere = "frontierInnerSphere"
    periphery = "periphery"
    outerPeriphery = "outerPeriphery"
    deepPeriphery = "deepPeriphery"
    outerLimits = "outerLimits"
    edgeOfUnknown = "edgeOfUnknown"
    vastExpanse = "vastExpanse"
    clanSpace = "clanSpace"


class Habitability(str, Enum):
    habitable = "habitable"
    marginal = "marginal"
    uninhabitable = "uninhabitable"


class GovernmentRegion(str, Enum):
    innerSphere = "innerSphere"
    periphery = "periphery"


class FactionAuthoritarianism(int, Enum):
    veryLiberal = -3
    liberal = -2
    typical = 0
    authoritarian = 2
    veryAuthoritarian = 3


class OccupancyHistory(int, Enum):
    preStarLeague = 1
    starLeagueHeyday = 2
    successionWarsRefugees = 3
    recentPeriphery = 4
    recentInnerSphere = 5
    recentClans = 6


class ColonyProfileKind(str, Enum):
    standard = "standard"
    lostColony = "lostColony"
    clanColony = "clanColony"
    outpost = "outpost"


class USILRLetter(int, Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    F = 4


class BaseGovernment(str, Enum):
    anarchy = "anarchy"
    democracy = "democracy"
    autocracyOligarchy = "autocracyOligarchy"
    dictatorship = "dictatorship"
    clan = "clan"


class GovernmentQualifier(str, Enum):
    athenianCyberdemocracy = "athenianCyberdemocracy"
    communist = "communist"
    confederacyAlliance = "confederacyAlliance"
    constitutional = "constitutional"
    corporate = "corporate"
    delegatedDemocracy = "delegatedDemocracy"
    demarchic = "demarchic"
    federal = "federal"
    feudal = "feudal"
    limitedDemocracyHybridRegime = "limitedDemocracyHybridRegime"
    monarchy = "monarchy"
    parliamentary = "parliamentary"
    republicRepresentativeDemocracy = "republicRepresentativeDemocracy"
    socialist = "socialist"
    theocracy = "theocracy"
    unitary = "unitary"
    confederacy = "confederacy"  # clan-only qualifiers
    federation = "federation"    # clan-only qualifiers


class HyperpulseGeneratorType(str, Enum):
    none = "none"
    ratedAHPG = "ratedAHPG"
    ratedBHPG = "ratedBHPG"
    ratedCService = "ratedCService"
    ratedDService = "ratedDService"


class RechargingStationLocation(str, Enum):
    none = "none"
    zenith = "zenith"
    nadir = "nadir"


# ----------------------------
# Models.swift output models
# ----------------------------

class StellarClassification(FrozenModel):
    class SpectralLetter(str, Enum):
        O = "O"
        B = "B"
        A = "A"
        F = "F"
        G = "G"
        K = "K"
        M = "M"

    letter: SpectralLetter
    subtype: int
    luminosityClass: str = "V"


class PrimarySolarStats(FrozenModel):
    spectralClass: str
    color: Optional[str] = None
    chargeTimeHours: int
    transitTimeDays: float
    safeJumpDistanceKm: int
    massSol: float
    luminositySol: float
    radiusSol: float
    surfaceTempK: float
    lifetimeMillionYears: float
    habitabilityModifier: int

    innerLifeZoneKm: int
    innerLifeZoneAU: float
    innerLifeZoneAvgTempK: float
    outerLifeZoneKm: int
    outerLifeZoneAU: float
    outerLifeZoneAvgTempK: float


class Star(FrozenModel):
    classification: StellarClassification
    stats: PrimarySolarStats


# NOTE:
# These types are referenced in your Swift file but NOT defined in the provided two files:
# - ObjectType
# - BeltWidthClass
# - BeltThermalClass
# - BeltComposition (referenced like a struct)
#
# For read-only/template-population purposes, it's safest to accept them as strings / minimal objects.
# If you later add the missing Swift definitions, we can tighten these to true enums.

class ObjectType(str, Enum):
    empty = "empty"
    asteroidBelt = "asteroidBelt"
    dwarfTerrestrial = "dwarfTerrestrial"
    terrestrial = "terrestrial"
    giantTerrestrial = "giantTerrestrial"
    gasGiant = "gasGiant"
    iceGiant = "iceGiant"

class BeltThermalClass(str, Enum):
    innerRocky = "innerRocky"
    outerIcu = "outerIcy"

class BeltWidthClass(str, Enum):
    narrow = "narrow"
    standard = "standard"
    wide = "wide"
    huge = "huge"


class BeltCompositionModel(FrozenModel):
    silicates: float
    metals: float
    ices: float
    carbonaceous: float


class Government(FrozenModel):
    base: BaseGovernment
    qualifiers: List[GovernmentQualifier] = Field(default_factory=list)


class TechSophisticationLetter(FrozenModel):
    type: Literal["letter"] = "letter"
    value: USILRLetter


class TechSophisticationAdvanced(FrozenModel):
    type: Literal["advanced"] = "advanced"


class TechSophisticationRegressed(FrozenModel):
    type: Literal["regressed"] = "regressed"


TechSophistication = Union[
    TechSophisticationLetter,
    TechSophisticationAdvanced,
    TechSophisticationRegressed,
]


class TechSophisticationSwift(RootModel[TechSophistication]):
    """
    Accepts Swift-like encoding:
      {"letter": 0}   (or {"letter":"A"} depending on your Swift JSONEncoder settings)
      "advanced"
      "regressed"
    Normalizes into a tagged union with a "type".
    """
    @field_validator("root", mode="before")
    @classmethod
    def parse_swift(cls, v: Any) -> Any:
        if isinstance(v, str):
            if v in ("advanced", "regressed"):
                return {"type": v}
            raise ValueError("Unknown TechSophistication string.")
        if isinstance(v, dict):
            k, payload = _parse_swift_single_key_enum(v)
            if k == "letter":
                # payload might be int (0..4) or "A"/"B"/...
                return {"type": "letter", "value": payload}
        raise ValueError("Invalid TechSophistication encoding.")


class USILR(FrozenModel):
    techSophistication: TechSophisticationSwift
    industrialDevelopment: USILRLetter
    rawMaterialDependence: USILRLetter
    industrialOutput: USILRLetter
    agriculturalDependence: USILRLetter


class Colony(FrozenModel):
    occupancy: OccupancyHistory
    population: int
    usilr: USILR
    government: Government
    rechargeStations: List[RechargingStationLocation]
    hpg: HyperpulseGeneratorType


class AsteroidBelt(FrozenModel):
    typicalRotationHours: int
    orbitAU: float
    widthAU: float
    innerEdgeAU: float
    outerEdgeAU: float
    widthClass: BeltWidthClass
    thermalClass: BeltThermalClass
    composition: BeltCompositionModel
    densityRating: float
    populationMultiplier: float
    dwarfBodyCount: int
    mediumAsteroidCount: int
    smallAsteroidCount: int
    dwarfBodySizeHintKm: IntClosedRange

    @field_validator("dwarfBodySizeHintKm", mode="before")
    @classmethod
    def parse_dwarfBodySizeHintKm(cls, v: Any):
        if isinstance(v, list) and len(v) == 2:
            return IntClosedRange(lowerBound=v[0], upperBound=v[1])
        if isinstance(v, IntClosedRange):
            return v
        raise ValueError("Invalid dwarfBodySizeHintKm encoding.")


class SatelliteObject(FrozenModel):
    type: SatelliteObjectType
    value: Union[PlanetBody, int]

    @field_validator("value", mode="before")
    @classmethod
    def parse_value(cls, v: Any) -> Any:
        if isinstance(v, dict):
            return PlanetBody.model_validate(v)
        elif isinstance(v, int):
            return v
        elif isinstance(v, str):
            return int(v)
        else:
            raise ValueError("Invalid satellite value encoding.")


class PlanetBody(FrozenModel):
    planetType: ObjectType
    atmosphericPressure: AtmosphericPressure
    diameterKm: float
    densityGPerCm3: float
    dayLengthHours: int
    surfaceGravityG: float
    escapeVelocityMps: float
    orbitalPeriodYears: float
    habitable: bool
    percentSurfaceWater: float
    atmosphericComposition: AtmosphericComposition
    temperature: PlanetaryTemperature
    highestLifeForm: PlanetaryHighestLifeForm
    satellites: Optional[List[SatelliteObject]] = None
    colony: Optional[Colony] = None

    @field_validator("planetType", mode="before")
    @classmethod
    def parse_planetType(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return ObjectType(value)
        elif isinstance(v, str):
            return ObjectType(v)

    @field_validator("atmosphericPressure", mode="before")
    @classmethod
    def parse_atmosphericPressure(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return AtmosphericPressure(value)
        elif isinstance(v, str):
            return AtmosphericPressure(v)

    @field_validator("atmosphericComposition", mode="before")
    @classmethod
    def parse_atmosphericComposition(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return AtmosphericComposition(value)
        elif isinstance(v, str):
            return AtmosphericComposition(v)

    @field_validator("temperature", mode="before")
    @classmethod
    def parse_temperature(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return PlanetaryTemperature(value)
        elif isinstance(v, str):
            return PlanetaryTemperature(v)

    @field_validator("highestLifeForm", mode="before")
    @classmethod
    def parse_highestLifeForm(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return PlanetaryHighestLifeForm(value)
        elif isinstance(v, str):
            return PlanetaryHighestLifeForm(v)

    @field_validator("satellites", mode="before")
    @classmethod
    def parse_satellites(cls, v) -> Any:
        convertedObjectsList = []
        if isinstance(v, list):
            for satellite in v:
                if isinstance(satellite, dict):
                    (satelliteObjectType, payload) = _parse_swift_single_key_enum(satellite)
                    if isinstance(payload, dict):
                        (_, value) = _parse_swift_single_key_enum(payload)
                        satelliteValue = {"type": satelliteObjectType, "value": value}
                        convertedObjectsList.append(SatelliteObject.model_validate(satelliteValue))
        if len(convertedObjectsList) > 0:
            return convertedObjectsList
        return None


class OrbitalObjectEmpty(FrozenModel):
    type: Literal["empty"] = "empty"


class OrbitalObjectAsteroidBelt(FrozenModel):
    type: Literal["asteroidBelt"] = "asteroidBelt"
    value: AsteroidBelt


class OrbitalObjectDwarfTerrestrial(FrozenModel):
    type: Literal["dwarfTerrestrial"] = "dwarfTerrestrial"
    value: PlanetBody


class OrbitalObjectTerrestrial(FrozenModel):
    type: Literal["terrestrial"] = "terrestrial"
    value: PlanetBody


class OrbitalObjectGiantTerrestrial(FrozenModel):
    type: Literal["giantTerrestrial"] = "giantTerrestrial"
    value: PlanetBody


class OrbitalObjectGasGiant(FrozenModel):
    type: Literal["gasGiant"] = "gasGiant"
    value: PlanetBody


class OrbitalObjectIceGiant(FrozenModel):
    type: Literal["iceGiant"] = "iceGiant"
    value: PlanetBody


OrbitalObjectUnion = Union[
    OrbitalObjectEmpty,
    OrbitalObjectAsteroidBelt,
    OrbitalObjectDwarfTerrestrial,
    OrbitalObjectTerrestrial,
    OrbitalObjectGiantTerrestrial,
    OrbitalObjectGasGiant,
    OrbitalObjectIceGiant,
]


class OrbitalObject(RootModel[OrbitalObjectUnion]):
    """
    Parses Swift enum encoding for OrbitalObject:

    - "empty"
    - {"asteroidBelt": {...}}
    - {"terrestrial": {...}}
    etc.

    Normalizes to a tagged union with {"type": ..., "value": ...} (or type-only for empty).
    """
    @field_validator("root", mode="before")
    @classmethod
    def parse_swift(cls, v: Any) -> Any:
        if v == "empty":
            return {"type": "empty"}
        if isinstance(v, dict):
            (objectType, payload), = v.items()
            if objectType == "empty":
                return {"type": "empty", "value": {}}
            (k, payload) = _parse_swift_single_key_enum(value=payload)
            return {"type": objectType, "value": payload}
        raise ValueError("Invalid OrbitalObject encoding.")


class OrbitalSlot(FrozenModel):
    slotIndex: int
    baseAU: float
    orbitalRadiusAU: float
    orbitalRadiusKm: float
    region: OrbitalRegion
    object: OrbitalObjectUnion

    @field_validator("object", mode="before")
    @classmethod
    def parse_swift(cls, v: Any) -> Any:
        if v == "empty":
            return OrbitalObjectEmpty.model_validate({"type": "empty", "value": {}})
        if isinstance(v, dict):
            (objectType, payload), = v.items()
            if objectType == "empty":
                return OrbitalObjectEmpty.model_validate({"type": "empty", "value": {}})
            (k, payload) = _parse_swift_single_key_enum(value=payload)
            objectData = {"type": objectType, "value": payload}
            if objectType == ObjectType.asteroidBelt:
                return OrbitalObjectAsteroidBelt.model_validate(objectData)
            elif objectType == ObjectType.dwarfTerrestrial:
                return OrbitalObjectDwarfTerrestrial.model_validate(objectData)
            elif objectType == ObjectType.terrestrial:
                return OrbitalObjectTerrestrial.model_validate(objectData)
            elif objectType == ObjectType.giantTerrestrial:
                return OrbitalObjectGiantTerrestrial.model_validate(objectData)
            elif objectType == ObjectType.gasGiant:
                return OrbitalObjectGasGiant.model_validate(objectData)
            elif objectType == ObjectType.iceGiant:
                return OrbitalObjectIceGiant.model_validate(objectData)
            return {"type": objectType, "value": payload}
        raise ValueError("Invalid OrbitalObject encoding.")


class SolarSystem(FrozenModel):
    id: str  # UUID as string in JSON
    name: str
    seed: int
    star: Star
    distanceFromSol: int
    orbitalSlots: List[OrbitalSlot]


# ----------------------------
# ColonyModels.swift input models (optional)
# (You said server models are read-only; including these is useful if you ever ship inputs to server.)
# ----------------------------

class ColonyPlanetInputs(FrozenModel):
    habitability: Habitability
    atmosphereQuality: AtmosphericComposition
    hasHighPollution: bool
    hasVeryHighTemperature: bool
    gravityG: float
    waterCoverage: float
    densityGcm3: Optional[float] = None


class ColonyGenerationInputs(FrozenModel):
    planet: ColonyPlanetInputs
    distanceFromTerraLY: int
    distanceZoneFromTerra: DistanceZoneFromSol = DistanceZoneFromSol.interiorInnerSphere
    yearsSinceSettlement: Optional[int] = None
    occupancyOverride: Optional[OccupancyHistory] = None
    isUltraAdvancedResearchHub: bool = False
    colonyProfileKind: ColonyProfileKind = ColonyProfileKind.standard
    governmentRegion: GovernmentRegion = GovernmentRegion.periphery
    factionAuthoritarianism: FactionAuthoritarianism = FactionAuthoritarianism.typical
    forceClanGovernment: bool = False
    governmentOverride: Optional[Government] = None