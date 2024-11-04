from pydantic import BaseModel, EmailStr
from typing import List

from app.api.categories.category_schema import CategoryResponse
from app.api.variants.variant_schema import VariantResponse

class ProductCreate(BaseModel):
    name: str
    description: str
    handle: str
    sku: str
    quantity: int
    cost_price: float
    selling_price: float
    category_id: str

class ProductUpdate(BaseModel):
    name: str
    description: str
    handle: str
    sku: str
    cost_price: float
    selling_price: float
    category_id: str

class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    handle: str
    sku: str
    quantity: int
    cost_price: float
    selling_price: float
    category: CategoryResponse
    # variants: List[VariantResponse]

    # class ConfigDict:
    #     from_attributes = True