from typing import List

from pydantic import Field

from NullgModels.NullGBaseModels import NullGBaseModel
from NullgModels.NullGEnums import RecordSheetType


### Army List Models

class ArmyUnitMember(NullGBaseModel):
    """A single combat unit entry within an army list.

    Represents one pilot/crew + platform (’Mech/vehicle/etc.) and its
    scenario-facing attributes (skill, availability, points, and sheet type).

    Attributes:
        id (str | None): Unique identifier for the unit (database or external id).
        skill (str | None): Skill rating/suffix for the pilot or crew (e.g., "3+/4+").
        availability (str | None): Availability code/era tag indicating when or where the unit can be fielded.
        pilot (str | None): Pilot/crew name or callsign.
        name (str | None): Platform name (e.g., chassis/variant).
        pilotAbilities (list[str] | None): Special pilot abilities or traits (rules keywords).
        rsType (RecordSheetType | None): Record sheet type to generate or reference.
        points (str | None): Point cost/value as displayed in list building.
    """
    id: str = Field(description="", default=None)
    skill: str = Field(description="", default=None)
    availability: str = Field(description="", default=None)
    pilot: str = Field(description="", default=None)
    name: str = Field(description="", default=None)
    pilotAbilities: List[str] = Field(description="", default=None)
    rsType: RecordSheetType = Field(description="", default=None)
    points: str = Field(description="", default=None)


class ArmyListMember(NullGBaseModel):
    """A group/element within an army list (e.g., lance, star, or formation slot).

    Bundles related units and their shared metadata like formation type,
    special abilities, and accumulated points.

    Attributes:
        name (str): Display name for this group/element.
        specialAbilities (list[str]): Special abilities that apply to the group as a whole.
        type (str): Element type/category (e.g., "Lance", "Star", "Support").
        formationType (str): Formation keyword/type for rules interactions.
        pointsType (str): Points system label (e.g., "PV", "BV2", "CP").
        pointsTotal (str): Total points for this element (precomputed/serialized).
        customFields (list[str]): Free-form or keyed custom fields for UI/export.
        experience (str): Experience rating applied to the element.
        techRating (str): Tech rating or tech base tag (e.g., "IS", "Clan", letter code).
        members (list[ArmyUnitMember]): Units in this element.
    """
    name: str = Field(description="", default="")
    specialAbilities: List[str] = Field(description="", default=[])
    type: str = Field(description="", default="")
    formationType: str = Field(description="", default="")
    pointsType: str = Field(description="", default="")
    pointsTotal: str = Field(description="", default="")
    customFields: List[str] = Field(description="", default=[])
    experience: str = Field(description="")
    techRating: str = Field(description="")
    members: List[ArmyUnitMember] = Field(description="", default=[])


class ArmyList(NullGBaseModel):
    """Top-level army list container with metadata and nested elements.

    Holds list-wide tags (era, tech rating, command structure) and the
    collection of `ArmyListMember` elements that make up the force.

    Attributes:
        name (str): Army list name/title.
        subCommand (str): Sub-command label or parent formation reference.
        fiction (str): Flavor text or narrative notes for the list.
        era (str): Era tag (e.g., "3049", "Jihad", "IlClan").
        points (str): Total points for the list (precomputed/serialized).
        pointsType (str): Points system label (e.g., "PV", "BV2", "CP").
        experience (str): Default/list-wide experience rating.
        abilities (list[str]): List-wide abilities or special rules.
        type (str): List type/category (e.g., "Battalion", "Company").
        combatCommand (str): Higher command or TO&E label.
        addNotes (bool): Whether to include additional notes in exports.
        rsType (RecordSheetType): Default record sheet type for the list.
        format (str): List format identifier (e.g., export/print preset).
        techRating (str): List-wide tech base/rating.
        members (list[ArmyListMember]): Elements that compose the army.
    """

    name: str = Field(description="", default="")
    subCommand: str = Field(description="", default="")
    fiction: str = Field(description="", default="")
    era: str = Field(description="", default="")
    points: str = Field(description="", default="")
    pointsType: str = Field(description="", default="")
    experience: str = Field(description="", default="")
    abilities: List[str] = Field(description="", default=[])
    type: str = Field(description="", default="")
    combatCommand: str = Field(description="", default="")
    addNotes: bool = Field(description="", default=False)
    rsType: RecordSheetType = Field(description="", default=RecordSheetType.none)
    format: str = Field(description="", default="")
    techRating: str = Field(description="", default="")
    members: List[ArmyListMember] = Field(description="", default=[])