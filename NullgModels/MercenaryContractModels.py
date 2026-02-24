from __future__ import annotations

from enum import IntEnum
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field, ConfigDict


# -----------------------------
# Enums
# -----------------------------

class MercenaryContractStatusType(IntEnum):
    new = 0
    accepted = 1
    inProgress = 2
    completed = 3
    declined = 4
    failed = 5
    breached = 6

    @classmethod
    def title(cls, v: MercenaryContractStatusType) -> str:
        print(">" + v.name + "<")
        return {
            cls.new: "New",
            cls.accepted: "Accepted",      # keeping your original spelling
            cls.inProgress: "In Progress",
            cls.breached: "Breached",
            cls.completed: "Completed",
            cls.failed: "Failed",
            cls.declined: "Declined",
        }[v]

    @classmethod
    def rgba(cls, v: MercenaryContractStatusType, alpha: float = 0.8) -> Tuple[str, float]:
        """
        Swift returns UIColor. In Python, we return a semantic color name + alpha.
        If you prefer hex, change the mapping to '#RRGGBB'.
        """
        return {
            cls.new: ("systemGray", alpha),
            cls.accepted: ("systemBlue", alpha),
            cls.inProgress: ("systemOrange", alpha),
            cls.breached: ("systemRed", alpha),
            cls.completed: ("systemGreen", alpha),
            cls.failed: ("systemPurple", alpha),
            cls.declined: ("systemPink", alpha),
        }[v]

    def __str__(self) -> str:
        return self.title(self)

class MercenaryContractType(IntEnum):
    none = 0
    invasion = 1
    garrison = 2
    raid = 3
    expedition = 4

    @classmethod
    def title(cls, v: MercenaryContractType) -> str:
        return {
            cls.none: "None",
            cls.invasion: "Invasion",
            cls.garrison: "Garrison",
            cls.raid: "Raid",
            cls.expedition: "Expedition",
        }[v]

    def __str__(self) -> str:
        return self.title(self)

    @classmethod
    def image_name(cls, v: MercenaryContractType) -> Optional[str]:
        """
        Swift returns UIImage?. In Python, we typically store the asset key/path
        and let the UI layer load it.
        """
        return {
            cls.none: "mc_none",
            cls.invasion: "mc_invasion",
            cls.garrison: "mc_garrison",
            cls.raid: "mc_raid",
            cls.expedition: "mc_expedition",
        }[v]


class MercenaryContractEmployerType(IntEnum):
    none = 0
    civilian = 1
    planetaryGovernment = 2
    mercenarySubcontract = 3
    corporation = 4
    houseGovernment = 5
    noble = 6

    @classmethod
    def title(cls, v: "MercenaryContractEmployerType") -> str:
        return {
            cls.none: "None",
            cls.civilian: "Civilian",
            cls.planetaryGovernment: "Planetary Government",
            cls.mercenarySubcontract: "Mercenary Subcontract",
            cls.corporation: "Corporation",
            cls.houseGovernment: "House Government",
            cls.noble: "Noble",
        }[v]

    def __str__(self) -> str:
        return self.title(self)

# -----------------------------
# Models (Swift structs)
# -----------------------------

class MercenaryContractEvent(BaseModel):
    month: int = 0
    event: str = ""
    cost: int = 0
    paid: int = 0
    cover: int = 0
    balance: int = 0
    rep: int = 0


class MercenaryContract(BaseModel):
    model_config = ConfigDict(use_enum_values=False)
    contractStatus: MercenaryContractStatusType = MercenaryContractStatusType.new
    contractId: str

    contractName: str = ""
    payRateRoll: int = 0
    commandRightsRoll: int = 0
    salvageRightsRoll: int = 0
    supportRightsRoll: int = 0
    transportationTermRoll: int = 0
    employerRoll: int = 0
    contractTypeRoll: int = 0
    useEmployerTable: bool = False
    useContractTypeTable: bool = False

    stepOriginalPayRate: int = 0
    stepOriginalCommandRights: int = 0
    stepOriginalSalvageRights: int = 0
    stepOriginalSupportRights: int = 0
    stepOriginalTransportationTerm: int = 0

    stepModifierPayRate: int = 0
    stepModifierCommandRights: int = 0
    stepModifierSalvageRights: int = 0
    stepModifierSupportRights: int = 0
    stepModifierTransportationTerm: int = 0

    lengthInMonths: int = 0

    stepNegotiatedPayRate: int = 0
    stepNegotiatedCommandRights: int = 0
    stepNegotiatedSalvageRights: int = 0
    stepNegotiatedSupportRights: int = 0
    stepNegotiatedTransportationTerm: int = 0

    payRate: str = ""
    commandRights: str = ""
    salvageRights: str = ""
    supportRights: str = ""
    transportationTerm: str = ""

    employerType: MercenaryContractEmployerType = MercenaryContractEmployerType.none
    contractType: MercenaryContractType = MercenaryContractType.none

    acceptableTerms: bool = True
    reputationValue: int = 0

    stepBasePayRate: int = 0
    stepBaseCommandRights: int = 0
    stepBaseSalvageRights: int = 0
    stepBaseSupportRights: int = 0
    stepBaseTransportationTerm: int = 0

    contractEvents: List[MercenaryContractEvent] = Field(default_factory=list)