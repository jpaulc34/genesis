from pydantic import BaseModel, EmailStr, PositiveInt
from typing import List

from app.api.categories.category_schema import CategoryResponse

class ProductCreate(BaseModel):
    name: str
    description: str
    handle: str
    sku: str
    quantity: PositiveInt
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
    quantity: PositiveInt
    cost_price: float
    selling_price: float
    category: CategoryResponse