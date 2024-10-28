from pydantic import BaseModel, EmailStr
from typing import List

from app.schemas.category_schema import CategoryResponse

class ProductCreate(BaseModel):
    name: str
    description: str
    handle: str
    category_id: str

class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    handle: str
    category: CategoryResponse

    # class ConfigDict:
    #     from_attributes = True