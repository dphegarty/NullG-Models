from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

# -----------------------------
# Allowed MongoDB operators
# -----------------------------
ALLOWED_OPERATORS = {
    "$eq", "$ne", "$gt", "$gte", "$lt", "$lte",
    "$in", "$nin", "$regex", "$exists",
    "$and", "$or", "$nor", "$not"
}

# -----------------------------
# Recursive filter validator
# -----------------------------
def validate_filter(filter_dict: Any):
    """Recursively validate MongoDB filter structure."""
    if isinstance(filter_dict, dict):
        for key, value in filter_dict.items():
            # Check for disallowed top-level operators
            if key.startswith("$") and key not in ALLOWED_OPERATORS:
                raise ValueError(f"Operator '{key}' is not allowed.")

            # Recurse into nested dicts or lists
            if isinstance(value, (dict, list)):
                validate_filter(value)
    elif isinstance(filter_dict, list):
        for item in filter_dict:
            validate_filter(item)
    # Scalars (str, int, etc.) are safe


# -----------------------------
# Models
# -----------------------------
class MongoQuery(BaseModel):
    filter: Dict[str, Any] = Field(default_factory=dict)

    def validate_security(self):
        validate_filter(self.filter)
