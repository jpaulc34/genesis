from pydantic import BaseModel, EmailStr
from typing import List

from app.api.categories.category_schema import CategoryResponse
from app.api.variants.variant_schema import VariantResponse

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
    # variants: List[VariantResponse]

    # class ConfigDict:
    #     from_attributes = True