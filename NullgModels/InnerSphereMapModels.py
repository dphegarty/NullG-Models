from typing import Optional, List

from pydantic import BaseModel, Field, AnyHttpUrl


class Coordinates3D(BaseModel):
    """
    Represents 3D coordinates with additional metadata.

    This class is a data model for representing a point in a 3D coordinate space
    along with associated metadata such as cluster number, p-value, and related
    parameters. It provides a structured way to organize and store information
    about a point's position and its associated statistical data.

    Attributes:
        x: x coordinate.
        y: y coordinate.
        z: z coordinate.
        cluster: cluster number. This is used for Faction control
        p: p-value.
        p_raw: raw p-value.
        r_check: r check value.
    """
    x: float = Field(description="x coordinate", default=0.0)
    y: float = Field(description="y coordinate", default=0.0)
    z: float = Field(description="z coordinate", default=0.0)
    cluster: int = Field(description="cluster number", default=0)
    p: float = Field(description="p value", default=0.0)
    p_raw: float = Field(description="raw p value", default=0.0)
    r_check: float = Field(description="r check value", default=0.0)

class CoordinatesItem(BaseModel):
    """
    Represents an item containing a name, description, and 3D coordinates.

    This class is used to define a structured representation for an item that includes
    a name for identification, a description for additional context, and 3D coordinates
    to store positional data. It serves as a data model to organize and validate these
    attributes when handling structured data.

    Attributes:
        name: Name of the item.
        description: Description of the item.
        coords: 3D coordinates.
    """
    name: str = Field(description="", default="")
    description: str = Field(description="", default="")
    coords: Coordinates3D = Field(description="3D coordinates", default=Coordinates3D)

class SizeItem(BaseModel):
    """
    Representation of a Size Item.

    This class is designed to manage size-related data with three integer
    attributes: `a`, `b`, and `c`. It provides default values and descriptions
    for each attribute to ensure clarity and consistency during use.

    Attributes:
        a: a value.
        b: b value.
        c: c value.
    """
    a: int = Field(description="a value", default=0)
    b: int = Field(description="b value", default=0)
    c: int = Field(description="c value", default=0)

class StarSystemControlHistoryRecord(BaseModel):
    """
    Represents a control history record with its associated details.

    This class is used to model the historic control data for a specific faction
    during a particular year. It contains attributes to define the year when
    the control was in effect and the corresponding faction identifying data.

    Attributes:
        id: Unique ID of the star system.
        year: Year this takes effect.
        factionId: Faction Id.
    """
    id: int = Field(description="Unique ID of the star system", default=0)
    year: int = Field(description="Year this takes effect", default=0, examples=[3025, 3050])
    factionId: int = Field(description="Faction Id", default=0)

class StarSystem(BaseModel):
    """
    Representation of a star system with various attributes and metadata.

    This class models the properties and metadata of a star system, including its
    identifier, name, coordinates, size, star type, planets, control history, and
    other related details.

    Attributes:
        id: Unique ID of the system.
        systemName: Name of the system.
        alternateName: Alternate name(s) for the system.
        coordinates: Coordinates of the system.
        size: Size of the system.
        sarnaLink: Link to Sarna for the system.
        distance: Distance from Sol in Light years.
        starSpectralClass: Spectral class of the star.
        rechargeTime: Recharge time in hours for Jumpships.
        planets: Number of planets in the system.
        rechargeStations: List of recharge station locations.
        controlHistory: List of control history records.
    """
    id: int = Field(description="Unique ID of the system", default=0)
    systemName: str = Field(description="", default="")
    alternateName: List[str] = Field(description="Alternate Name", default_factory=list)
    coordinates: List[CoordinatesItem] = Field(description="", default_factory=list)
    size: SizeItem = Field(description="Size of the system", default="")
    sarnaLink: AnyHttpUrl = Field(description="Link to Sarna", default="")
    distance: float = Field(description="Distance from Sol in Light years", default=0.0)
    starSpectralClass: str = Field(description="Spectral class of the star", default="")
    rechargeTime: int = Field(description="Recharge time in hours", default=0)
    planets: int = Field(description="Number of planets in the system", default=0)
    rechargeStations: List[str] = Field(description="List of recharge station locations", default_factory=list)
    controlHistory: List[StarSystemControlHistoryRecord] = Field(description="List of control history records", default_factory=list)

class InnerSphereFactionRecord(BaseModel):
    """
    Represents a record for an Inner Sphere faction.

    This class models details about an Inner Sphere faction, including its
    identifier, abbreviation, full name, color, active years, and a link to its
    Sarna entry. It serves as a data structure to store details about factions
    in the Inner Sphere, providing easy access to faction-specific metadata.

    Attributes:
        id: Faction Id.
        factionAbbr: Faction Abbreviation.
        factionName: Faction Name.
        color: Faction HTML Color.
        startYear: Start Year.
        endYear: End Year.
        sarnaLink: Link to Sarna.
    """
    id: int = Field(description="Faction Id", default=0)
    factionAbbr: str = Field(description="Faction Abbreviation", default="")
    factionName: str = Field(description="Faction Name", default="")
    color: Optional[str] = Field(description="Faction HTML Color", default="")
    startYear: Optional[int] = Field(description="Start Year", default=0)
    endYear: Optional[int] = Field(description="End Year", default=0)
    sarnaLink: Optional[AnyHttpUrl] = Field(description="Link to Sarna", default="")
