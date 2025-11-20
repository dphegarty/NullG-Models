# NullG-Models

**Version:** 0.1.10

## Overview

NullG-Models is a Python library that provides a comprehensive collection of data models, enumerations, and utility classes for managing Battletech-related data. It is designed to support the NullG APIs by offering type-safe structures for units, equipment, pilots, and game mechanics across different rule sets (Total Warfare, Alpha Strike, etc.).
The concept is to provide concert models for the data that is used in the API and to provide a layer of abstraction to make it easier to work with the data. These models should remain simple so they can be easily translated to other languages.

* Right now the focus is on the Battletech universe, but the library is designed to be extensible to other rulesets.
* API site: https://api.nullg.tech/docs

## Features

*   **Core Data Models:**  Pydantic or similar structured models for Battletech units, equipment, and inventory.
*   **Game System Support:**  Handling for *Total Warfare*, *Alpha Strike*, and *HardWar* game systems.
*   **Type-Safe Enumerations:**  Extensive collection of enums for tech bases, unit types, weight classes, equipment types, and more to ensure data consistency.
*   **Equipment Management:**  Models covering weapons, ammo, engines, gyros, and other components.
*   **Validation:**  Built-in logic to validate unit legality (Official, User Created, Apocryphal, Illegal).
*   **Integration Ready:**  Includes connector utilities and field metadata for easier API integration.

## Project Structure

The library is organized into the following modules:

*   `NullgModels/`
    *   `NullGEnums.py`:  Central definition of all enumeration types (e.g., `TechbaseType`, `UnitType`, `WeightClassType`).
    *   `BattletechModels.py`:  Core models specific to the Battletech universe.
    *   `AlphaStrikeModels.py`:  Models specific to the Alpha Strike ruleset.
    *   `TotalWarModels.py`:  Models specific to the Total Warfare ruleset.
    *   `PilotModels.py`:  Definitions for pilots, experience levels, and skills.
    *   `EquipmentModels.py`:  Detailed breakdowns of equipment components.
    *   `NullGBaseModels.py`:  Base classes and common shared logic.
    *   `InventoryModels.py`:  Handling user collections and storage states.
    *   `Constants.py`:  System-wide constants.
*   `Utils/`:  Helper scripts including introspection and connectors.

## Installation

Ensure you have Python 3.9+ installed.

1.  Clone the repository.
2.  Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage Examples

### Using Enums

The `NullGEnums` module provides semantic clarity for integer-based database fields.

```python
from NullgModels.NullGEnums import TechbaseType, UnitType, EquipmentType

# Example: Checking for Clan Tech
tech_id = 1
if tech_id == TechbaseType.clan:
    print("This is a Clan unit.")

# Example: Filtering for Mechs
unit_filter = {"unitTypeId": UnitType.mech}
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.