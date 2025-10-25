# utils/introspection.py
from typing import Any, List, get_origin, get_args, Dict
from pydantic import BaseModel
from NullgModels.FieldMetadata import FieldMetadata


DEFAULT_OPERATORS = {
    "integer": ["$eq", "$gte", "$lte"],
    "float": ["$eq", "$gte", "$lte"],
    "string": ["$eq", "$regex"],
    "array[string]": ["$in", "$regex"],
    "array[integer]": ["$in"],
    "boolean": ["$eq"],
    "dict[string, any]": ["$eq", "$regex", "$gt", "$gte", "$lt", "$lte"],
}


def get_type_name(py_type: Any) -> str:
    args = get_args(py_type)
    if isinstance(args, tuple) and len(args) > 0:
        py_type = args[0]
    if get_origin(py_type) in (list, List):
        arg = get_args(py_type)[0] if get_args(py_type) else "any"
        return f"array[{get_type_name(arg)}]"
    elif get_origin(py_type) in (dict, Dict):
        dict_arg = get_args(py_type)
        first_arg = get_type_name(dict_arg[0])
        second_arg = get_type_name(dict_arg[1])
        return f"dict[{first_arg}, {second_arg}]"
    elif py_type == str or str in get_args(py_type):
        return "string"
    elif py_type == int or int in get_args(py_type):
        return "integer"
    elif py_type == float or float in get_args(py_type):
        return "float"
    elif py_type == bool or bool in get_args(py_type):
        return "boolean"
    elif py_type == Any:
        return "any"
    elif hasattr(py_type, "__name__"):
        return py_type.__name__
    return str(py_type)


def walk_model_fields(model: type[BaseModel], prefix: str = "", category: str = None) -> List[FieldMetadata]:
    """Recursively collect nested field metadata (Pydantic v2-safe)."""
    raw_fields: List[FieldMetadata] = []
    for name, field in model.model_fields.items():
        field_name = f"{prefix}.{name}" if prefix else name
        field_type = get_type_name(field.annotation)
        desc = field.description or "No description"

        # ✅ get the first example if available
        examples = []
        if hasattr(field, "examples") and field.examples:
            examples = field.examples
        elif getattr(field, "json_schema_extra", None):
            examples = field.json_schema_extra.get("examples", [])
        example = str(examples[0]) if examples else None

        operators = DEFAULT_OPERATORS.get(field_type)
        current_category = category or prefix.split(".")[0] if prefix else name

        field_args = get_args(field.annotation)
        if not field_args:
            field_args = (field.annotation,)
        for arg in field_args:
            if arg is type(None):
                continue
            # recurse into submodels
            if hasattr(arg, "model_fields"):
                raw_fields += walk_model_fields(arg, field_name, current_category)
            elif get_origin(arg) in (list, List):
                args = get_args(arg)
                if args and hasattr(args[0], "model_fields"):
                    raw_fields += walk_model_fields(args[0], field_name, current_category)
                else:
                    raw_fields.append(FieldMetadata(
                        name=field_name, type=field_type, description=desc,
                        operators=operators, example=example, category=current_category
                    ))
            else:
                raw_fields.append(FieldMetadata(
                    name=field_name, type=field_type, description=desc,
                    operators=operators, example=example, category=current_category
                ))
    ## Dedup fields from the TotalWar models
    included_fields = set()
    fields: List[FieldMetadata] = []
    for field in raw_fields:
        if field.name not in included_fields:
            included_fields.add(field.name)
            fields.append(field)
    return fields
