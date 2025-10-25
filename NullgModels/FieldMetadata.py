from typing import Optional, List

from pydantic import BaseModel


class FieldMetadata(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    operators: Optional[List[str]] = None
    example: Optional[str] = None
    category: Optional[str] = None


class MetadataResponse(BaseModel):
    fields: List[FieldMetadata]