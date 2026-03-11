from __future__ import annotations

import re
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

    def summary(self) -> str:
        return f"{self.lowerBound} - {self.upperBound}"


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

    def displayName(self):
        text = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', self.value)
        text = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', text)
        return text.title()

class AtmosphericPressure(str, Enum):
    vacuum = "vacuum"
    trace = "trace"
    low = "low"
    normal = "normal"
    high = "high"
    veryHigh = "veryHigh"

    def displayName(self) -> str:
        if self == AtmosphericPressure.vacuum:
            return "Vacuum"
        elif self == AtmosphericPressure.trace:
            return "Trace"
        elif self == AtmosphericPressure.low:
            return "Low"
        elif self == AtmosphericPressure.normal:
            return "Normal"
        elif self == AtmosphericPressure.high:
            return "High"
        elif self == AtmosphericPressure.veryHigh:
            return "Very High"
        return ""


class AtmosphericComposition(str, Enum):
    none = "none"
    toxic = "toxic"
    tainted = "tainted"
    breathable = "breathable"

    def displayName(self) -> str:
        return self.value.title()


class PlanetaryTemperature(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    veryHigh = "veryHigh"

    def displayName(self) -> str:
        if self == PlanetaryTemperature.low:
            return "Low"
        elif self == PlanetaryTemperature.medium:
            return "Medium"
        elif self == PlanetaryTemperature.high:
            return "High"
        elif self == PlanetaryTemperature.veryHigh:
            return "Very High"
        return ""


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

    def displayName(self) -> str:
        return self.value.title()


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

    def displayName(self) -> str:
        return self.value.title()


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

    def displayName(self) -> str:
        if self == OccupancyHistory.preStarLeague:
            return "Pre-Star League"
        elif self == OccupancyHistory.starLeagueHeyday:
            return "Star League Heyday"
        elif self == OccupancyHistory.successionWarsRefugees:
            return "Succession Wars Refugees"
        elif self == OccupancyHistory.recentPeriphery:
            return "Recent Periphery"
        elif self == OccupancyHistory.recentInnerSphere:
            return "Recent Inner Sphere"
        elif self == OccupancyHistory.recentClans:
            return "Recent Clans"
        return ""


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

    def displayName(self) -> str:
        return self.name.title()


class BaseGovernment(str, Enum):
    anarchy = "anarchy"
    democracy = "democracy"
    autocracyOligarchy = "autocracyOligarchy"
    dictatorship = "dictatorship"
    clan = "clan"

    def displayName(self) -> str:
        if self == BaseGovernment.anarchy:
            return "Anarchy"
        elif self == BaseGovernment.democracy:
            return "Democracy"
        elif self == BaseGovernment.autocracyOligarchy:
            return "Autocracy/Oligarchy"
        elif self == BaseGovernment.dictatorship:
            return "Dictatorship"
        elif self == BaseGovernment.clan:
            return "Clan"
        return ""


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

    def displayName(self) -> str:
        if self == GovernmentQualifier.athenianCyberdemocracy:
            return "Athenian Cyberdemocracy"
        elif self == GovernmentQualifier.communist:
            return "Communist"
        elif self == GovernmentQualifier.confederacyAlliance:
            return "Confederacy Alliance"
        elif self == GovernmentQualifier.constitutional:
            return "Constitutional"
        elif self == GovernmentQualifier.corporate:
            return "Corporate"
        elif self == GovernmentQualifier.delegatedDemocracy:
            return "Delegated Democracy"
        elif self == GovernmentQualifier.demarchic:
            return "Demarchic"
        elif self == GovernmentQualifier.federal:
            return "Federal"
        elif self == GovernmentQualifier.feudal:
            return "Feudal"
        elif self == GovernmentQualifier.limitedDemocracyHybridRegime:
            return "Limited Democracy Hybrid Regime"
        elif self == GovernmentQualifier.monarchy:
            return "Monarchy"
        elif self == GovernmentQualifier.parliamentary:
            return "Parliamentary"
        elif self == GovernmentQualifier.republicRepresentativeDemocracy:
            return "Republic Representative Democracy"
        elif self == GovernmentQualifier.socialist:
            return "Socialist"
        elif self == GovernmentQualifier.theocracy:
            return "Theocracy"
        elif self == GovernmentQualifier.unitary:
            return "Unitary"
        elif self == GovernmentQualifier.confederacy:
            return "Confederacy"
        elif self == GovernmentQualifier.federation:
            return "Federation"
        return ""


class HyperpulseGeneratorType(str, Enum):
    none = "none"
    ratedAHPG = "ratedAHPG"
    ratedBHPG = "ratedBHPG"
    ratedCService = "ratedCService"
    ratedDService = "ratedDService"

    def displayName(self) -> str:
        if self == HyperpulseGeneratorType.none:
            return "None"
        elif self == HyperpulseGeneratorType.ratedAHPG:
            return "A Rated HPG"
        elif self == HyperpulseGeneratorType.ratedBHPG:
            return "B Rated HPG"
        elif self == HyperpulseGeneratorType.ratedCService:
            return "C Rated Service"
        elif self == HyperpulseGeneratorType.ratedDService:
            return "D Rated Service"
        return ""


class RechargingStationLocation(str, Enum):
    none = "none"
    zenith = "zenith"
    nadir = "nadir"

    def displayName(self) -> str:
        return self.value.title()

class ReportClassificationType(str, Enum):
    unclassified = "unclassified"
    restricted = "restricted"
    confidential = "confidential"
    secret = "secret"
    topSecret = "topSecret"

    def displayName(self) -> str:
        if self == ReportClassificationType.unclassified:
            return "UNCLASSIFIED"
        elif self == ReportClassificationType.restricted:
            return "RESTRICTED"
        elif self == ReportClassificationType.confidential:
            return "CONFIDENTIAL"
        elif self == ReportClassificationType.secret:
            return "SECRET"
        elif self == ReportClassificationType.topSecret:
            return "TOP SECRET"
        return ""

class ReportPreparedByType(str, Enum):
    survey = "survey"
    ship = "ship"
    office = "office"
    other = "other"

    def displayName(self) -> str:
        if self == ReportPreparedByType.survey:
            return "Survey"
        elif self == ReportPreparedByType.ship:
            return "Ship"
        elif self == ReportPreparedByType.office:
            return "Office"
        elif self == ReportPreparedByType.other:
            return "Other"
        return ""

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

    def displayName(self):
        return f"{self.classification.letter}{self.classification.subtype}{self.classification.luminosityClass}"


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

    def displayName(self) -> str:
        if self == ObjectType.empty:
            return "Empty"
        elif self == ObjectType.asteroidBelt:
            return "Asteroid Belt"
        elif self == ObjectType.dwarfTerrestrial:
            return "Dwarf Terrestrial"
        elif self == ObjectType.terrestrial:
            return "Terrestrial"
        elif self == ObjectType.giantTerrestrial:
            return "Giant Terrestrial"
        elif self == ObjectType.gasGiant:
            return "Gas Giant"
        elif self == ObjectType.iceGiant:
            return "Ice Giant"
        return ""

class BeltThermalClass(str, Enum):
    innerRocky = "innerRocky"
    outerIcu = "outerIcy"

    def displayName(self) -> str:
        if self == BeltThermalClass.innerRocky:
            return "Inner Rocky"
        elif self == BeltThermalClass.outerIcu:
            return "Outer Icy"
        return ""

class BeltWidthClass(str, Enum):
    narrow = "narrow"
    standard = "standard"
    wide = "wide"
    huge = "huge"

    def displayName(self) -> str:
        return self.value.title()

class BeltCompositionModel(FrozenModel):
    silicates: float
    metals: float
    ices: float
    carbonaceous: float

    def compositionSummary(self) -> str:
        return f"{self.silicates:.2f} silicates, {self.metals:.2f} metals, {self.ices:.2f} ices, {self.carbonaceous:.2f} carbonaceous"


class Government(FrozenModel):
    base: BaseGovernment
    qualifiers: List[GovernmentQualifier] = Field(default_factory=list)

    @field_validator("base", mode="before")
    @classmethod
    def parse_base(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return BaseGovernment(value)
        elif isinstance(v, str):
            return BaseGovernment(v)

    def qualifiersSummary(self) -> str:
        return ", ".join(self.qualifiers)


class TechSophisticationLetter(FrozenModel):
    type: Literal["letter"] = "letter"
    value: USILRLetter

    def displayName(self) -> str:
        return self.value.displayName()


class TechSophisticationAdvanced(FrozenModel):
    type: Literal["advanced"] = "advanced"

    def displayName(self) -> str:
        return "Advanced"


class TechSophisticationRegressed(FrozenModel):
    type: Literal["regressed"] = "regressed"

    def displayName(self) -> str:
        return "Regressed"


TechSophistication = Union[
    TechSophisticationLetter,
    TechSophisticationAdvanced,
    TechSophisticationRegressed,
]

class USILR(FrozenModel):
    techSophistication: TechSophistication
    industrialDevelopment: USILRLetter
    rawMaterialDependence: USILRLetter
    industrialOutput: USILRLetter
    agriculturalDependence: USILRLetter

    @field_validator("techSophistication", mode="before")
    @classmethod
    def parse_techSophistication(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (objectType, payload) = _parse_swift_single_key_enum(v)
            if objectType == "letter":
                (_, value) = _parse_swift_single_key_enum(payload)
                objectDict = {"type": "letter", "value": value}
                return TechSophisticationLetter.model_validate(objectDict)
            elif objectType == "advanced":
                objectDict = {"type": "advanced"}
                return TechSophisticationAdvanced.model_validate(objectDict)
            elif objectType == "regressed":
                objectDict = {"type": "regressed"}
                return TechSophisticationRegressed.model_validate(objectDict)
        raise ValueError("Invalid USILR techSophistication encoding.")


class Colony(FrozenModel):
    name: Optional[str] = ""
    occupancy: OccupancyHistory
    population: int
    usilr: USILR
    government: Government
    rechargeStations: List[RechargingStationLocation]
    hpg: HyperpulseGeneratorType

    @field_validator("rechargeStations", mode="before")
    @classmethod
    def parse_rechargeStations(cls, v: Any) -> Any:
        if isinstance(v, list):
            convertedObjectsList = []
            for station in v:
                if isinstance(station, dict):
                    (value, _) = _parse_swift_single_key_enum(station)
                    convertedObjectsList.append(RechargingStationLocation(value))
            return convertedObjectsList
        return []

    @field_validator("hpg", mode="before")
    @classmethod
    def parse_hpg(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return HyperpulseGeneratorType(value)
        elif isinstance(v, str):
            return HyperpulseGeneratorType(v)
        return HyperpulseGeneratorType("none")

    def rechargeStationSummary(self) -> str:
         return ", ".join([x.displayName() for x in self.rechargeStations])

    def usilrSummary(self) -> str:
        return f"{self.usilr.techSophistication.displayName()}-{self.usilr.industrialDevelopment.displayName()}-{self.usilr.rawMaterialDependence.displayName()}-{self.usilr.industrialOutput.displayName()}-{self.usilr.agriculturalDependence.displayName()}"


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

    def summary(self):
        if isinstance(self.value, PlanetBody):
            return self.value.planetType.displayName()
        elif isinstance(self.value, int):
            return str(self.value)
        else:
            return ""


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

    def displayName(self) -> str:
        return "Empty"


class OrbitalObjectAsteroidBelt(FrozenModel):
    type: Literal["asteroidBelt"] = "asteroidBelt"
    value: AsteroidBelt

    def displayName(self) -> str:
        return "Asteroid Belt"


class OrbitalObjectDwarfTerrestrial(FrozenModel):
    type: Literal["dwarfTerrestrial"] = "dwarfTerrestrial"
    value: PlanetBody

    def displayName(self) -> str:
        return "Dwarf Terrestrial"


class OrbitalObjectTerrestrial(FrozenModel):
    type: Literal["terrestrial"] = "terrestrial"
    value: PlanetBody

    def displayName(self) -> str:
        return "Terrestrial"

class OrbitalObjectGiantTerrestrial(FrozenModel):
    type: Literal["giantTerrestrial"] = "giantTerrestrial"
    value: PlanetBody

    def displayName(self) -> str:
        return "Giant Terrestrial"


class OrbitalObjectGasGiant(FrozenModel):
    type: Literal["gasGiant"] = "gasGiant"
    value: PlanetBody

    def displayName(self) -> str:
        return "Gas Giant"


class OrbitalObjectIceGiant(FrozenModel):
    type: Literal["iceGiant"] = "iceGiant"
    value: PlanetBody

    def displayName(self) -> str:
        return "Ice Giant"


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

class SolarSystemReport(FrozenModel):
    reportId: str
    reportDate: str
    reportPreparedBy: ReportPreparedByType
    reportClassification: ReportClassificationType
    reportFooters: List[str]
    solarSystem: SolarSystem

    @field_validator("reportClassification", mode="before")
    @classmethod
    def parse_reportClassification(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return ReportClassificationType(value)
        elif isinstance(v, str):
            return ReportClassificationType(v)

    @field_validator("reportPreparedBy", mode="before")
    @classmethod
    def parse_reportPreparedBy(cls, v: Any) -> Any:
        if isinstance(v, dict):
            (value, _) = _parse_swift_single_key_enum(v)
            return ReportPreparedByType(value)
        elif isinstance(v, str):
            return ReportPreparedByType(v)

    def get_formatted_footer(self):
        return ", ".join(self.reportFooters)