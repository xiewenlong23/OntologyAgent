from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ObjectTypeDefinition(BaseModel):
    id: str
    api_name: str
    display_name: str
    description: Optional[str] = None
    status: str = "active"
    properties: list[str] = []
    relations: list[str] = []


class PropertyDefinition(BaseModel):
    id: str
    api_name: str
    display_name: str
    type: str  # string, int, float, bool, datetime
    description: Optional[str] = None
    status: str = "active"


class LinkTypeDefinition(BaseModel):
    id: str
    api_name: str
    display_name: str
    source_object_type: str
    target_object_type: str
    cardinality: str  # one-to-one, one-to-many, many-to-many
    description: Optional[str] = None
    status: str = "active"


class ObjectCreate(BaseModel):
    object_type: str
    api_name: str
    display_name: str
    properties: dict = {}


class ObjectResponse(ObjectCreate):
    id: str
    tenant_id: str
    created_at: datetime
    updated_at: datetime
